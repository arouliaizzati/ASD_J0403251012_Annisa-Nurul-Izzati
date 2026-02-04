#Praktikum 1 : Konsep ADT dan file handling
# latihan dasar 1A : Membaca seluruh ii file


#membuka file dengan mode read ("r") dalam satu string
with open("data_Mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca seluruh isi file dalam satu string
print (isi_file)

print()
print ("=========Hasil Read=========")
print("Tipe data : ", type(isi_file))
print('Jumlah karakter', len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)
print()

#membuka file per baris
print("=========Membaca file per baris==========")
jumlah_baris= 0
with open ("data_Mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris= jumlah_baris+1
        baris=baris.strip() #menghilangkan baris baru \n sehingga terambil data murninya
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)


print()
#=========================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 2 : Parsing data   

print("============Membaca file per data============")
with open ("data_Mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris =baris.strip()
        nim, nama, nilai= baris.split(",") #parsing data berdasarkan karakter
        print("NIM : ", nim,"| Nama : ", nama,"| Nilai: ", nilai) # | digunakan untuk membedakan kolomnya


print()
#=========================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 3 : Membaca File dan menyimpan kelist


data_list= [] #list untukmenampung data mahasiswa
with open ("data_Mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris=baris.strip()

        nim, nama, nilai = baris.split(",")
        #simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print("==========Data mahasiswa dalam list==========")
print(data_list)
print()

print("==========jumlah record dalam list==========")
print("jumlah record", len(data_list))
print()

print("==========Menampilkan data record tertentu==========")
print("Contoh record pertama", data_list[0])


print()
#=========================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 4: Membaca File dan menyimpan ke dictionary


data_dict= {} #buat variabel untuk dictionary
with open ("data_Mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris=baris.strip()
        nim, nama, nilai= baris.split(",")

        #simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim]= {           #key
            "nama": nama,           #values
            "nilai": int(nilai)     #values
        }
print("==========Data mahasiswa dalam Dictionary==========")
print(data_dict)