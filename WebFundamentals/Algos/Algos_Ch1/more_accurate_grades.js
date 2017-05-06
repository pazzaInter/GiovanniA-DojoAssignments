//For an additional challenge, add ‘-’ signs to scores in the bottom two percent of A, B, C and D scores, and “ +” signs to the top two percent of B, C and D scores (sorry, Mr. Cerise never gives an A+).

//Example: Given 88, console.log "Score: 88. Grade: B+". Given 61, log "Score: 61. Grade: D-".

function accurateGrades(score) {
    var grade;
    var sign = ''
    // Check if score is in top/bottom 2 percent
    if (score % 10 > 7) {
        sign = '+'
    }
    else if (score % 10 < 3) {
        sign = '-'
    }
    if (score >= 90) {
        grade = "A";
    }
    else if (score >= 80) {
        grade = "B";
    }
    else if (score >= 70) {
        grade = "C";
    }

    else if (score >= 60) {
        grade = "D";
    }
    else if (score < 60) {
        grade = "F";
    }
    console.log("Score:", score + ".", "Grade:", grade + sign + ".");
}

accurateGrades(80);
