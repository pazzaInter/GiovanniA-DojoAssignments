//this function will print out the values in a list along with their index.
function fancyArray(arr, symbol, direction) {
    //if the direction is true then the print order will be reversed
    if (direction === true) {
        for (var i = arr.length - 1; i >= 0; i--) {
            console.log(i + symbol + arr[i]);
        }
    }
    else {
        for (var i = 0; i < arr.length; i++) {
            console.log(i + symbol + arr[i]);
      }
    }
}

//prompt to the user about which symbol they prefer to print between index and value
var choice = prompt("Enter number to choose symbol: 1->,2=>,3::,4-----");

//declaring symbol to undefined for now, this will be set later
var symbol;

//this will set the symbol to print according to the value of choice (1-4)
if (choice === "1") {
    symbol = "->"
}
else if (choice === "2") {
    symbol = "=>"
}
else if (choice === "3") {
    symbol = "::"
}
else if (choice === "4") {
    symbol = "------"
}
else {
    //default will be blank
    symbol = " "
}
fancyArray(["James", "Jill", "Jane", "Jack"], symbol, true)
