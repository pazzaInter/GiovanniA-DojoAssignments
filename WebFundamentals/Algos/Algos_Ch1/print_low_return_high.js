//Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

function pLowRHigh(arr) {
    var min = arr[0]
    var max = arr[0]
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    console.log(min);
    return max;
}


pLowRHigh([1,2,3,7,9,0,-1,-6,9,-6,2])
