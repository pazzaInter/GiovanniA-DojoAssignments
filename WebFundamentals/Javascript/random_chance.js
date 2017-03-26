//this function will start a new game for a slot machine
function newGame(coins) {
    //the following two variables will determine the target to hit and its rewards
    var winningNumer = Math.trunc(Math.random()*100) + 1;
    var winnings = Math.trunc(Math.random()*50) + 50;
    console.log(winnings);
    //as long as the player has coins the following loop will run
    while (coins > 0) {
        console.log(coins);
        var gameResult = Math.trunc(Math.random()*100) + 1
        if (gameResult === winningNumer) {
            //gotta pay to play
            coins-=1;
            //total of winnings and whatever coins were left
            return winnings + coins;
        }
        else {
            //didn't win so player looses mula
            coins-=1;
        }
    }
    return 0;
}

newGame(100);
