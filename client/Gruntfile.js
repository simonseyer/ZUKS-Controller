module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      code: {
        files: ['components/**', 'client.html', 'controller.html', 'demo.html', 'demo/*'],
        options: {
          livereload: true
        }
      },
      css: {
        files: '**/*.scss',
				tasks: ['sass']
      }
    },
    settings: grunt.file.readJSON('settings.json'),
    prompt: {
      default: {
        options: {
          questions: [
            {
              config: 'settings.serverURL',
              type: 'input',
              message: 'Please enter the backend server url',
              default: '<%- settings.serverURL %>',
              filter:  function(value) {
                // Append trailing slash
                if (value.substr(-1) !== "/") {
                  return value + "/";
                }
                return value;
              }
            },
            {
              config: 'settings.websocketServerURL',
              type: 'input',
              message: 'Please enter the websocket server url',
              default: '<%- settings.websocketServerURL %>'
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
            replace: '$1"<%= settings.serverURL %>"$2'
          },
          {
            name: 'Update websocket server url',
            search: '(\\/\\*SETTINGS:websocket-server-url\\*\\/).*(\\/\\*END_SETTINGS\\*\\/)',
            replace: '$1"<%= settings.websocketServerURL %>"$2'
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
          'dist/controller/index.html': 'controller.html',
          'dist/client/index.html': 'client.html',
          'dist/demo/index.html': 'demo.html'
        }
      },
      compress: {
        options: {
          strip: true
        },
        files: {
          'dist/controller/index.html': 'dist/controller/index.html',
          'dist/client/index.html': 'dist/client/index.html',
          'dist/demo/index.html': 'dist/demo/index.html'
        }
      },
    },
    sass: {
      default: {
        files: {
          'demo/demo.css': 'demo/demo.scss'
        }
      },
      deploy: {
        options: {
          style: 'compressed'
        },
        files: {
          'dist/demo/demo/demo.css': 'demo/demo.scss'
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
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-devtools');
  grunt.loadNpmTasks('grunt-mkdir');
  grunt.loadNpmTasks('grunt-regex-replace');
  grunt.loadNpmTasks('grunt-prompt');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.registerTask('saveSettings', 'Stores the configured settings in the settings.json file', function() {
    grunt.file.write('settings.json', JSON.stringify(grunt.config('settings'), null, 4));
  });

  grunt.registerTask('install', ['mkdir', 'vulcanize:default', 'sass:deploy', 'copy', 'prompt', 'saveSettings', 'regex-replace', 'vulcanize:compress']);
  grunt.registerTask('deploy', ['mkdir', 'vulcanize:default', 'sass:deploy', 'copy', 'regex-replace', 'vulcanize:compress']);
};
