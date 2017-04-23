//Create celsiusToFahrenheit(cDegrees) that accepts the number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.

function celsiusToFahrenheit(cDegrees) {
    var fahrenheit = (9/5 * cDegrees) + 32;
    return fahrenheit;
}

celsiusToFahrenheit(50);

//(optional) Do Fahrenheit and Celsius values equate at a certain number? The scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.

function equalTo() {
    var equalAt;
    for (var i = 200; i <=200; i--) {
        var celsius = (i - 32) * 5/9;
        var fahrenheit = (9/5 * i) + 32;
        if (celsius === fahrenheit) {
            equalAt = i;
            console.log('Fahrenheit and Celsius meet at', equalAt)
            return equalAt
        }
    }
    console.log('They did not meet at any of the given values checked.')
}

equalTo()
