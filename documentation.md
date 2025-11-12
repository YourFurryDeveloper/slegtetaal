# SLEGTETAAL DOCUMENTATION
<br>

## Code definitions

### Memory operations
`memop {operation}` Performs a virtual memory operation.
<br>
`<` moves the virtual memory index pointer position back by one, `>` moves it forward by one.
<br>
There can be as many memory operations as you please in one memop command.

`setmem {value}` Sets the value at the currently selected virtual memory location. Can be an int, float, or str.

`[rmem]` Retrieves the value at the currently selected virtual memory location.
<br>
Example: `prnt 0 Current memory location value: rmem`

### Standard functions

`prnt {value}` Prints any specified value to the terminal

`gt {line}` Goes to and executes a specified line in the code.

`[` Starts a loop; `]` Marks the end of it.