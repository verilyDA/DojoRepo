function myFunction(days){
  while (days > 0){
    if(days >60){
      console.log(days + " til your birthday. How unfortunate.");
    }else if(days >30){
      console.log(days + " til your birthday. It's getting closer...");
    }else if (days > 5) {
      console.log(days + " til your birthday. WOOT!");
    }else{
      console.log(days + " til your birthday. SOOOOOOOOOOO CLOSE!!!");
    }
    days--;
  }
  console.log("Happy Birthday!");
}

myFunction(79);
