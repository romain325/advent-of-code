const fs = require("fs");
console.log("Day2");

let depth = 0, pos = 0;

let up = (x) => { depth -= x; };
let down = (x) => {depth += x; };
let forward = (x) => { pos += x; };

let decision = {
    "up": up,
    "down": down,
    "forward": forward
};

const f = fs.readFileSync("./input1", 'utf-8');
f.split(/\r?\n/).forEach(line => {
    const val = line.split(" ");
    decision[val[0]](parseInt(val[1]));
});

console.log("Answer 1= res: d=" + depth + ", pos=" + pos + " --> " + pos*depth);

/////////////////////////////////////////////////////////////////////////////////////////

let aim = 0;
depth = pos = 0;

up = (x) => { aim -= x; };
down = (x) => { aim += x; };
forward = (x) => { 
    pos += x;
    depth += (aim*x);
};
decision = {
    "up": up,
    "down": down,
    "forward": forward
};

f.split(/\r?\n/).forEach(line => {
    const val = line.split(" ");
    decision[val[0]](parseInt(val[1]));
});

console.log("Answer 2= res: d=" + depth + ", pos=" + pos + " --> " + pos*depth);