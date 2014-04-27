'use strict';

var app = angular.module('jApp', [
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

app.config(function($routeProvider) {
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


;/* Controllers */

'use strict';

var app = angular.module('jApp.controllers', []);

//app.controller('HeaderController', function($scope, $modal) {
//});

app.controller('IndexController', function($scope, PagesService) {
    PagesService.getPages().success(function(data) {
        $scope.pages = data;
    });
});

app.controller('SidebarController', function($scope, ElementsService, PagesService, $location) {
    $scope.isOpen = false;

    /**
      * Prepare and emit addElement event, 
      * for the page controller, to handle
      * the element adding process
      */
    $scope.addElement = function (elementType) {
        ElementsService.prepAddEvent(true, elementType);
    };

    $scope.addPage = function () {
        var placeholderPage = {title: 'New page'};
        PagesService.createPage(placeholderPage).success(function(page){
            $location.path('page=' + page.page_number);
        });

    };
});

app.controller('PageController', function($rootScope, $scope, $routeParams, $location, PagesService, BulletsService, ElementsService) {
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
        if (bullet.done) {bullet.done = false;}
        else {bullet.done = true;}

        BulletsService.updateBullet(bullet);
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
        };

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
        if (bullet.name === $scope.original.name) {
            $scope.editedBullet = null;
            return;
        }
        BulletsService.updateBullet(bullet.id, bullet).success(function() {
            $scope.editedBullet = null;
        });
    };

    $scope.cancelEditing = function (bullet) {
        $scope.bullets[$scope.bullets.indexOf(bullet)] = $scope.original;
        $scope.editedBullet = null;
    };

    $scope.editPage = function (page) {
        $scope.editedPage = page;
        $scope.originalPage = angular.extend({}, page);
    };

    $scope.donePageEditing= function (page) {
        if (page.title === $scope.originalPage.name) {
            $scope.editedPage= null;
            return;
        }
        console.log("Pre save page: ", page);
        PagesService.updatePage(page).success(function(page) {
            console.log("Post save page: ", page);
            $scope.editedPage = null;
        });
    };

    $scope.cancelPageEditing= function () {
        $scope.page = $scope.originalPage;
        $scope.editedPage = null;
    };


    // Listening on the addNewElement event, fired when,
    // user clicks on add elements on the sidebar
    $scope.$onRootScope('addNewElement', function() {
    console.log($scope.addNewElement);
        $scope.addNewElement = ElementsService.flag;
        $scope.elementType = ElementsService.elementType;
    });
});
;/* Directives */
'use strict';

var appDirectives = angular.module('jApp.directives', []);

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
;'use strict';

angular.module('jApp.filters', []).
  filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    };
  }]);
;/* Services */
'use strict';

var appServices = angular.module('jApp.services', []);

appServices.factory('PagesService', function($http) {
    return {
        getPageBullets: function(queryParam, queryValue) {
            var bullets = $http.get("/api/bullets?" + queryParam + "=" + queryValue);
            return bullets;
        },
        getPage: function(id) {
            var page = $http.get("/api/pages/" + id);
            return page;
        },
        getPageByPageNumber: function(pageNumber) {
            var page = $http.get("/api/pages?page_number=" + pageNumber);
            return page;
        },
        getPages: function() {
            var pages = $http.get('/api/pages');
            return pages;
        },
        getTotalPageCount: function() {
            var count = $http.get('/api/count');
            return count;
        },
        createPage: function(pageObj) {
            var page = $http.post('/api/pages', pageObj);
            return page;
        },
        updatePage: function(pageObj) {
            var page = $http.put('/api/pages/' + pageObj.id, pageObj);
            return page;
        }
    }; 
});

appServices.factory('BulletsService', function($http) {
    return {
        createBullet: function(bulletObj) {
            var bullet = $http.post('/api/bullets', bulletObj); 
            return bullet;
        },
        updateBullet: function(bulletObj) {
            var bullet = $http.put('/api/bullets/' + bulletObj.id, bulletObj);
            return bullet;
        },
        removeBullet: function(bulletId) {
            var bullet = $http.delete('/api/bullets/' + bulletId);
            return bullet;
        },
    };
});

// Service for broadcasting the add element event from the sidebar
appServices.factory('ElementsService', function($rootScope){
    this.flag = false;
    this.elementType = '';
    return {
        prepAddEvent: function (flag, elementType) {
            this.elementType = elementType;
            this.flag = flag;
            this.emitAddEvent();
        },
        emitAddEvent: function () {
            $rootScope.$emit('addNewElement');
        }
    };
});


