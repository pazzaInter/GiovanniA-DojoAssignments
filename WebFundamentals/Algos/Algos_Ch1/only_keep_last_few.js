//Stan learned something today: that reducing an array’s .length immediately shortens it by that amount. Given array arr and number X, remove all except the last X elements, and return arr (changed and shorter). Given ([2,4,6,8,10],3), change the given array to [6,8,10] and return it.

function lastFew(array, x) {
    return array.slice(-x)
}

lastFew([2,4,6,8,10],3);


// method 2

function lastFew2(array, x) {
    var newArray =[];
    for (var i = array.length-x; i < array.length; i++) {
        newArray.push(array[i]);
    }
    return newArray
}

lastFew2([2,4,6,8,10],3);
