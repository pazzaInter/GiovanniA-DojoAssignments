var money = .01;
for (var i = 1; i < Infinity; i++) {
    var days = i;
    var money = money * 2;
    if (days ===30) {
        console.log("After 30 days the servant received", money, "dollars.");
        break;
    }
}
