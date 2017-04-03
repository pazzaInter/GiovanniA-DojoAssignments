//given (lowNum, highNum, mult), print the numbers in multiples of mult from highNum down to lowNum, using a FOR loop.

function countdown(lowNum, highNum, mult) {
    for (var i = highNum; i >= lowNum; i--) {
        if (i%mult === 0) {
            console.log(i);
        }
    }
}

countdown(2,9,3);
