module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    less: {
      bootstrap: {
        options: {
            paths: 'components/bootstrap/less/'
        },
        files: {
            'public/css/bootstrap.css': ['main/static/css/bootstrap-overrides.less'],
        }
      },
      css: {
        files: {
          'public/css/main.css': ['main/static/css/main.less']
        }
      },
      min: {
        options: {
            yuicompress: true,
            paths: 'components/bootstrap/less/'
        },
        files: {
            'public/css/bootstrap.min.css': ['main/static/css/bootstrap-overrides.less'],
            'public/css/main.min.css': ['main/static/css/main.less']
        }
      }
    },
    coffee: {
      compile: {
        files: {
          'public/js/app.js': 'main/static/scripts/main.coffee'
        }
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      jquery: {
        files: {
          'public/js/jquery.min.js': ['components/jquery/jquery.js']
        }
      },
      bootstrap: {
        files: {
          'public/js/bootstrap.min.js': ['components/bootstrap/js/*.js']
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
        files: 'main/static/css/main.less',
        tasks: ['less:css']
      },
      bootstrap: {
        files: 'main/static/css/bootstrap-overrides.less',
        tasks: ['less']
      },
      coffee: {
        files: ['main/static/scripts/main.coffee'],
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
