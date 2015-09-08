module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    less: {
      bootstrap: {
        options: {
            paths: 'components/bootstrap/less/'
        },
        files: {
            'public/css/bootstrap.css': ['core/static/css/bootstrap-overrides.less'],
        }
      },
      css: {
        files: {
          'public/css/{{project_name}}.css': ['core/static/css/{{project_name}}.less']
        }
      },
      min: {
        options: {
            yuicompress: true,
            paths: 'components/bootstrap/less/'
        },
        files: {
            'public/css/bootstrap.min.css': ['core/static/css/bootstrap-overrides.less'],
            'public/css/{{project_name}}.min.css': ['core/static/css/{{project_name}}.less']
        }
      }
    },
    coffee: {
      compile: {
        files: {
          'public/js/app.js': 'core/static/scripts/{{project_name}}.coffee'
        }
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      jquery: {
        files: {
          'public/js/jquery.min.js': ['components/jquery/dist/jquery.js']
        }
      },
      bootstrap: {
        files: {
          'public/js/bootstrap.min.js': ['components/bootstrap/dist/js/bootstrap.min.js']
        }
      },
      modernizr: {
        files: {
          'public/js/modernizr.min.js': ['components/modernizr/modernizr.js']
        }
      },
      app: {
        files: {
          'public/js/app.min.js': ['public/js/app.js']
        }
      }
    },
    watch: {
      options: {
        livereload: true
      },
      less: {
        files: 'core/static/css/{{project_name}}.less',
        tasks: ['less:css']
      },
      bootstrap: {
        files: 'core/static/css/bootstrap-overrides.less',
        tasks: ['less']
      },
      coffee: {
        files: ['core/static/scripts/{{project_name}}.coffee'],
        tasks: ['coffee']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-coffee');

  grunt.registerTask('default', ['less', 'coffee', 'uglify']);
};
