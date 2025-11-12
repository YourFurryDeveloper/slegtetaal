import time

import storage


RESET = "\033[0m"
ansiEffects = [
    "\033[0m" # Reset/none
    "\033[1m",   # Bold
    "\033[2m",   # Dim
    "\033[3m",   # Italic
    "\033[4m",   # Underline
    "\033[5m",   # Blink (slow)
    "\033[6m",   # Blink (rapid)
    "\033[7m",   # Invert / Reverse
    "\033[8m",   # Hidden
    "\033[9m",   # Strikethrough

    # Text colors (foreground)
    "\033[30m",  # Black
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m",  # White
    "\033[90m",  # Bright Black (Gray)
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m",  # Bright Cyan
    "\033[97m",  # Bright White

    # Background colors
    "\033[40m",  # Background Black
    "\033[41m",  # Background Red
    "\033[42m",  # Background Green
    "\033[43m",  # Background Yellow
    "\033[44m",  # Background Blue
    "\033[45m",  # Background Magenta
    "\033[46m",  # Background Cyan
    "\033[47m",  # Background White
    "\033[100m", # Bright Background Black (Gray)
    "\033[101m", # Bright Background Red
    "\033[102m", # Bright Background Green
    "\033[103m", # Bright Background Yellow
    "\033[104m", # Bright Background Blue
    "\033[105m", # Bright Background Magenta
    "\033[106m", # Bright Background Cyan
    "\033[107m"  # Bright Background White
]

def checkLine(line):
    if "gt" in line:
        gtLine = int(line.split()[1]) - 1
        storage.curLine = gtLine
        checkLine(storage.codebuffer[gtLine])

    if "prnt" in line:
        txtEffect = int(line.split()[1])
        txtToPrint = line.split()[2:]
        if "[rmem]" in txtToPrint:
            txtToPrint = ' '.join(str(x) for x in txtToPrint)
            txtToPrint = txtToPrint.replace("[rmem]", storage.membuffer[storage.mempos])
        else:
            txtToPrint = ' '.join(str(x) for x in txtToPrint)

        print(f"{ansiEffects[txtEffect]}{txtToPrint}{RESET}")

    if "wait" in line:
        waitS = float(line.split()[1])
        time.sleep(waitS)

    if "memop" in line:
        memOperation = line.split()[1]
        for op in memOperation:
            if op == "<":
                storage.mempos -= 1
                if not storage.mempos - 1 in storage.membuffer:
                    storage.membuffer[storage.mempos - 1] = 0
            elif op == ">":
                storage.mempos += 1
                if not storage.mempos + 1 in storage.membuffer:
                    storage.membuffer[storage.mempos + 1] = 0

    if "setmem" in line:
        valueToSet = line.split()[1:]
        valueToSet = ' '.join(str(x) for x in valueToSet)
        storage.membuffer[storage.mempos] = valueToSet