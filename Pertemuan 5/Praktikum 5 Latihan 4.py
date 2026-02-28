#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================


# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

# Fungsi kombinasi digunakan untuk menghasilkan semua
# kemungkinan kombinasi huruf "A" dan "B" sepanjang n karakter.

def kombinasi(n, hasil=""):
# Parameter:
# - n     : panjang kombinasi yang diinginkan
# - hasil : string sementara untuk menyimpan kombinasi yang sedang dibentuk

    
    # Base case
    
    # Jika panjang string hasil sudah sama dengan n, berarti satu kombinasi telah terbentuk.
    # Kombinasi tersebut dicetak lalu fungsi dihentikan (return).
    if len(hasil) == n:
        print(hasil)
        return

    
    # Recursive case 1
    
    # Menambahkan huruf "A" ke hasil saat ini, lalu memanggil fungsi kombinasi kembali.
    # membentuk cabang pertama dari pohon rekursi.
    kombinasi(n, hasil + "A")


    # Recursive case 2

    # Menambahkan huruf "B" ke hasil saat ini, lalu memanggil fungsi kombinasi kembali.
    # membentuk cabang kedua dari pohon rekursi.
    kombinasi(n, hasil + "B")

kombinasi(2)