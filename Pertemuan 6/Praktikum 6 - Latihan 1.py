#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================

# ==========================================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = key

    return data

'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

Jawaban :
1)  Karena elemen pertama (index 0) dianggap sudah rapi 
    sebagai patokan di awal, jadi mulai ambil data dari elemen kedua

2)  Sebagai tempat menyimpan sementara angka yang mau dipindah, 
    supaya tidak hilang saat angka lain digeser.

3)  Karena kita nggak tahu harus mundur berapa kali. 
    (while) bakal berhenti otomatis begitu ketemu angka yang lebih kecil 
    atau sudsah mentok di ujung kiri

4)  Operasi pergeseran (shifting) angka yang lebih besar ke arah kanan 
    untuk memberi ruang buat si (key).

'''