function slots(maxCoins, minCoins, maxPlays){
  var coins = Math.trunc(Math.random() * (maxCoins - minCoins) + minCoins);
  while (coins > 0){
    if(maxPlays < 0){
      break;
    }
    maxPlays--;
    if (Math.random() * (700 - 1) + 1 >= 350){
      coins--;
      console.log("You lost and now have " + coins + " coins left");
    }else{
      var winnings = Math.trunc(Math.random() * (200 - 1) + 1);
      coins += winnings;
      console.log("You won " + winnings + " coins! Congrats! You know have " + coins + " coins!");
    }
  }
}

slots(20, 4, 50);
