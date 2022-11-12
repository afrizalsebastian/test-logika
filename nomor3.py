import numpy as np

number = [i for i in range(48, 58)]         #representasi angka pada ASCII decimal
upperCase = [i for i in range(65, 91)]      #representasi huruf kecil pada ASCII decimal 
lowerCase = [i for i in range(97, 122)]     #representasi huruf kapital pada ASCII decimal

#input user
password = input("Password = ") 
passASCII = list(password.encode('ascii'))  #encode ke ASCII dalam bentuk list

if(len(password )>= 8 and len(password) <= 32):
    if(passASCII[0]>=48 and passASCII[0]<=57):  #Jika password diawali angka
        print("Karakter awal tidak boleh angka")
    else:
        checkNumber = np.isin(passASCII, number)                    #melakukan pengecekan angka pada password
        checkUpperCase = np.isin(passASCII, upperCase)              #melakukan pengecekan huruf kapital pada password
        checkLowerCase = np.isin(passASCII, lowerCase)              #melakukan pengecekan huruf kecil pada password
        if(np.any(checkNumber) and np.any(checkUpperCase) and np.any(checkLowerCase)): #jika password Valid
            print("Kata sandi valid")
        else:
            if(not(np.any(checkNumber) and (not(np.any(checkLowerCase)) or not(np.any(checkUpperCase))))):
                print("Harus memiliki huruf kapital dan huruf kecil")
                print("Harus memiliki angka")
            elif(not(np.any(checkNumber))):
                print("Harus memiliki angka")
            else:
                print("Harus memiliki huruf kapital dan huruf kecil")
else:
    print("Panjang password tidak sesuai (Note : Minimal = 8 karakter dan Maksimal = 32 karakter)")