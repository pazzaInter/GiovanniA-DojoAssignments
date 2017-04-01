//Return a new array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element).

function countdown(num) {
    var newArr = [];
    for (var i = num; i >= 0; i--) {
        newArr.push(i);
    }
    console.log("Your new array is:", newArr);
    console.log("Its length is:", newArr.length);
    return newArr;
}

countdown(10);
