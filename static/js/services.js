/* Services */
appServices = angular.module('jApp.services', []);

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
            var count = $http.get('/api/count')
            return count;
        }
    } 
});

appServices.factory('BulletsService', function($http) {
    return {
        updateBullet: function(bulletId, data) {
            var bullet = $http.put('/api/bullets/' + bulletId, data);
            return bullet;
        }
    }
});

// Service for broadcasting the add element event from the sidebar
appServices.factory('ElementsService', function($rootScope){
    var flag = false;
    var elementType = '';
    return {
        prepAddEvent: function (flag, elementType) {
            this.elementType = elementType;
            this.flag = flag;
            this.emitAddEvent();
        },
        emitAddEvent: function () {
            $rootScope.$emit('addNewElement');
        }
    }
});


