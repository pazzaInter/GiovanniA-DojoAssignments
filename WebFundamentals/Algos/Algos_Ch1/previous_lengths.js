//You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.

function previousLengths(arr) {
    var current = 0;
    var previous = 0;
    for (var i = 0; i < arr.length; i++) {
        current = arr[i].length;
        arr[i]= previous;
        previous = current;
    }
    return arr;
}

previousLengths(['hello', 'world', 'bye', 'python', 'javascript'])
