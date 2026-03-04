#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================

# ==========================================================
# Latihan 2 : Melengkapi Potongan Kode
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and ______________________:
            data[j + 1] = data[j]
            j -= 1

        ______________________

    return 

'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending.

Jawaban :
1)  Ascending
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key

    Isi dengan data[j]> key #karena kita mau geser angka kanan 
    yang JIKA angka di sebelah kirinya (data[j]) > dari angka 
    yang dipegang (key)

2.  Descending
    while j >= 0 and data[j] < key:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key

    Isi dengan data[j]< key #karena di sini kita mau geser angka 
    ke kanan kalau angka di kiri itu lebih kecil. Jadi angka yang 
    paling gede bakal "menggusur" angka kecil ke belakang


'''