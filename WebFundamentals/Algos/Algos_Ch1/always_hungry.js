function alwaysHungry(array) {
    for (var i = 0; i < array.length; i++) {
        if (array[i] === "food") {
            console.log("Yummy");
        }
    }
    console.log("I'm hungry");
}

alwaysHungry(['food', 'food', 'pie', 'food', 'empty', 1, true, false])
