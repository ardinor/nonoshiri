'use strict';

/* Services */
angular.module('statusqueryService', ['ngResource']).
    factory('StatusUpdate', function($resource){
  return $resource('api/q/:search.json', {}, {
    query: {method:'GET', params:{search:'test'}, isArray:true}
  });
});
