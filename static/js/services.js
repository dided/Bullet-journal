/* Services */
appFac = angular.module('jApp.services', []);


appFac.factory('PagesService', function($http) {
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

appFac.factory('BulletsService', function($http) {
    return {
        updateBullet: function(bulletId, data) {
            var bullet = $http.put('/api/bullets/' + bulletId, data);
            return bullet;
        }
    }
});


