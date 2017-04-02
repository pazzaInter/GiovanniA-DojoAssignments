// given an array this will print the sum of its first value and the length of the arry. This will search for the first number in the array before summing.

function firstPlus(arr) {
    var i = 0;
    while (isNaN(arr[i])=== true || arr[i] === false) {
        i++;
    }
    var sum = arr[i] + arr.length;
    return sum;
}

var arr= [false,'true', 'Hello', 7, 2, 5, 6];

firstPlus(arr);
