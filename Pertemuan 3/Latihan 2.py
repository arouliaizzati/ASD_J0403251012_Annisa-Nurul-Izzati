#======================================
#Latihan 2: Buat kode implementasikan pencarian pada node tertentu single circular linked list
#======================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def display(self):
        if not self.head:
            print("list is empty")
            return
        print("Circular linked list: ")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("....(back to head)")

    def search(self, key):
        if not self.head:
            print("Tidak ada elemen yang dicari dalam circular linked list")
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan")
                return True
            temp = temp.next
            if temp == self.head: #sudah melakukan 1 kali putaran
                break
        
        print(f"Elemen {key} tidak ditemukan")
        return False


# ===== Testing =====
cll = CircularSinglyLinkedList()
#Tampilan elemen ada
for x in [3, 7, 12, 19, 25, 5]:
    cll.insert_at_end(x)

cll.display()
cll.search(12) #contoh contoh elemen yang ada


#Tampilan elemen tidak ada
cll1 = CircularSinglyLinkedList()
for x in [5, 10, 15, 20, 30]:
    cll1.insert_at_end(x)

cll1.display()
cll1.search(25) #contoh elemen yang tidak ada

#Tampilan list kosong
cll2 = CircularSinglyLinkedList()
for x in []:
    cll2.insert_at_end(x)

cll2.display()
cll2.search(30) #contoh elemen yang tidak ada di linked list kosong