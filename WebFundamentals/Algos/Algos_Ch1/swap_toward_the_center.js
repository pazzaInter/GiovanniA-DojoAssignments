function swapTowardCenter(array) {
    for (var i = 0; i < array.length/2; i+=2) {
        var temp = array[i];
        array[i] = array[array.length - i -1];
        array[array.length - i -1] = temp;
    }
  return array;
}

//swapTowardCenter([true,42,"Ada",2,"pizza"])
//swapTowardCenter([1,2,3,4,5,6])
