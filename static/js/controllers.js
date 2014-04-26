/* Controllers */

app = angular.module('jApp.controllers', []);

app.controller('HeaderController', function($scope, $modal) {
    $scope.openAddModal = function() {
        $modal.open({
            templateUrl: '/static/partials/_add_elements.html',
            controller: AddElementsController        
        });
    }
});

app.controller('IndexController', function($scope, PagesService) {
    PagesService.getPages().success(function(data) {
        $scope.pages = data;
    });
});

app.controller('SidebarController', function($scope, ElementsService) {
    $scope.isOpen = false;
    $scope.editStart = false;

    //Prepare and emit addElement event, 
    //for the page controller, to handle
    //the element adding process
    $scope.addElement = function (elementType) {
        ElementsService.prepAddEvent(true, elementType);
    };
});

app.controller('PageController', function($rootScope, $scope, $routeParams, $location, PagesService, BulletsService, ElementsService) {

console.log("here");
    // Get total pages count for the navigation, 
    // pretty sure there is a better way 
    PagesService.getTotalPageCount().success(function(count) { 
        $rootScope.pageCount = count.page_count;
    });

    var pageNumber = parseInt($routeParams.page_number);

    //Work around, so that ng-repeat doesn't add index page twice
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

    // Toggle bullet done status and,
    // send a put request to the server,
    // to update the bullet done status
    $scope.toggleDone = function(bullet) {
        if (bullet.done) bullet.done = false;
        else bullet.done = true;

        BulletsService.updateBullet(bullet.id, bullet);
    };

    $scope.cancel = function ($event) {
        $event.preventDefault();
        ElementsService.prepAddEvent(false);
    
    };

    $scope.addElement = function () {
        var bulletName = $scope.bulletName;
  
        if (!bulletName) {
            return;
        }

        var bulletObj = {
            name: bulletName.trim(),
            type: $scope.elementType,
            page: $scope.page.id 
        }

        BulletsService.createBullet(bulletObj).success(function(newBullet) {
            $scope.bulletName = '';
            $scope.bullets.push(newBullet);
            $scope.addNewElement = false;
        });
    };

    $scope.removeElement = function (bullet) {
        console.log($scope.bullets);
        console.log($scope.bullets.indexOf(bullet));
    
        BulletsService.removeBullet(bullet.id).then(function() {
            $scope.bullets.splice($scope.bullets.indexOf(bullet), 1);
        });

    };

    $scope.editBullet = function (bullet) {
        //$scope.editStart = true;
        $scope.editedBullet = bullet;
        $scope.original = angular.extend({}, bullet);
    };

    $scope.doneEditing = function (bullet) {
        console.log(bullet);
        if (bullet.name === $scope.original.name) {
            $scope.editedBullet = null;
            return;
        }
        BulletsService.updateBullet(bullet.id, bullet).success(function(bullet) {
            $scope.editedBullet = null;
        
        });
    };

    $scope.cancelEditing = function (bullet) {
        $scope.bullets[$scope.bullets.indexOf(bullet)] = $scope.original;
        $scope.editedBullet = null;
    };

    // Listening on the addNewElement event, fired when,
    // user clicks on add elements on the sidebar
    $scope.$onRootScope('addNewElement', function() {
    console.log($scope.addNewElement);
        $scope.addNewElement = ElementsService.flag;
        $scope.elementType = ElementsService.elementType;
    });

});

var AddElementsController = function ($scope, $modal, $routeParams, $location, PagesService, BulletsService) {
    var currentPage = $routeParams.page_number;
}


