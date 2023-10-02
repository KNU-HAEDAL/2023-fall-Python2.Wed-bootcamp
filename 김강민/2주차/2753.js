const year = require('fs').readFileSync('/dev/stdin');

if (year % 4 == 0) {
    if (year % 100 !== 0 || year % 400 == 0) {
        console.log('1');
    } else {
        console.log('0');
    }
} else {
    console.log('0');
}

// 이걸 왜함? ㅋ;
