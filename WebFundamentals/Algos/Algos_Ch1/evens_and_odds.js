//Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"

function evensOdds(arr) {
    //keep track consecutive odds
    var countOdd = 0;
    //keep track consecutive evens
    var countEven = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 !== 0) {
            //if odd then reset even counter and add to odd
            countOdd += 1;
            countEven = 0;
            if (countOdd === 3) {
                //if the count is 3 then we reset counter and print message
                countOdd = 0;
                console.log("That's odd!");
            }
        }
        if (arr[i] % 2 === 0) {
            //if even then reset odd counter and add to even
            countEven += 1;
            countOdd = 0;
            if (countEven === 3) {
                //if the count is 3 then we reset counter and print message
                countEven = 0;
                console.log('Even more so!');
            }
        }
    }
}

evensOdds([2,4,6,2,7,1,5,6,6,5,5,5,5,5,7,8,8,4]);

//alternative that will print message mulitple times for larger groups, no reset after 3 consecutive

function evensOdds2(array){
  for (var i = 0; i < array.length - 2; i++){
    if (array[i] % 2 !== 0 && array[i + 1] % 2 !== 0 && array[i + 2] % 2 !== 0){
        console.log("That's odd!");
    }
    if (array[i] % 2 === 0 && array[i + 1] % 2 === 0 && array[i + 2] % 2 === 0){
        console.log("Even more so!");
    }
  }
}

evensOdds2([2,4,6,2,7,1,5,6,6,5,5,5,5,5,7,8,8,4]);
