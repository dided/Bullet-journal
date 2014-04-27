module.exports = function(grunt) {
  'use strict';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      options: {
        separator: ';'
      },
      dist: {
        src: [
            '/static/js/bower_components/angular/angular.js',
            '/static/js/bower_components/angular-bootstrap3/ui-bootstrap-tpls.js',
            '/static/js/bower_components/angular-resource/angular-resource.js',
            '/static/js/bower_components/angular-route/angular-route.js',		
            '/static/js/**/*.js'
	],
        dest: 'static/dist/js/app.js'
      }
    },  
    uglify: {
      dist: {
        files: {
          'static/dist/js/app.min.js': ['<%= concat.dist.dest %>']
        }
      }
    },	
    less: {	 
      development: {
            options: {
              paths: [""]
            },
            files:{
              "/static/dist/css/app.css": "/static/less/*.less",
            }
      },
      production: {
        options: {
              paths: [""],
              cleancss: true,
            },
            files: [{
              "dist/css/app.css": ["less/app.less", "less/bootstrap.less"],
            }]
      }
    },	
    jshint: {
      files: ['Gruntfile.js', 'js/**/*.js'],
      options: {
        curly: true,
        eqeqeq: true,
        unused: true,
        globalstrict: true,
        globals: {
            angular: true,
            jQuery: true,
            console: true,
            module: true,
            document: true
        }
      }
    },
    copy: {
      images: {
        expand: true,
        src: ["img/*"],
        dest: 'dist/'
      },
      partials: {
        expand: true,
        src: ["partials/*"],
        dest: 'dist/'
      }
    },
    watch: {
      javascript: {
		files: ['js/*.js'],
		tasks: ['concat']
        },
      less: {
            files: ['less/*.less'],
            tasks: ['less:development']
      }
    }
  });
  
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');  
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    //grunt.loadNpmTasks('grunt-contrib-watch');  

    grunt.registerTask('default', ['concat', 'less:development']);
    grunt.registerTask('test', ['jshint']);
    grunt.registerTask('build', ['concat', 'uglify', 'less:production', 'copy']);
    grunt.registerTask('watcher', ['watch']);
    grunt.registerTask('heroku:development', ['concat', 'less:development']);

};
