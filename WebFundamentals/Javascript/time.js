var HOUR = 7;
var MINUTE = 15;
var PERIOD = "PM";

function whatTime(hr,min,pr) {
    var currentTime;
    if (pr === "AM") {
        if (min > 30) {
            currentTime = console.log("It's almost", hr + 1, "in the morning");
        }
        else if (min < 30) {
            currentTime = console.log("It's just after", hr, "in the morning");
        }
    }
    else {
        if (min > 30) {
            currentTime = console.log("It's almost", hr +1, "in the evening");
        }
        else if (min < 30) {
            currentTime = console.log("It's just after", hr, "in the evening");
        }
    }
    return currentTime;
}

whatTime(HOUR,MINUTE,PERIOD);
