#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================

# ==========================================================
# Latihan 3 : Tracing Insertion Sort
# ==========================================================

def insertion_sort (data):
    #melihat data awal
    print("Data awal: ",data)
    print("="*50)

    #loop milai dari data ke 2 (index array ke 1)
    for i in range (1, len (data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index elemen terakhir di bagian kiri data

        print("Iterasi ke- ", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut): ", data[:i])
        print("Bagian kanan (belum terurut): ", data[i:])
        
        #geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j-=1

        #sisipkan key ke posisi yang benar
        data[j+1]=key

        print("Setelah disisipkan :", data)
        print("-"*50)

    return data

data = [5, 2, 4, 6, 1, 3]
print("Hasil sorting : ", insertion_sort(data))



'''
Buat program dengan menggunakan algoritma insertion sort
Tracing dengan data = [5, 2, 4, 6, 1, 3]


Soal:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?

Jawaban :
1) Isi list setelah iterasi i = 1 [2, 5, 4, 6, 1, 3]
2) Isi list setelah iterasi i = 3 [2, 4, 5, 6, 1, 3]
3) Pada iterasi i = 4 terjadi 4 kali pergeseran, 
   karena angka 1 lebih kecil dari semua elemen sebelumnya 
   sehingga seluruh elemen tersebut digeser ke kanan


'''