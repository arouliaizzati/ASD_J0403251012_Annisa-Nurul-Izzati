#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#=================================================

# ==========================================================
# Latihan 5 : Melengkapi Fungsi Merge
# ==========================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if ______________________: #
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



'''

Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().

Jawaban :
1) if left[i] <= right[j]: #
            result.append(left[i])
            i += 1

2) Fungsi result.extend() digunakan untuk menambahkan 
   seluruh elemen yang tersisa dari list left atau right 
   ke dalam list result, sehingga semua elemen tergabung 
   menjadi satu list


'''