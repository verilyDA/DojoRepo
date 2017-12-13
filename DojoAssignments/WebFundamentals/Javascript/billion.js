function myFunction(days){
  var cash = 0, penny = 0;
  for (var i = 1; i <= days; i++){
    penny = Math.pow(2, i-1);
    cash = cash + penny;
  }
  return "Total loot: " + cash/100;
}

console.log(myFunction(30));
