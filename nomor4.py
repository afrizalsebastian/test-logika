import numpy as np

arrInt = []
temp = ""


# Input
arrayInput = input("")

for inputUser in arrayInput :
    if(inputUser == "]"):
        intTemp = int(temp)
        temp = ""
        arrInt.append(intTemp)
    elif(inputUser == '0' or inputUser == '1' or inputUser == '2' or inputUser == '3' or inputUser == '4' or inputUser == '5' or inputUser == '6' or inputUser == '7' or inputUser == '8' or inputUser == '9'):
        temp += inputUser
    elif(inputUser == ',') :
        intTemp = int(temp)
        temp = ""
        arrInt.append(intTemp)


# Check
npArr = np.sort(arrInt)
currentValue = npArr[0]

for elmt in npArr :
    if(elmt == currentValue):
        currentValue += 1
    else :
        break

print(currentValue)
