function rightFit(arr) {
    if (arr[0] > arr.length) {
        console.log("Too big!");
    }
    else if (arr[0] < arr.length) {
        console.log("Too small!");
    }
    else if (arr[0] === arr.length) {
        console.log("Just right!");
    }
    else {
        console.log("What kind of array is this?");
    }
}
rightFit([1,2,3,4,5,6,7,8])
