function greaterThanSecond(arr) {
    var newArr = [];
    var counter = 0;
    if (arr.length>1) {
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] > arr[1]) {
                newArr.push(arr[i])
                counter ++;
            }
        }
    }
    else {
        console.log("Need to enter an array bigger than 1.");
        return arr;
    }
    console.log("Number of values that were greater than second value in original array:",counter);
    return newArr;
}

greaterThanSecond([8,3,4,5]);
