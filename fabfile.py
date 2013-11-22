from os.path import join, exists
from fabric.api import run, env, local, sudo, put, require, cd, roles, task
from fabric.contrib.project import rsync_project
from fabric.context_managers import prefix

RSYNC_EXCLUDE = (
    '.git',
    '.gitignore',
    '.bzr',
    '.bzrignore',
    '*.pyc',
    '*.db',
    'fabfile.py',
    'media',
    'static'
)

env.home = '/srv/django'
env.project = '{{ project_name }}'
env.requirements_file = 'config/requirements.pip'


def _setup_path():
    env.root = join(env.home, env.domain)
    env.code_root = join(env.root, env.project)


@task
def staging():
    env.user = 'django'
    env.environment = 'staging'
    env.domain = "{{ project_name }}.strycore.com"
    env.roledefs = {
        'web': [env.domain],
    }
    _setup_path()


@task
def production():
    env.user = 'django'
    env.environment = 'production'
    env.domain = '{{ project_name }}.com'
    env.roledefs = {
        'web': [env.domain],
    }
    _setup_path()


def activate():
    return prefix('source %s/bin/activate' % env.root)


@task
def touch():
    """Touch wsgi file to trigger reload."""
    require('code_root', provided_by=('staging', 'production'))
    conf_dir = join(env.code_root, env.project)
    with cd(conf_dir):
        run('touch wsgi.py')


@task
@roles('web')
def apache_reload():
    sudo('service apache2 reload', shell=False)


@task
@roles('web')
def setup():
    """Setup virtualenv"""
    run('mkdir -p %(root)s' % env)
    with cd(env.root):
        run('virtualenv --no-site-packages .')


@task
@roles('web')
def requirements():
    with cd(env.code_root):
        with activate():
            run('pip install --requirement {0}'.format(env.requirements_file))


@task
@roles('web')
def update_vhost():
    local('cp config/%(project)s.conf /tmp' % env)
    local('sed -i s#%%ROOT%%#%(root)s#g /tmp/%(project)s.conf' % env)
    local('sed -i s/%%PROJECT%%/%(project)s/g /tmp/%(project)s.conf' % env)
    local('sed -i s/%%ENV%%/%(environment)s/g /tmp/%(project)s.conf' % env)
    local('sed -i s/%%DOMAIN%%/%(domain)s/g /tmp/%(project)s.conf' % env)
    put('/tmp/%(project)s.conf' % env, '%(root)s' % env)
    sudo('cp %(root)s/%(project)s.conf ' % env +
         '/etc/apache2/sites-available/%(domain)s' % env, shell=False)
    sudo('a2ensite %(domain)s' % env, shell=False)


@task
@roles('web')
def rsync():
    require('root', provided_by=('staging', 'production'))
    extra_opts = '--omit-dir-times'
    rsync_project(
        env.root,
        exclude=RSYNC_EXCLUDE,
        delete=True,
        extra_opts=extra_opts
    )


@task
@roles('web')
def copy_local_settings():
    local_settings = 'config/local_settings_%(environment)s.py' % env
    if exists(local_settings):
        put(local_settings, env.code_root)
        with cd(env.code_root):
            run('mv local_settings_%(environment)s.py %(project)s/local_settings.py' % env)


@task
@roles('web')
def syncdb():
    require('code_root', provided_by=('stating', 'production'))
    with cd(env.code_root):
        with activate():
            run("python manage.py syncdb --noinput")


@task
@roles('web')
def pull():
    with cd(env.code_root):
        run('git pull')


@task
@roles('web')
def migrate():
    with cd(env.code_root):
        with activate():
            run("python manage.py migrate")


@task
@roles('web')
def collectstatic():
    with cd(env.code_root):
        with activate():
            run('python manage.py collectstatic --noinput')


@task
@roles('web')
def configtest():
    sudo("apache2ctl configtest")


@task
@roles('web')
def fix_perms(user="www-data"):
    with cd(env.code_root):
        run("mkdir -p media")
        run("mkdir -p static")
        sudo("chmod -R ug+w .")
        sudo("chown -R %s.%s media" % (user, env.user))
        sudo("chown -R %s.%s static" % (user, env.user))


@task
@roles('web')
def deploy():
    rsync()
    requirements()
    fix_perms(env.user)
    copy_local_settings()
    collectstatic()
    update_vhost()
    configtest()
    fix_perms()
    apache_reload()


@task
@roles('web')
def fastdeploy():
    rsync()
    touch()
