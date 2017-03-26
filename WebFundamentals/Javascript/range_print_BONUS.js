function printRange(a,b,c) {
    //a = start point
    //b = end point
    //c = skip amount
    if (c === undefined) {
        c = 1;
    }
    if (b === undefined) {
        b = a;
        a = 0;
    }
    for (var i = a; i < b; i+=c) {
        console.log(i);
    }
}
printRange(2, 10);
