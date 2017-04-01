//Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) that one.

function finalCountdown(param1, param2, param3, param4) {
    var i = param2;
    while (i<=param3) {
        if (i%param1 === 0 && i!==param4) {
            console.log(i);
        }
        i++;
    }
}

finalCountdown(3,5,17,9);
