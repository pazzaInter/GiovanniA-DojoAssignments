var birthMonth = 7;
var birthDay = 9;

function guessBirthday(month, day) {
    if ((month === birthDay || month === birthMonth) &&
        (day === birthDay || day === birthMonth)) {
        console.log("How did you know?");
    }
    else {
        console.log("Just another day....");
    }
}

guessBirthday(9,7)
