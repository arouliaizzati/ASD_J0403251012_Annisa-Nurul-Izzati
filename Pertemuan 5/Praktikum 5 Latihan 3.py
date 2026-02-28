#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================


# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
# Parameter:
# - data  : list berisi angka-angka
# - index : posisi elemen yang sedang diperiksa (default = 0)

    # Base case
    # Base case terjadi saat index berada pada elemen terakhir list.
    # Jika sudah sampai elemen terakhir, maka nilai tersebut
    # langsung dikembalikan sebagai nilai maksimum sementara.
    if index == len(data) - 1:
        return data[index]
    

    # Recursive case
    # Fungsi memanggil dirinya sendiri untuk mencari nilai maksimum
    # pada sisa elemen list (index + 1 sampai akhir).
    maks_sisa = cari_maks(data, index + 1)

    # Setelah mendapatkan nilai maksimum dari sisa list,
    # nilai tersebut dibandingkan dengan elemen pada index saat ini.
    if data[index] > maks_sisa:
        # Jika elemen saat ini lebih besar, maka elemen tersebut menjadi nilai maksimum
        return data[index]
    else:
        # Jika tidak, nilai maksimum tetap dari sisa list
        return maks_sisa


# Data yang akan dicari nilai maksimumnya
angka = [3, 7, 2, 9, 5]

# Pemanggilan fungsi dan menampilkan hasil
print("Nilai maksimum:", cari_maks(angka))