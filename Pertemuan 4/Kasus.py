#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B/P2
#===============================================


#===============================================
#Studi kasus : Sistem Antrian layanan Akademik
#===============================================

#Implementasi Queue =>
#Stak ==> Front -> c-> b-> a-> None
#Front -> a -> b -> c-> Rear 
#enqueue : memindahkan pointer rear (nambah data baru dari belakang)
#denqueue : memindahkan pointer front (menghapus data dari depan)


#1. Mendefinisikan node (unit dasar linked list)
class node:
    def __init__(self, nim, nama):
        self.nim  =nim #menyimpan nim mahasiswa
        self.nama =nama #menyimpan nama mahasiswa
        self.next =None #pointer ke node berikutnya

#2. mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front =None
        self.rear =None

    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.front is None
    
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue (self,nim,nama):
        node_baru =node(nim,nama) #instantiasi
        if self.is_empty():
            #jika ada data kamu masuk dari queue yang kosong maka data baru front = rear = none
            self.front=node_baru
            self.rear=node_baru
            return
        
        #jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        
        self.rear.next= node_baru
        self.rear = node_baru

    #menghapus data paling depan (memberikan laanan akademik)
    def dequeue(self):

        if self.is_empty():
            print ("antrian kosong. tidak ada mahasiswa dilayani)")
            return None

        #lihat data bagian front, simpan di variabel data yang akan dihapus (dilayanai)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none (dalam antrian terakhir yang dilayani), maka front =rear=none
        if self.front is None:
            self.rear=None
        
        return node_dilayani
    
    def tampilkan (self):
        print ("daftar antrian mahasiswa (front -> rear) : ")
        current= self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no +=1
    
#program utama

def main():

    #instantiasi queue
    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah mahasiswa")
        print("2. layani mahasiswa")
        print("3. Lihat antrian")
        print("4. Keluar")

        pilihan= input("pilih menu (1-4) : ").strip()

        if pilihan == "1":
            nim= input("Masukkan NIM : ").strip()
            nama= input("Masukkan Nama : ").strip()


            q.enqueue(nim,nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan =="3":
            q.tampilkan()

        elif pilihan =="4":
            print("program selesai")
            break
        else:
            print("pilihan tidak valid")
if __name__ == "__main__":
    main()