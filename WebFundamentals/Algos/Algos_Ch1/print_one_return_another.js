//Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.

function printReturn(arr) {
    console.log(arr[arr.length-2]);
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 !== 0)
        return arr[i];
    }
}

printReturn([2,4,6,8,10,-2,3,5,2,5,67,8,4,1,0])
