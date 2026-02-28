#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#===============================================


#===============================================
# Materi Rekrursif : Menjumlahkan elemen list
#===============================================

def jumlah_list(data, index=0):
    #base case :jika index sudah mencapai panjang list
    if index == len(data):
        return 0

    #recursive case : elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index+1)

print("====== Program Jumlah Data ======")
print (jumlah_list([2,4,5]))