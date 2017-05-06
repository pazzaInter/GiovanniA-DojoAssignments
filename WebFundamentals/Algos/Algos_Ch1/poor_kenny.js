//Kenny tries to stay safe, but somehow everyday something happens. If there is a 10% chance of volcano, 15% chance of tsunami, 20% chance of earthquake, 25% chance of blizzard, and 30% chance of meteor strike, write function whatHappensToday() to print the outcome.

function whatHappensToday() {
    var disasterValue = Math.floor((Math.random() * 100) + 1)
    if (disasterValue <= 10) {
        console.log('Volcano erupting');
    }
    else if (disasterValue <= 25) {
        console.log('Tsunami coming, grab your surfboards');
    }
    else if (disasterValue <= 45) {
        console.log('Earthquake, run');
    }
    else if (disasterValue <= 70) {
        console.log('A blizzard is pouring Dairy Queen from the sky');
    }
    else if (disasterValue <= 100) {
        console.log('Meteor shower, grab an umbrella');
    }
}

whatHappensToday()
