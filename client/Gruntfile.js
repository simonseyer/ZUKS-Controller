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
    prompt: {
      default: {
        options: {
          questions: [
            {
              config: 'server.url',
              type: 'input',
              message: 'Please enter the backend server url',
              default: 'http://localhost:8000/',
              filter:  function(value) {
                // Append trailing slash
                if (value.substr(-1) !== "/") {
                  return value + "/";
                }
                return value;
              }
            },
            {
              config: 'websocket.server.url',
              type: 'input',
              message: 'Please enter the websocket server url',
              default: 'ws://localhost:8888/ws'
            }
          ]
        }
      },
    },
    "regex-replace": {
      default: {
        src: ['dist/controller/index.html','dist/client/index.html', 'dist/demo/index.html'],
        actions: [
          {
            name: 'Update server url',
            search: '(\\/\\*SETTINGS:server-url\\*\\/).*(\\/\\*END_SETTINGS\\*\\/)',
            replace: '$1"<%= server.url %>"$2'
          },
          {
            name: 'Update websocket server url',
            search: '(\\/\\*SETTINGS:websocket-server-url\\*\\/).*(\\/\\*END_SETTINGS\\*\\/)',
            replace: '$1"<%= websocket.server.url %>"$2'
          }
        ]
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
    },
    copy: {
      default: {
        files: [
          {'expand': true, 'src' : ['bower_components/**', 'components/**'], 'dest' : 'dist/controller'},
          {'expand': true, 'src' : ['bower_components/**', 'components/**'], 'dest' : 'dist/client'},
          {'expand': true, 'src' : ['bower_components/**', 'components/**', 'demo/*'], 'dest' : 'dist/demo'},
        ],
      },
    },
  });
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-vulcanize');
  grunt.loadNpmTasks('grunt-devtools');
  grunt.loadNpmTasks('grunt-minify-html');
  grunt.loadNpmTasks('grunt-mkdir');
  grunt.loadNpmTasks('grunt-regex-replace');
  grunt.loadNpmTasks('grunt-prompt');
  grunt.loadNpmTasks('grunt-contrib-copy');

  grunt.registerTask('deploy', ['mkdir', 'vulcanize', 'minifyHtml', 'copy']);
  grunt.registerTask('install', ['deploy','prompt', 'regex-replace']);
};
