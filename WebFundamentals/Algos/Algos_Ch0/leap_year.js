function leapYear(year) {
    if (year%400 === 0) {
        console.log("It's a leap year!");
    }

    else if (year%100 === 0) {
        console.log("Not a leap year.");
    }

    else if (year%4 === 0) {
        console.log("It's a leap year!");
    }

    else {
        console.log("Not a leap year.");
    }
}

leapYear(2100);
