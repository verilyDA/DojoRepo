for (var num = 10; num > 2; num = num - 1)
{
  console.log('num is currently', num);
}

var num = 1;
while (num < 5)
{
  if (num == 3)
  {
    break;
    // it stops here and breaks the loop
    // if you have additional code down here, it will never run!
  }
  console.log("I'm counting! The number is ", num);
  num = num + 1;          // if we break, we leave the WHILE loop so these lines won’t run
}

for (var num = 1; num < 5; num += 1)
{
  if (num == 3)
  {
    continue;
    // it skips this iteration and "continue"s
  }
  console.log("I'm counting! The number is ", num);
}

//for (INITIALIZATION; TEST; INCREMENT/DECREMENT)
{
  // BODY of the loop – this runs repeatedly while TEST is true
}
// INIT. [TEST?-BODY-INCREMENT] (repeatedly while TEST is true). Exit.
var glazedDonuts = [
  {
    frosting: 'glazed',
    style: 'cake',
    type: 'old fashioned',
    age: '45',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'regular',
    age: '5',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'jelly filled',
    age: '1',
    time: 'seconds'
  }
];

var numPurchase = 0;
for (var donut in glazedDonuts){
  console.log(glazedDonuts[donut].type);
  if((glazedDonuts[donut].age < 25 && glazedDonuts[donut].time == 'minutes') || glazedDonuts[donut].time == 'seconds'){
    numPurchase++;
  }
  else {
    console.log('not this donut...');
   }
}
console.log(numPurchase);
