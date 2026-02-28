#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

# Fungsi pangkat digunakan untuk menghitung nilai a^n
# menggunakan konsep rekursi (pemanggilan fungsi ke dirinya sendiri)
def pangkat(a, n):

    # Base case adalah kondisi penghentian rekursi.
    # Jika n == 0, maka hasil pangkat selalu 1.
    # Tanpa base case, fungsi akan memanggil dirinya sendiri terus-menerus
    if n == 0:
        return 1
    
    # Recursive case
    # Fungsi akan memanggil dirinya sendiri dengan nilai n yang lebih kecil sampai mencapai base case.
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16