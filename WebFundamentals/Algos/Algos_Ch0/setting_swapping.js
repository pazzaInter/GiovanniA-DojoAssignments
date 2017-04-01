var myNumber = 42;
var myName = "Giovanni";

function swapper(item1, item2) {
    var temp = item1;
    myNumber = item2;
    myName = temp;
}
swapper(myNumber, myName);

console.log(myNumber, myName);
