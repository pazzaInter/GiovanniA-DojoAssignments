var world = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,2],
    [2,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,2],
    [2,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2],
    [2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2],
    [2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,1,1,1,3,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,1,1,1,2,2,2,2,2,1,1,1,2],
    [2,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,2],
    [2,1,1,1,2,1,1,1,1,1,1,1,2,2,1,1,2],
    [2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,2],
    [2,1,1,1,1,1,2,2,2,2,2,1,1,2,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
]
var pacman = {
    'x' : 1,
    'y' : 1,
    'direction' : 1,
    'degrees': 0,
}
var pacman2 = {
    'x' : 15,
    'y' : 1,
    'direction' : 1,
    'degrees': 180,
}
var ghost = {
    'x' : 6,
    'y' : 6,
    'direction': 1,
}
var score = 0;
var score2 = 0;
var keyPressed = {
    'uparrow': false,
    'downarrow': false,
    'leftarrow': false,
    'rightarrow': false,
    'w': false,
    's': false,
    'a': false,
    'd': false,
}
function displayWorld() {
    var output = '';

    for (var i = 0; i < world.length; i++) {
        output += "\n<div class='row'>\n";
        for (var j = 0; j < world[i].length; j++) {
            if (world[i][j]===2) {
                output += "<div class='brick'></div>";
            }
            else if (world[i][j] === 1) {
                output += "<div class='coin'></div>";
            }
            else if (world[i][j] === 0) {
                output += "<div class='empty'></div>";
            }
            else if (world[i][j] === 3) {
                output += "<div class='cherry'></div>";
            }
            // else if (world[i][j] === 4) {
            //     output += "<div class='ghost'></div>";
            // }
        }
        output += "\n</div>";
    }
    document.getElementById('world').innerHTML = output;
    // console.log(document.getElementById('world').innerHTML);
}
function displayPacman() {
    // position and direction of player 1
    document.getElementById('pacman').style.left = pacman['x'] * 20 + 'px';
    document.getElementById('pacman').style.top = pacman['y'] * 20 + 'px';
    document.getElementById('pacman').style.transform = 'rotate('+ pacman['degrees'] + 'deg)';
}
function displayPacman2() {
    // position and direction of player 2
    document.getElementById('pacman2').style.left = pacman2['x'] * 20 + 'px';
    document.getElementById('pacman2').style.top = pacman2['y'] * 20 + 'px';
    document.getElementById('pacman2').style.transform = 'rotate('+ pacman2['degrees'] + 'deg)';
}
function displayGhost() {
    // position of ghost
    document.getElementById('ghost').style.left = ghost['x'] * 20 + 'px';
    document.getElementById('ghost').style.top = ghost['y'] * 20 + 'px';
    // document.getElementById('ghost').style.transform = 'rotate('+ ghost['degrees'] + 'deg)';
}
function displayScore() {
    document.getElementById('score').innerHTML = 'P1 score: '+ score;
    document.getElementById('score2').innerHTML = 'P2 score: '+ score2;
}

