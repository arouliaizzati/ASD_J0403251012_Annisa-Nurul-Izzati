



#======================================
#Latihan 1: Implementasikan	fungsi untuk menghapus node dengan nilai tertentu.
#======================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, nilai_dihapus):
        temp = self.head
        if temp and temp.data == nilai_dihapus:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != nilai_dihapus:
            prev = temp
            temp = temp.next
    
        if temp is None:
            return
        prev.next = temp.next
        temp = None

#memasukkan data linked list
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(7)
ll.insert_at_end(9)
ll.insert_at_end(5)
ll.display()

ll.delete_node(9)
ll.display()


#======================================
#Latihan 2: Buat kode implementasikan pencarian pada node tertentu single circular linked list
#======================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        pass

class CircularSinglyLinkedList:
    def	__init__(self):
        self.head = None
        self.tail =	None # Tambahkan pointer tail

    def	insert_at_end(self,	data):
        new_node = Node(data)
        if	not	self.head: # Jika linked list kosong
            self.head	=	new_node
            self.tail	=	new_node
            self.tail.next	=	self.head #	Circular link ke dirinya sendiri
        else:
            self.tail.next = new_node #	Sambungkan tail	ke node	baru
            self.tail =	new_node # Update tail ke node baru
            self.tail.next = self.head # Circular link kembali ke head
               
    def display (self):
        if not self.head:
            print("list is empty")
            return
        print("Circular linked list traversal: ")
        temp = self.head
        print(temp.data, end="->")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end="->")
            temp = temp.next

        print("....(back to head)")



#masukkan datanya
cll= CircularSinglyLinkedList
for x in [3,6,34,7,13,5]:
    cll.insert_at_end(x)
cll.display()
