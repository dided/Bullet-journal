/* Directives */

appDirectives = angular.module('jApp.directives', []);

//Directive to auto foucs inputs
appDirectives.directive('focusOn', function($timeout, $parse){
    return {
        link: function($scope, element, attrs) {
            var model = $parse(attrs.focusOn);
            $scope.$watch(model, function(value) {
                if (value) {
                    $timeout(function() {
                        element[0].focus();
                    });
                }
            });
        }
    };
});
