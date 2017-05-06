//Kyle (smarter than Kenny) notes that the chance of one disaster is totally unrelated to the chance of another. Change whatHappensToday() function to create whatReallyHappensToday(). In this new function test for each disaster independently, instead of assuming exactly one disaster will happen. In other words, with this new function, all five might occur today – or none. Maybe Kenny will survive!

function whatReallyHappensToday() {
    var eventOccur = 0;
    var disasterValue = Math.floor((Math.random() * 100) + 1)
    if (disasterValue <= 10) {
        eventOccur += 1;
        console.log('Volcano erupting');
    }
    disasterValue = Math.floor((Math.random() * 100) + 1)
    if (disasterValue <= 15) {
        eventOccur += 1;
        console.log('Tsunami coming, grab your surfboards');
    }
    disasterValue = Math.floor((Math.random() * 100) + 1)
    if (disasterValue <= 20) {
        eventOccur += 1;
        console.log('Earthquake, run');
    }
    disasterValue = Math.floor((Math.random() * 100) + 1)
    if (disasterValue <= 25) {
        eventOccur += 1;
        console.log('A blizzard is pouring Dairy Queen from the sky');
    }
    disasterValue = Math.floor((Math.random() * 100) + 1)
    if (disasterValue <= 30) {
        eventOccur += 1;
        console.log('Meteor shower, grab an umbrella');
    }
    if (eventOccur === 0) {
        console.log('Your safe Kenny, nothing happened!');
    }
}

whatReallyHappensToday()
