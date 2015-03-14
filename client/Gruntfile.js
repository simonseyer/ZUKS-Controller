module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      code: {
        files: ['components/**', 'client.html', 'controller.html', 'demo.html'],
        options: {
          livereload: true
        }
      }     
    },
    mkdir: {
      default: {
        options: {
          create: ['dist/controller', 'dist/client', 'dist/demo']
        }
      }
    },
    vulcanize: {
      default: {
        files: {
          'dist/controller/index.long.html': 'controller.html',
          'dist/client/index.long.html': 'client.html',
          'dist/demo/index.long.html': 'demo.html'
        }
      },
    },
    minifyHtml: {
        default: {
            files: {
                'dist/controller/index.html': 'dist/controller/index.long.html',
                'dist/client/index.html': 'dist/client/index.long.html',
                'dist/demo/index.html': 'dist/demo/index.long.html'
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
