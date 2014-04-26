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
        },
        createPage: function(page) {
            var page = $http.post('/api/pages', page);
            return page;
        },
        updatePage: function(page) {
            console.log(page);
            var page = $http.put('/api/pages/' + page.id, page);
            return page;
        }
    } 
});

appServices.factory('BulletsService', function($http) {
    return {
        createBullet: function(bulletObj) {
            var bullet = $http.post('/api/bullets', bulletObj); 
            return bullet;
        },
        updateBullet: function(bullet) {
            var bullet = $http.put('/api/bullets/' + bullet.id, bullet);
            return bullet;
        },
        removeBullet: function(bulletId) {
            var bullet = $http.delete('/api/bullets/' + bulletId);
            return bullet;
        },
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


