import defs
import storage

with open("code.st", "r") as slegtetaalRaw:
    code = slegtetaalRaw.readlines()

    # Load code into the buffer/cache for the goto functions
    for line in code:
        storage.codebuffer.append(line.strip())
        #print(codebuffer)

    # Start interpreting
    def intLoop():
        for line in storage.codebuffer[storage.curLine:]:
            #if not storage.curLine == storage.lastLine:
                #intLoop()
                #print("oh")
                
            storage.curLine += 1
            defs.checkLine(str(line))
            storage.lastLine += 1

    intLoop()