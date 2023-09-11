#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
    console.log('Missing size');
} else {
    const x = Number(process.argv[2]);
    let cnt = 0;
    while (cnt < x) {
        console.log('X'.repeat(x));
        cnt++;
    }
}