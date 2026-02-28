#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================


# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

# Fungsi buat_pin digunakan untuk menghasilkan semua kemungkinan
# PIN dengan panjang tertentu menggunakan digit 0, 1, dan 2.

def buat_pin(panjang, hasil=""):
# Parameter:
# - panjang : panjang PIN yang diinginkan
# - hasil   : string sementara untuk menyimpan PIN yang sedang dibentuk
    
    # Base case
    
    # Jika panjang string hasil sudah sama dengan panjang PIN
    # yang diinginkan, maka satu PIN lengkap telah terbentuk.
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Recursive case

    # Loop digunakan untuk menentukan digit apa saja yang boleh digunakan dalam pembentukan PIN.
    # Setiap iterasi akan menambahkan satu digit ke string hasil,
    # kemudian fungsi memanggil dirinya sendiri (rekursi).
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


# Pemanggilan fungsi untuk menghasilkan PIN sepanjang 3 digit
buat_pin(3)