function makeArray(num1, num2) {
    //if the two values passed in match
    if (num1 === num2) {
        console.log('Jinx!');
    }
    var newArr= [];
    for (var i = 0; i <num1 ; i++) {
        newArr.push(num2)
    }
    return newArr
}

makeArray(3,4);
