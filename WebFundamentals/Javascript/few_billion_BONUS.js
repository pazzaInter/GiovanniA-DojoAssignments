var money = .01;
for (var i = 1; i < Infinity; i++) {
    var days = i;
    var money = money * 2;
    if (money >= 10000 && money <20000) {
        console.log("It took", days, "days to make $10,000.");
    }
    if (money >= 1000000000 && money <2000000000) {
        console.log("It took", days, "days to make 1 billion dollars.");
    }
    if (money === Infinity) {
      console.log("It took", days, "days to reach infinity dollars. Share the wealth.")
      break;
    }
}
