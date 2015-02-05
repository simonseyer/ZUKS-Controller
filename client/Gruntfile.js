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
    mkdir: {
      default: {
        options: {
          create: ['dist/controller', 'dist/client']
        }
      }
    },
    vulcanize: {
      default: {
        files: {
          'dist/controller/index.long.html': 'controller.html',
          'dist/client/index.long.html': 'client.html'
        }
      },
    },
    minifyHtml: {
        default: {
            files: {
                'dist/controller/index.html': 'dist/controller/index.long.html',
                'dist/client/index.html': 'dist/client/index.long.html'
            }
        }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-vulcanize');
  grunt.loadNpmTasks('grunt-devtools');
  grunt.loadNpmTasks('grunt-minify-html');
  grunt.loadNpmTasks('grunt-mkdir');

  grunt.registerTask('deploy', ['mkdir', 'vulcanize', 'minifyHtml']);
};
