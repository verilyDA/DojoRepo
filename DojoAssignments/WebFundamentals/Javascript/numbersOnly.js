function myFunction(arr){
  var array = [];
  for (var i = 0; i < arr.length; i++){
    if(typeof arr[i] === "number"){
      array.push(arr[i]);
    }
  }
  return array;
}

console.log(myFunction([1, "tim", 5, "sally", true, 0]));
