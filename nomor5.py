N = int(input("Input Nilai N = "))

#Iterative
# if(N % 2 == 0):
#     print("Harus bilangan ganjil")
# else:
#     for i in range(N):
#         for j in range(N):
#             if(i == 0 or j==0 or j == N-1 or i == N-1):
#                 print("X", end="")
#             else:
#                 if(i+j == N-1):
#                     print("X", end="")
#                 else:
#                     print("O", end="")
#         print("")


#Rekursif
def makePattern(N, jumlahOKiri, jumlahOKanan, segment):
    if(segment == 0 or segment == 2):                           #Segment Semua X (dilihat dari baris)
        for i in range(N):
            print("X", end="")

        if(segment == 0):
            print()
        makePattern(N, jumlahOKiri, jumlahOKanan, segment+1)

    elif(segment == 1):                                         #Segment Terdapat O pada pattern
        if(jumlahOKanan != (N-2)):
            for i in range(N):
                if(i == 0 or i == N-1):
                    print("X", end="")
                else:
                    if(i == jumlahOKiri + 1):
                        print("X", end="")
                    else:
                        print("O", end="")
            print()
            makePattern(N, jumlahOKiri-1, jumlahOKanan+1, segment) #Rekursif untuk pattern selanjutnya
        else:
            makePattern(N, jumlahOKiri-1, jumlahOKanan+1, segment+1) #Rekursif untuk pattern selanjutnya
    

jumlahOKiri = N - 3
jumlahOKanan = 0
if(N %  2 == 0):
    print("Harus bilangan ganjil")
else:
    if(N == 1):
        print("X")
    else:
        makePattern(N, jumlahOKiri, jumlahOKanan, 0)


