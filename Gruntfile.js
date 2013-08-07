module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    recess: {
      options: {
        compile: true
      },
      bootstrap: {
        files: {
            'public/css/bootstrap.css': ['components/bootstrap/less/bootstrap.less']
        }
      },
      min: {
        options: {
            compress: true
        },
        files: {
            'public/css/bootstrap.min.css': ['components/bootstrap/less/bootstrap.less']     
        }
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      build: {
        src: 'components/jquery/jquery.js',
        dest: 'public/js/jquery.min.js'
      }
    },
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-recess');

  grunt.registerTask('default', ['recess', 'uglify']);
};
