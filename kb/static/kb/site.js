var app = angular.module('app', ['ngAnimate']);

console.log("hi")
app.controller('AppController', ['$scope', '$http', '$q', function($scope, $http,$q) { 
  console.log("hi")
  $http.get('https://spreadsheets.google.com/feeds/list/1GY-HS0jdJD6Vsj3W7yUSjcoouYjIo90OuMS0-GQ6Qzo/1/public/values?alt=json').then(function (success){ 
    console.log(success.data);
    $scope.products = success.data.feed.entry;  console.log("Hey I worked!");
  var data = eval($scope.products);
  $scope.backorders = []
  $scope.outofstocks = []
  console.log("printing products" + $scope.products)

  for (product in $scope.products){
    console.log("Hey i'm working this loop for backorders- " + Object.values($scope.products[product].gsx$product));
    if(Object.values($scope.products[product].gsx$type) == "Backorder"){
      $scope.backorders.push($scope.products[product])
    } 
  }
  
  for (product in $scope.products){
    console.log("Hey i'm working this loop for Out of Stock- " + Object.values($scope.products[product].gsx$product));
    if(Object.values($scope.products[product].gsx$type) == "Out of Stock"){
      $scope.outofstocks.push($scope.products[product])
    } 
  }

  for(backorder in $scope.backorders){
    console.log("printing backorders - " + Object.values($scope.backorders[backorder].gsx$product))
  }
  for(oos in $scope.outofstocks){
    console.log("printing out of stocks - " + Object.values($scope.outofstocks[oos].gsx$product))
  }

  }, function(error){
    console.log("woops")
  })
 $scope.users = []
 $http.get('http://127.0.0.1:8000/medals/?format=json').then(function(success){
   console.log(success.data)
   $scope.users = success.data; console.log('logged users')
 })

}]);