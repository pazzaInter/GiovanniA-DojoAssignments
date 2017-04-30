function scaleArray(array, num) {
    for (var i = 0; i < array.length; i++) {
        array[i] = array[i] * num;
    }
    return array;
}

scaleArray([1,2,3,4,5,6], 5)
