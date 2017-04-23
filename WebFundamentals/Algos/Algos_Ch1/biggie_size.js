//Given an array, write a function that changes all positive numbers in the array to “big”.

function makeItBig(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            arr[i] = 'big'
        }
    }
    return arr
}

makeItBig([-1,3,5,-5]) 
