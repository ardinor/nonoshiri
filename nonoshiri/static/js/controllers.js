'use strict';

/* Controllers */
function StatusQueryCtrl($scope, StatusUpdate, $timeout) {
  $scope.statuses = [];
  $scope.statuses = StatusUpdate.query();
  $scope.onTimeout = function() {
    var newStatuses = StatusUpdate.query();
    for(var i=0;i<newStatuses.length;i++)
    {
        $scope.statuses.push(newStatuses[i])
    }
    //$scope.statuses = StatusUpdate.query();
    //$scope.statuses.concat(StatusUpdate.query());
    updatetimeout = $timeout($scope.onTimeout, 5000);
  }
  var updatetimeout = $timeout($scope.onTimeout, 5000);
}