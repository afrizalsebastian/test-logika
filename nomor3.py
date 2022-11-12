import numpy as np

number = [i for i in range(48, 58)]
upperCase = [i for i in range(65, 91)]
lowerCase = [i for i in range(97, 122)]

password = input("")
passASCII = list(password.encode('ascii'))

if(passASCII[0]>=48 and passASCII[0]<=57):
    print("Karakter awal tidak boleh angka")
else:
    checkNumber = np.isin(passASCII, number)
    if(np.any(checkNumber)):
        checkUpperCase = np.isin(passASCII, upperCase)
        if(np.any(checkUpperCase)):
            checkLowerCase = np.isin(passASCII, lowerCase)
            if(np.any(checkLowerCase)):
                print("Kata sandi valid")
            else:
                print("Harus memiliki huruf kapital dan huruf kecil")
        else:
            print("Harus memiliki huruf kapital dan huruf kecil")
    else:
        print("Harus memiliki angka")