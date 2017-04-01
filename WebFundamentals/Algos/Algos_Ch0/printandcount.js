function multiplesFive() {
    var counter = 0;
    for (var i = 512; i <= 4096; i++) {
        if (i%5 === 0) {
            counter ++;
            console.log(i);
        }
    }
    return counter;
}

multiplesFive();
