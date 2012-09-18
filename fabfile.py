from os.path import join, exists
from fabric import utils
from fabric.api import run, env, local, sudo, put, require, cd
from fabric.contrib.project import rsync_project

RSYNC_EXCLUDE = (
    '.git',
    '.gitignore',
    '.bzr',
    '.bzrignore',
    '*.pyc',
    '*.db',
    'fabfile.py',
    'bootstrap.py',
    'reload',
    'save-fixtures',
    'media/*',
    'static',
)

env.home = '/var/www/{{ project_name }}'
env.project = '{{ project_name }}'
DOMAIN = '{{ project_name }}.com'


def _setup_path():
    env.root = join(env.home, env.environment)
    env.code_root = join(env.root, env.project)


def staging():
    env.user = 'django'
    env.environment = 'staging'
    env.hosts = [DOMAIN]
    env.host = DOMAIN
    _setup_path()


def production():
    utils.abort("No production server defined")


def touch():
    """Touch wsgi file to trigger reload."""
    require('code_root', provided_by=('staging', 'production'))
    conf_dir = join(env.code_root, env.project)
    with cd(conf_dir):
        run('touch wsgi.py')


def apache_reload():
    sudo('service apache2 reload', shell=False)


def initial_setup():
    """Setup virtualenv"""
    sudo('pip install virtualenv', shell=False)
    run('mkdir -p %(home)s' % env)
    with cd(env.home):
        run('virtualenv --no-site-packages %(environment)s' % env)
    put('requirements.txt', env.root)
    with cd(env.root):
        run('. ./bin/activate; pip install -r requirements.txt')


def update_vhost():
    local('cp config/%(project)s.conf /tmp' % env)
    local('sed -i s#%%ROOT%%#%(home)s#g /tmp/%(project)s.conf' % env)
    local('sed -i s/%%PROJECT%%/%(project)s/g /tmp/%(project)s.conf' % env)
    local('sed -i s/%%ENV%%/%(environment)s/g /tmp/%(project)s.conf' % env)
    local('sed -i s/%%DOMAIN%%/%(host)s/g /tmp/%(project)s.conf' % env)
    put('/tmp/%(project)s.conf' % env, '%(root)s' % env)
    sudo('cp %(root)s/%(project)s.conf ' % env +
         '/etc/apache2/sites-available/%(project)s' % env, shell=False)
    sudo('a2ensite %(project)s' % env, shell=False)


def rsync():
    require('root', provided_by=('staging', 'production'))
    extra_opts = '--omit-dir-times'
    rsync_project(
        env.root,
        exclude=RSYNC_EXCLUDE,
        delete=True,
        extra_opts=extra_opts
    )


def copy_local_settings():
    require('code_root', provided_by=('staging', 'production'))
    local_settings = 'config/local_settings_%(environment)s.py' % env
    if exists(local_settings):
        put(local_settings, env.code_root)
        with cd(env.code_root):
            run('mv local_settings_%(environment)s.py local_settings.py' % env)


def collectstatic():
    with cd(env.code_root):
        run('source ../bin/activate; python manage.py collectstatic --noinput')


def configtest():
    run("apache2ctl configtest")


def deploy():
    rsync()
    copy_local_settings()
    collectstatic()
    update_vhost()
    configtest()
    apache_reload()
