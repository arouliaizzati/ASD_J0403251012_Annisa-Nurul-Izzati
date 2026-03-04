#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================

# ==========================================================
# Latihan 4 : Memahami Kode Program (Merge Sort)
# ==========================================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?

Jawaban :
1)  Base case adalah kondisi berhenti pada fungsi rekursif
    pada fungsi ini base case nya ada di bagian 
    if len(data) <= 1:
        return data
    yang artinya ketika data = 0 atau 1, maka fungsi dihentikan

2)  Fungsi memanggil dirinya sendiri karena menggunakan metode rekursi 
    untuk membagi data menjadi bagian yang lebih kecil hingga mencapai 
    base case, baru mengurutkan secara bertahap

3)  Tujuannya untuk menggabungkan 2 list yang sudah terurut (right dan left)
    menjadi 1 list baru yang tetap terurut



'''