document.onkeydown = function movePacman(e) {
    // the following is to account for multiple key presses, any key pressed will be logged as true in dicionary until let go
    if (e['keyCode'] === 37) {
        keyPressed['leftarrow']= true;
    }
    else if (e['keyCode'] === 38) {
        keyPressed['uparrow']= true;
    }
    else if (e['keyCode'] === 39) {
        keyPressed['rightarrow']= true;
    }
    else if (e['keyCode'] === 40) {
        keyPressed['downarrow']= true;
    }
    else if (e['keyCode'] === 65) {
        keyPressed['a']= true;
    }
    else if (e['keyCode'] === 87) {
        keyPressed['w']= true;
    }
    else if (e['keyCode'] === 68) {
        keyPressed['d']= true;
    }
    else if (e['keyCode'] === 83) {
        keyPressed['s']= true;
    }

    // player 1
    // left arrow is pressed
    if (keyPressed['leftarrow'] && world[pacman['y']][pacman['x']-1] !== 2) {
        pacman['degrees']= 180;
        pacman['x'] --
    }
    // up arrow is pressed
    else if (keyPressed['uparrow'] && world[pacman['y']-1][pacman['x']] !== 2) {
        pacman['degrees']= 270;
        pacman['y'] --
    }
    // right arrow is pressed
    else if (keyPressed['rightarrow'] && world[pacman['y']][pacman['x']+1] !== 2) {
        pacman['degrees']= 0;
        pacman['x'] ++
    }
    // down arrow is pressed
    else if (keyPressed['downarrow'] && world[pacman['y']+1][pacman['x']] !== 2) {
        pacman['degrees']= 90;
        pacman['y'] ++
    }
    // if pacman runs into ghost location then reset pacman
    if (pacman['y'] === ghost['y'] && pacman['x'] === ghost['x']) {
        pacman['x'] = 1;
        pacman['y'] = 1;
    }
    // points for eating a coin
    if (world[pacman['y']][pacman['x']] === 1) {
        world[pacman['y']][pacman['x']] = 0;
        score += 10;
    }
    // points for eating a cherry
    if (world[pacman['y']][pacman['x']] === 3) {
        world[pacman['y']][pacman['x']] = 0;
        score += 50;
    }

    // player 2
    // a is pressed left
    if (keyPressed['a'] && world[pacman2['y']][pacman2['x']-1] !== 2) {
        pacman2['degrees']= 180;
        pacman2['x'] --
    }
    // w is pressed for up
    else if (keyPressed['w'] && world[pacman2['y']-1][pacman2['x']] !== 2) {
        pacman2['degrees']= 270;
        pacman2['y'] --
    }
    // d is pressed for right
    else if (keyPressed['d'] && world[pacman2['y']][pacman2['x']+1] !== 2) {
        pacman2['degrees']= 0;
        pacman2['x'] ++
    }
    // s is pressed for down
    else if (keyPressed['s'] && world[pacman2['y']+1][pacman2['x']] !== 2) {
        pacman2['degrees']= 90;
        pacman2['y'] ++
    }

    // if pacman runs into ghost location then reset pacman
    if (pacman2['y'] === ghost['y'] && pacman2['x'] === ghost['x']) {
        pacman2['x'] = 15;
        pacman2['y'] = 1;
    }
    // points for eating a coin
    if (world[pacman2['y']][pacman2['x']] === 1) {
        world[pacman2['y']][pacman2['x']] = 0;
        score2 += 10;
    }
    // points for eating a cherry
    if (world[pacman2['y']][pacman2['x']] === 3) {
        world[pacman2['y']][pacman2['x']] = 0;
        score2 += 50;
    }

    displayWorld();
    displayPacman();
    displayPacman2();
    displayScore();
}
document.onkeyup = function (e) {
    // once a key is released then its key will be marked as false
    if (e['keyCode'] === 37) {
        keyPressed['leftarrow']= false;
    }
    else if (e['keyCode'] === 38) {
        keyPressed['uparrow']= false;
    }
    else if (e['keyCode'] === 39) {
        keyPressed['rightarrow']= false;
    }
    else if (e['keyCode'] === 40) {
        keyPressed['downarrow']= false;
    }
    else if (e['keyCode'] === 65) {
        keyPressed['a']= false;
    }
    else if (e['keyCode'] === 87) {
        keyPressed['w']= false;
    }
    else if (e['keyCode'] === 68) {
        keyPressed['d']= false;
    }
    else if (e['keyCode'] === 83) {
        keyPressed['s']= false;
    }
}

function moveGhost() {

    // if none of the next moves in horizontal position would hit a wall, then proceed with changing x coordinate
    if (world[ghost['y']][ghost['x']-1] !== 2 || world[ghost['y']][ghost['x']+1] !== 2) {
        ghost['x'] += ghost['direction'];
    }
    else if (world[ghost['y']-1][ghost['x']] !== 2 || world[ghost['y']+1][ghost['x']] !== 2) {
        ghost['y'] += ghost['direction'];
    }

    // change direction of ghost if next move would hit a wall
    if (world[ghost['y']][ghost['x']-1] === 2) {
        ghost['direction'] = 1;
    }
    if (world[ghost['y']][ghost['x']+1] === 2) {
        ghost['direction'] = -1;
    }
    if (world[ghost['y']-1][ghost['x']] === 2) {
        ghost['direction'] = 1;
    }
    if (world[ghost['y']+1][ghost['x']] === 2) {
        ghost['direction'] = -1;
    }
    //if ghost were to run into a pacman, then have the pacman reset
    if (ghost['y'] === pacman['y'] && ghost['x'] === pacman['x']) {
        pacman['x'] = 1;
        pacman['y'] = 1;
        displayPacman();
    }
    if (ghost['y'] === pacman2['y'] && ghost['x'] === pacman2['x']) {
        pacman2['x'] = 15;
        pacman2['y'] = 1;
        displayPacman2();
    }
    displayGhost();
}
displayWorld();
displayGhost();
setInterval(function(){ moveGhost() }, 500);
