module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    recess: {
      options: {
        compile: true
      },
      bootstrap: {
        files: {
            'public/css/bootstrap.css': ['components/bootstrap/less/bootstrap.less'],
            'public/css/main.css': ['main/static/css/main.less']
        }
      },
      min: {
        options: {
            compress: true
        },
        files: {
            'public/css/bootstrap.min.css': ['components/bootstrap/less/bootstrap.less'],
            'public/css/main.min.css': ['main/static/css/main.less']
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
      }
    },
    watch: {
      recess: {
        files: 'main/static/css/main.less',
        tasks: ['recess']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-recess');

  grunt.registerTask('default', ['recess', 'uglify']);
};
