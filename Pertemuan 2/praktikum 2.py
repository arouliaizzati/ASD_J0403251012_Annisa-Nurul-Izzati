# ===================================
# Praktikum 2 : KonsepADT dan file handlig
# Latihan 1 : Membuat fungsi load data
#====================================

nama_file ="data_Mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file) :
    data_dict= {} #inisialisasi data dictionary
    with open ("data_Mahasiswa.txt","r", encoding="utf-8") as file:
        for baris in file:
            baris=baris.strip()
            nim, nama, nilai= baris.split(",") #pecah menjadi data

            

            #simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim]= {           #key
                "nama": nama,           #values
                "nilai": int(nilai)     #values
            }
    print("==========Data mahasiswa dalam Dictionary==========")
    return (data_dict)

    #memanggil fungsi baca_data_mahasiswa
buka_data= baca_data_mahasiswa(nama_file)
print("jumlah data terbaca", len(buka_data))

# ==================================
# Praktikum 2 : KonsepADT dan file handlig
# Latihan 2 : Membuat fungsi menampilkan data
#===================================


def tampilan_data(data_dict):

    if len (data_dict) ==0:
        print("data kosong")
        return
    
    #membuat header tabel
    print("\n======= Daftar Mahasaiswa =======")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    print ("-" * 32) #membuat garis header

    #untuk tampilan yang rapi, atur f-srting formating
        #{'NIM' : <10} artinya :tampilan nim <= rata kiri dengan lebar 10 karakter
        #{'Nama' : <12} artinya : tampilan nama rata kiri dengan lebar kolom 12 karakter
        #{'Nilai' : >5}" artinya : tampilan nilai >= rata kanan, lebar kolom 5 karakter

    for nim in sorted(data_dict):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} |{nilai:>5}")

#memanggil fungsi menampilkan data
#tampilan_data(buka_data) ===============

# ==================================
# Praktikum 2 : KonsepADT dan file handlig
# Latihan 3 : Membuat fungsi mencari data
#===================================

def cari_data(data_dict):
    #mencari dta mahasiswa
    nim_cari = input("Masukkan NIM yang ingin di cari: ").strip()

    if nim_cari in data_dict:
        nama= data_dict[nim_cari]["nama"]
        nilai= data_dict[nim_cari]["nilai"]

        print("\n=== Data Mahasiswa ditemukan ===")
        print(f"NIM     : {nim_cari}")
        print (f"Nama   : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan") 

#cari_data(buka_data)================

# ==================================
# Praktikum 2 : KonsepADT dan file handlig
# Latihan 4 : Membuat fungsi update nilai
#===================================

def update_nilai(data_dict):
    
    #cari nim mahasiswa yang akan diupdate nilainya
    nim =input ("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan")
        return
    try: #kalau ada
        nilai_baru = int(input("Masukkan nilai baru (1-100): "))
    except ValueError:
        print("Nilai harus berupa angka")
        return
    
    if nilai_baru < 0 or nilai_baru >100:
        print("Nilai harus antara 0 sampai 100")

    nilai_lama= data_dict[nim]["nilai"]
    #memasukkan nilai update baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil, nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)===============

# ==================================
# Praktikum 2 : KonsepADT dan file handlig
#Latihan 5 : Membuat fungsi menyimpan perubahan data ke file
#===================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai} \n")
simpan_data(nama_file, buka_data)
#print(" data berhasil disimpan")=========


# ==================================
# Praktikum 2 : KonsepADT dan file handlig
# Latihan 6 : Membuat menu program
#===================================


def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n==== MENU DATA MAHASISWA ====")
    print("1. Tampilkan semua data")
    print("2. Cari data")
    print("3. Update data")
    print("4. simpan data ke file")
    print ("0. keluar")

    pilihan = input("pilhan menu: ").strip()

    if pilihan == "1":
        tampilan_data(buka_data)
    elif pilihan == "2":
        cari_data(buka_data)
    elif pilihan == "3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file,buka_data)
        print("data berhasil disimpan")
    elif pilihan == "0":
        print("program selesai")
        break
    #else:
        #print("pilihan tidak valid,coba lagi")

if __name__ == "__main__":
    main()   





