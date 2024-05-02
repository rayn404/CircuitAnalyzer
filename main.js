let resistors = 
[[[0,0],[2,2],3],
[[2,2],[4,4],2]];
let nodes = [];
for (i=0; i<resistors.length; i++) {
    console.log(resistors[i]);
    if (!nodes.includes(resistors[i][0]) ){
        nodes.push(resistors[i][0]);
    }
    if (!nodes.includes(resistors[i][1]) ){
        nodes.push(resistors[i][1]);
    }
}


document.getElementById("net-r").textContent=(nodes);