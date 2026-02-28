#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#===============================================


#===============================================
#Materi Rekrursif : Faktorial
# recursive case => 3! = 3 x 2 x 1 
# base case => 0 berhenti 
#===============================================

def faktorial(n):
    #base case
    if n==0:
        return 1

    #recursive case
    return n*faktorial(n-1)   #n-1*n-2*n-3..........n-?
print("===== Programm Faktorial =====")
print("Hasil faktorial : ", faktorial(3))