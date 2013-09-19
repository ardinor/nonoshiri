'use strict';

/* Controllers */
function StatusQueryCtrl($scope, StatusUpdate, $timeout) {
  $scope.statuses = [];
  //$scope.statuses = StatusUpdate.query();
  //console.log($scope.statuses);
  $scope.onTimeout = function() {
    /*
    var newStatuses = StatusUpdate.query();
    console.log(newStatuses);
    for(var i=0;i<newStatuses.length;i++)
    {
        //console.log(newStatuses[i]);
        $scope.statuses.push(newStatuses[i]);
    } */
    var newStatuses = StatusUpdate.query( function(stat) {
      $scope.statuses.push(stat);
    });


    //$scope.statuses = StatusUpdate.query();  // this works but just replaces the list
    //$scope.statuses.concat(StatusUpdate.query());
    updatetimeout = $timeout($scope.onTimeout, 5000);
  };
  var updatetimeout = $timeout($scope.onTimeout, 5000);
}