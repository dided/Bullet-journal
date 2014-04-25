// Declare app level module which depends on filters, and services
app = angular.module('jApp', [
  'ngResource',
  'ngRoute',
  'jApp.filters',
  'jApp.services',
  'jApp.directives',
  'jApp.controllers',
  'ui.bootstrap',
]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');    
    $interpolateProvider.endSymbol('}]}');    
});

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


