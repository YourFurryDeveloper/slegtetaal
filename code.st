setmem Mem1
memop >
setmem Hello world!
memop <

prnt 0 Current vmem value at position [rmem]: [rmem]
memop >
prnt 0 Current vmem value at position 1: [rmem]

wait 0.5
gt 6