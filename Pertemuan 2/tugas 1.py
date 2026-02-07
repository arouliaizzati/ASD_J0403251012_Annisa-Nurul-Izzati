# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Annisa Nurul Izzati
# NIM : J0403251012
# Kelas : B2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------


nama_file = "stok_barang.txt"
# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

#Membaca data stok dari file teks.
def baca_stok(nama_file):
    stok_dict = {}
    with open (nama_file,"r", encoding="utf-8") as file:
        for baris in file:
            baris=baris.strip()
            if baris == "":
                continue

            data = [x.strip() for x in baris.split(",")]
            if len(data) != 3:
                continue

            KodeBarang, NamaBarang, Stok = data

        
            #KodeBarang ,NamaBarang ,Stok = baris.split (",")
            stok_dict[KodeBarang]={
               "NamaBarang" : NamaBarang,
                "Stok" : int(Stok)
            }
    return stok_dict

 # TODO: Buka file dan baca seluruh baris
 # Hint: with open(nama_file, "r", encoding="utf-8") as f:
 # TODO: Untuk setiap baris:
 # - gunakan strip() untuk menghilangkan \n
 # - split(",") untuk memisahkan kolom
 # - simpan ke dictionary

    

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

#Menyimpan seluruh data stok ke file teks
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for KodeBarang in sorted(stok_dict.keys()):
            NamaBarang = stok_dict[KodeBarang]["NamaBarang"]
            Stok = stok_dict[KodeBarang]["Stok"]
            file.write(f"{KodeBarang},{NamaBarang},{Stok}\n")

 # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
 # Hint: with open(nama_file, "w", encoding="utf-8") as f:



# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

#Menampilkan semua barang di stok_dict.
def tampilkan_semua(stok_dict):
    if len (stok_dict) ==0:
        print("stok kosong")
        return
    
    #membuat header tabel
    print("\n========== Daftar Barang ==========")
    print(f"{'Kode' : <10} | {'Nama Barang' : <15} | {'Stok' :>5}")
    print ("-" * 36) #membuat garis header

    #untuk tampilan yang rapi, atur f-srting formating
        #{'Kode Barang' : <10} artinya :tampilan kode <= rata kiri dengan lebar 10 karakter
        #{'Nama barang' : <12} artinya : tampilan barang rata kiri dengan lebar kolom 12 karakter
        #{'Stok' : >5}" artinya : tampilan stok >= rata kanan, lebar kolom 5 karakter

    for KodeBarang in sorted(stok_dict):
        NamaBarang=stok_dict[KodeBarang]["NamaBarang"]
        Stok=stok_dict[KodeBarang]["Stok"]
        print(f"{KodeBarang:<10} | {NamaBarang:<15} |{Stok:>5}")


 # TODO: Jika kosong, tampilkan pesan stok kosong
 # TODO: Tampilkan dengan format rapi: kode | nama | stok



# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------

#Mencari barang berdasarkan kode barang
def cari_barang(stok_dict):

    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict:
        NamaBarang= stok_dict[kode]["NamaBarang"]
        Stok= stok_dict[kode]["Stok"]

        print("\n=== Data Barang ditemukan ===")
        print(f"KodeBarang     : {kode}")
        print (f"NamaBarang   : {NamaBarang}")
        print(f"Stok   : {Stok}")
    else:
        print("Barang tidak ditemukan")

 # TODO: Cek apakah kode ada di dictionary
 # Jika ada: tampilkan detail barang
 # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
 


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------

def tambah_barang(stok_dict):

    #Menambah barang baru ke stok_dict.
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in stok_dict:
        print("Kode sudah digunakan")
        return
    
    nama = input("Masukkan nama barang: ").strip()
    try:
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    # Simpan ke dictionary
    stok_dict[kode] = {
        "NamaBarang": nama,
        "Stok": stok_awal
    }
    print("Barang baru berhasil ditambahkan.")
    

 # TODO: Validasi kode tidak boleh duplikat
 # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
 # TODO: Input stok awal (integer)
 # Hint: stok_awal = int(input(...))
 # TODO: Simpan ke dictionary
 


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------


#Mengubah stok barang (tambah atau kurangi).
def update_stok(stok_dict):

    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah=int(input("Masukkan jumlah barang yang di update: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    stok_lama= stok_dict[kode]["Stok"]

    if pilihan == "1":
        stok_dict[kode]["Stok"] += jumlah
        print("Stok berhasil ditambahkan.")
    elif pilihan == "2":
        if stok_dict[kode]["Stok"] - jumlah < 0:
            print("Error: stok tidak boleh negatif.")
        else:
            stok_dict[kode]["Stok"] -= jumlah
            print("Stok berhasil dikurangi.")
    
    stok_baru= stok_dict[kode]["Stok"]
    #memasukkan nilai update baru ke dictionary
    

    print(f"Update berhasil, nilai {kode} berubah dari {stok_lama} menjadi {stok_baru}")


 # TODO: Cek apakah kode ada di dictionary
 # Jika tidak ada: tampilkan pesan dan return

 # TODO: Input jumlah perubahan stok
 # Hint: jumlah = int(input("Masukkan jumlah: "))
 # TODO:
 # - Jika pilihan 1: stok = stok + jumlah
 # - Jika pilihan 2: stok = stok - jumlah
 # - Jika hasil < 0: batalkan dan tampilkan error



# -------------------------------
# Program Utama
# -------------------------------

def main():
 # Membaca data dari file saat program mulai
 stok_barang = baca_stok(nama_file)
 while True:
    print("\n=== MENU STOK KANTIN ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan kode")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Simpan ke file")
    print("0. Keluar")
    pilihan = input("Pilih menu: ").strip()
    if pilihan == "1":
        tampilkan_semua(stok_barang)
    elif pilihan == "2":
        cari_barang(stok_barang)
    elif pilihan == "3":
        tambah_barang(stok_barang)
    elif pilihan == "4":
        update_stok(stok_barang)
    elif pilihan == "5":
        simpan_stok(nama_file, stok_barang)
        print("Data berhasil disimpan.")
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama

if __name__ == "__main__":
    main()