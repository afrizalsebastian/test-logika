N = int(input("Nilai N = "))

counter = 0         #counter untuk banyak angka yang akan ditampilkan
number = 3          #Angka yang akan diiterasi secara berurut

while(counter < N):                         #Melakukan Loop sebanyak counter
    if (number % 3 == 0 and number % 7 == 0):
        if(counter != N-1):
            print("N, ", end="")
        else :
            print("N", end="")
        counter +=1
    elif(number % 3 == 0 or number % 7 == 0):
        if(counter != N-1):
            print(number,', ', end="")
        else:
            print(number, end="")
        counter +=1
    number +=1
