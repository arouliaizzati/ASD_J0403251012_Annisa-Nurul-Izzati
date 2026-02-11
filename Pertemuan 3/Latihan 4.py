#======================================
#Latihan 4: Buat metode untuk menggabungkan dua single linked list menjadi satu linked list baru
#======================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def concatenate(self, other_list):
        # Jika linked list pertama kosong, hasilnya linked list kedua
        if not self.head:
            self.head = other_list.head
            return
        
        # Jika linked list kedua kosong, hasilnya linked list pertama tetap
        if not other_list.head:
            return
        
        # Cari node terakhir linked list pertama
        temp = self.head
        while temp.next:
            temp = temp.next
        
        # Hubungkan node terakhir linked list pertama dengan head linked list kedua
        temp.next = other_list.head


# ===== Testing =====

#====== Linked list ada isinya========
print("====== Linked list ada isinya========")
# Buat linked list 1 dan isi data
ll1 = SingleLinkedList()
for x in [1, 3, 5, 7]:
    ll1.insert_at_end(x)
print("Linked List 1:")
ll1.display()

# linked list 2 dan isi data
ll2 = SingleLinkedList()
for x in [2, 4, 6, 8]:
    ll2.insert_at_end(x)
print("Linked List 2:")
ll2.display()

# Gabungkan linked list 2 ke linked list 1
ll1.concatenate(ll2)
print("Linked List setelah digabungkan:")
ll1.display()


#======== Salah satu linked list kosong =========
print("======== Salah satu linked list kosong =========")
ll3 = SingleLinkedList()
for x in [1, 3, 5, 7]:
    ll3.insert_at_end(x)
print("Linked List 3:")
ll3.display()

ll4 = SingleLinkedList()
for x in []:
    ll4.insert_at_end(x)
print("Linked List 4:")
ll4.display()

# Gabungkan linked list 2 ke linked list 1
ll3.concatenate(ll4)
print("Linked List setelah digabungkan:")
ll3.display()
