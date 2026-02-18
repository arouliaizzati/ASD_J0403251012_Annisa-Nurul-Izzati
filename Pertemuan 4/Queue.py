#=================================================
#Nama : Annisa Nurul Izzati
#NIM : J0403251012
#Kelas : B2
#===============================================


#===============================================
#Implementasi Dasar : Queue berbasis linked list
#===============================================


#membuat class node (merupakan unit dasar dari variabel)
class Node:
    def __init__(self,data): #otomatis construktornya dijalankan (konstruktor)
        self.data = data #menyimpan nilai/ data
        self.next = None #inisialisasi pointer (pointer ke note berikutnya) (awal=none)

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue (self,data):#entry queue
        #menambah data dibelakang (rear)
        nodebaru = Node(data)
    
        #jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodebaru
            self.rear = nodebaru
            return
        
        #jika queue tidak kosong:
        #rear lama menunjuk ke node baru
        self.rear.next = nodebaru #dia masih sekedar nunjuk aja (pointer) saat ada .next
        #rear pindah ke node baru
        self.rear = nodebaru

    def dequeue(self):
        #menghapus data dari depan

        #1. mengambil data yang paling depan (masih proses melihat data)
        data_terhapus = self.front.data

        #2. geser front ke node berikutnya
        self.front = self.front.next

        #3. jika setelah digeser front menjadi none, maka queue kosong
        #reaer juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus


    def tampilkan(self):

        current = self.front
        print("front -", end="-> ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print("none - rear di node terakhir")


#Instantiasi objek class QueueLL

q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()

q.dequeue()
q.tampilkan()
