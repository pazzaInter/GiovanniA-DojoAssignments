// Create ThreesFives() that adds values from 100 and 4000000 (inclusive) if that value is evenly divisible by 3 or 5 but not both. Display the final sum in the console.

function ThreesFives(start, end) {
    var sum = 0;
    for (var i = 100; i <= 4000000; i++) {
        if (i % 3 === 0) {
            if (i % 5 !== 0) {
                sum += i;
            }
        }
        if (i % 5 === 0) {
            if (i % 3 !== 0) {
                sum += i;
            }
        }
    }
    return sum;
}

ThreesFives();

// Create BetterThreesFives(start,end) that allows you to enter arbitrary start and end values for your range.

function BetterThreesFives(start, end) {
    var sum = 0;
    for (var i = start; i <= end; i++) {
        if (i % 3 === 0) {
            if (i % 5 !== 0) {
                sum+= i;
            }
        }
        if (i % 5 === 0) {
            if (i % 3 !== 0) {
                sum+= i;
            }
        }
    }
    return sum;
}

BetterThreesFives(5, 100);
