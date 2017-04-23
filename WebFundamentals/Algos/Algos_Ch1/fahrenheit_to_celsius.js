// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees.

function fahrenheightToCelsius(fdegrees) {
    var celsius = (fdegrees - 32) * 5/9;
    return celsius;
}

fahrenheightToCelsius(50);
