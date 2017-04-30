function negativeOutlook(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            arr[i] = arr[i] * -1;
        }
    }
    return arr;
}

negativeOutlook([1,-3,5])
