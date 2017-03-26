//the number of days until birthday
var daysUntilMyBirthday = 60;

//print sad, excited, celebration messge depending on days until birthday
function birthdayCountdown(days) {
    var until_message = days + " days until my birthday.";
    if (days>30) {
        return console.log(until_message, "Such a long time until I get presents.");
    }
    else if (days > 5) {
        return console.log(until_message, "I wonder if I will get that new Metal Gear Solid game.");
    }
    else if (days < 5 && days >0) {
        return console.log(until_message.toUpperCase(), "!!!!!!!!");
    }
    else if (days === 0) {
        return console.log("Thank you everyone for being here. Lets eat and drink!!!!!");
    }
    //This will catch any other value than those checked above.
    else {
        return console.log("Who cares about birthdays anyways.");
    }
}

birthdayCountdown(daysUntilMyBirthday);
