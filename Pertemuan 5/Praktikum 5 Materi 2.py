#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#===============================================


#===============================================
# Materi Rekrursif : Call Stack
# tracing bilangan (masuk-keluar)
# input 3
# Masuk  3-2-1
# keluar 1-2-3
#===============================================

def hitung(n):

    #base case
    if n==0 :
        print("selesai")
        return
    
    print ("masuk :", n)
    hitung(n-1) #recursive case
    print("keluar", n)

print("====== Program Tracing ======")
hitung(3)