//Given an array of numbers arr, add 1 to every second element, specifically those whose index is odd (arr[1], [3], [5], etc). Afterward, console.log each array value and return arr.

function incrementSeconds(arr) {
    for (var i = 1; i < arr.length; i+=2) {
        arr[i] += 1;
    }
    console.log(arr);
    return arr;
}

incrementSeconds([1,1,3,3,5,5,7,7,9,0])
