function addSeven(arr) {
    var newArr = [];
    // start at 2nd item so we skip adding the first
    for (var i = 1; i < arr.length; i++) {
        if (arr[i]/1 === arr[i]) {
            newArr.push(arr[i]+7);
        }
    }
    return newArr;
}

addSeven([1, 2, 3, 4, 5, 'tree', '7', 9])
