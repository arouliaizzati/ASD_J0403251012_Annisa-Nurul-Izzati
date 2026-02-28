#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================


# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

# Fungsi countdown digunakan untuk menelusuri (tracing)
# bagaimana proses rekursi berjalan dari pemanggilan awal
# hingga kembali (return) ke pemanggil sebelumnya.
def countdown(n):

    # Base case
    # Jika n bernilai 0, maka rekursi dihentikan.
    # Fungsi mencetak "Selesai" lalu keluar (return)
    # tanpa memanggil dirinya sendiri lagi.
    if n == 0:
        print("Selesai")
        return


    # Proses sebelum pemanggilan rekursif
    # Baris ini dieksekusi saat fungsi "masuk" ke level rekursi.
    # Menunjukkan nilai n saat fungsi pertama kali dipanggil.
    print("Masuk:", n)


    # Pemanggilan rekursif
    countdown(n - 1)


    # Proses setelah pemanggilan rekursif
    print("Keluar:", n)


# Pemanggilan fungsi awal
countdown(3)