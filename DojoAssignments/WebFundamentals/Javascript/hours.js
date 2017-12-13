function myFunction(hour, minute, period){
  var tempStr;
  if ( hour >=0 && minute >= 0 && (period === "AM" || period === "PM")){

    if (minute<30){
      tempStr = "just after";
    }
    else
    {
      tempStr = "almost";
    }

    if (period === "AM"){
      return "It's " + tempStr + " " + hour + " in the morning.";
    }
    else
    {
      return "It's " + tempStr + " " + hour + " in the evening.";
    }
  }
  else
  {
    return "What have you given me?";
  }
}

console.log(myFunction(7,45,"tuesday"));
