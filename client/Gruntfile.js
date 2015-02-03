module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      code: {
        files: ['components/**', 'index.html'],
        options: {
          livereload: true
        }
      }     
    },
    vulcanize: {
      default: {
        options: {},
        files: {
          'build.html': 'index.html'
        }
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-vulcanize');
  grunt.loadNpmTasks('grunt-devtools');
};
