/* Controllers */

app = angular.module('jApp.controllers', []);

app.controller('HeaderController', function($scope) {
    $scope.message ='hello';
});

app.controller('SideBarController', function($scope) {
    $scope.message ='hello';
});

app.controller('IndexController', function($scope, PagesService) {
    PagesService.getPages().success(function(data) {
        $scope.pages = data;
    });
});

app.controller('PageController', function($rootScope, $scope, $routeParams, $location, PagesService) {
    PagesService.getTotalPageCount().success(function(count) {
        $rootScope.pageCount = count.page_count;
    
    });
    var pageNumber = parseInt($routeParams.page_number);
    if (pageNumber === 1) {
        $location.path('/');
        return;
    }
    PagesService.getPageBullets('page', pageNumber).success(function(bullets) {
        $scope.bullets = bullets;
        PagesService.getPageByPageNumber(pageNumber).success(function(page) {
            $scope.page = page[0];
            $scope.firstPage = function() {
                $location.path('page=1');
            };
            $scope.lastPage = function() {
                $location.path('page=' + $rootScope.pageCount);
            };
            $scope.nextPage = function() {
                if ($rootScope.pageCount <= pageNumber){
                    $location.path('/');
                    return;
                }
                var nextPage = pageNumber + 1; 
                $location.path('page=' + nextPage);
            };
            $scope.prevPage = function() {
                var prevPage = pageNumber - 1; 
                $location.path('page=' + prevPage);
            };
        });
    });

});

