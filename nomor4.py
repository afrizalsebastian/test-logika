import numpy as np

arrInt = []
temp = ""

# Input
arrayInput = input("")                           ## Input berupa "[number, number, ...]"

for inputUser in arrayInput :                   #Mengambil setiap angka pada input-an
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
npArr = np.sort(arrInt)                         #sort array
currentValue = npArr[0]                         #Sequential number (nilai yang seharusnya)

for elmt in npArr :
    if(elmt == currentValue):
        currentValue += 1
    else :                                      #Jika tidak ditemukan angka yang seharusnya (terkecil)
        break

print(currentValue)
