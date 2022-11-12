import re
import copy

result = []
text = input("")

#gajah
tempGajah = copy.deepcopy(text)
newGajahStart = 0
gajahCheck = True

while(gajahCheck):
    gajahMatch = re.search(r'(S|s)ang gajah', tempGajah)
    if(gajahMatch):
        tempGajah = tempGajah[gajahMatch.end():]
        result.append(("g", gajahMatch.start()+newGajahStart))
        newGajahStart = gajahMatch.end()
    else:
        gajahCheck = False

#serigala
tempSerigala = copy.deepcopy(text)
newSerigalaStart = 0
serigalaCheck = True

while(serigalaCheck):
    appendBool = True
    serigalaMatch = re.search(r'(S|s)erigala', tempSerigala)
    if(serigalaMatch):
        tempSerigala = tempSerigala[serigalaMatch.end():]
        for i in range(len(result)):
            if(result[i][1] > serigalaMatch.start()+newSerigalaStart):
                result.insert(i, ("s", serigalaMatch.start()+newSerigalaStart))
                appendBool = False
                break
        
        if(appendBool):
            result.append(("s", serigalaMatch.start()+newSerigalaStart))
        newSerigalaStart = serigalaMatch.end()
    else:
        serigalaCheck = False

#Harimau
tempHarimau = copy.deepcopy(text)
newHarimauStart = 0
harimauCheck = True

while(harimauCheck):
    appendBool = True
    HarimauMatch = re.search(r'(H|h)arimau', tempHarimau)
    if(HarimauMatch):
        tempHarimau = tempHarimau[HarimauMatch.end():]
        for i in range(len(result)):
            if(result[i][1] > HarimauMatch.start()+newHarimauStart):
                result.insert(i, ("h", HarimauMatch.start()+newHarimauStart))
                appendBool = False
                break
        
        if(appendBool):
            result.append(("h", HarimauMatch.start()+newHarimauStart))
        newHarimauStart = HarimauMatch.end()
    else:
        harimauCheck = False


#display
for i in range(len(result)):
    if(result[i][0] == 'g') :
        if(i != len(result) - 1):
            print("sang gajah - ", end="")
        else:
            print("sang gajah", end="")
    elif(result[i][0] == 's') :
        if(i != len(result) - 1):
            print("serigala - ", end="")
        else:
            print("serigala", end="")
    elif(result[i][0] == 'h') :
        if(i != len(result) - 1):
            print("harimau - ", end="")
        else:
            print("harimau", end="")