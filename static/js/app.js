// Declare app level module which depends on filters, and services
app = angular.module('jApp', [
  'ngResource',
  'ngRoute',
  'jApp.filters',
  'jApp.services',
  'jApp.directives',
  'jApp.controllers',
  'ui.bootstrap',
  'ui.utils',
]);

app.config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{[{');    
    $interpolateProvider.endSymbol('}]}');    

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});

app.config(['$provide', function($provide){
    $provide.decorator('$rootScope', ['$delegate', function($delegate){

        Object.defineProperty($delegate.constructor.prototype, '$onRootScope', {
            value: function(name, listener){
                var unsubscribe = $delegate.$on(name, listener);
                this.$on('$destroy', unsubscribe);
            },
            enumerable: false
        });

        return $delegate;
    }]);
}]);

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/partials/_index_page.html',
            controller: 'IndexController'
        })
        .when('/page=:page_number', {
            templateUrl: '/static/partials/_page.html',
            controller: 'PageController'
        })
        .otherwise({ redirectTo: '/' });
});


