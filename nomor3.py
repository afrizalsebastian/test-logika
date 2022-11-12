import numpy as np

number = [i for i in range(48, 58)]         #representasi angka pada ASCII decimal
upperCase = [i for i in range(65, 91)]      #representasi huruf kecil pada ASCII decimal 
lowerCase = [i for i in range(97, 122)]     #representasi huruf kapital pada ASCII decimal

#input user
password = input("") 
passASCII = list(password.encode('ascii'))  #encode ke ASCII dalam bentuk list

if(passASCII[0]>=48 and passASCII[0]<=57):  #Jika password diawali angka
    print("Karakter awal tidak boleh angka")
else:
    checkNumber = np.isin(passASCII, number)                    #melakukan pengecekan angka pada password
    if(np.any(checkNumber)):                                    #jika password memiliki angka
        checkUpperCase = np.isin(passASCII, upperCase)          #melakukan pengecekan huruf kapital pada password
        if(np.any(checkUpperCase)):                             #jika password memiliki huruf kapital
            checkLowerCase = np.isin(passASCII, lowerCase)      #melakukan pengecekan huruf kecil pada password
            if(np.any(checkLowerCase)):                         #jika password memiliki huruf kecil
                print("Kata sandi valid")
            else:                                               #Jika tidak memiliki huruf kecil
                print("Harus memiliki huruf kapital dan huruf kecil")
        else:                                                   #jika tidak memiliki huruf besar
            print("Harus memiliki huruf kapital dan huruf kecil")
    else:                                                       #jika tidak memiliki angka
        print("Harus memiliki angka")