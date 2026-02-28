#=================================================
# Nama : Annisa Nurul Izzati
# NIM  : J0403251012
# Kelas: B/P2
#=================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

# Class Node untuk menyimpan data pelanggan
class Node:
    def __init__(self, no, nama, servis):
        self.no = no            # Nomor antrian
        self.nama = nama        # Nama pelanggan
        self.servis = servis    # Jenis servis
        self.next = None        # Pointer ke node berikutnya
        # Awalnya None karena belum terhubung ke node lain


# Class Queue berbasis Linked List
class QueueBengkel:        # mengelola sistem antrian menggunakan konsep Queue dengan prinsip FIFO (First In First Out)
    def __init__(self):
        self.front = None  # Antrian terdepan
        self.rear = None   # Antrian terakhir

    # Fungsi untuk menambahkan pelanggan ke antrian (enqueue). Proses penambahan dilakukan dari bagian BELAKANG antrian
    def enqueue(self, no, nama, servis):
        node_baru = Node(no, nama, servis)   # Membuat node baru berisi data pelanggan

        # Jika antrian kosong
        if self.front is None:
            # Front dan rear sama-sama menunjuk ke node baru karena hanya ada satu pelanggan dalam antrian
            self.front = node_baru
            self.rear = node_baru

        else:
            # Jika antrian sudah berisi pelanggan Node terakhir (rear) akan menunjuk ke node baru
            self.rear.next = node_baru
            self.rear = node_baru
        

        print("Pelanggan berhasil ditambahkan ke antrian.")

    # Melayani pelanggan terdepan (dequeue)
    def dequeue(self):
        # Mengecek apakah antrian kosong
        if self.front is None:
            print("Antrian kosong. Tidak ada pelanggan yang dilayani.")
            return

        # Menampilkan data pelanggan yang sedang dilayani
        print("Melayani pelanggan:")
        print(f"No Antrian : {self.front.no}")
        print(f"Nama       : {self.front.nama}")
        print(f"Servis     : {self.front.servis}")

        # Geser front ke node berikutnya, artinya pelanggan terdepan telah keluar dari antrian
        self.front = self.front.next

        # Jika antrian menjadi kosong maka rear juga harus di-set ke None
        if self.front is None:
            self.rear = None

    # Menampilkan seluruh antrian
    def tampilkan(self):
        if self.front is None:
            print("Antrian masih kosong.")
            return

        print("\nDaftar Antrian Pelanggan:")
        current = self.front
        while current:
            print(f"No Antrian : {current.no} | Nama : {current.nama} | Servis : {current.servis}")
            current = current.next


# Program utama
def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)
        elif pilih == "2":
            q.dequeue()
        elif pilih == "3":
            q.tampilkan()
        elif pilih == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()