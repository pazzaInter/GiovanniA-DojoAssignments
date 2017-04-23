//Given array of numbers, create function to replace last value with number of positive values.

function countPositives(arr) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            count += 1;
        }
    }
    arr[arr.length-1] = count;
    return arr;
}

countPositives([-1,1,1,1])
