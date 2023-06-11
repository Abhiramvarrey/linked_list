'linked list creation'
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
n1=node(10)
linkedlist.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n3.next=None
def display():
    temp=linkedlist.head
    while temp:
        if temp.next:
            print(temp.data,end="-->")
        else:
            print(temp.data)
        temp=temp.next
def insert_beg(value):
    temp=linkedlist.head
    n=node(value)
    n.next=temp
    linkedlist.head=n
insert_beg(40)
def insert_end(value):
    n=node(value)
    temp=linkedlist.head
    while temp.next:
        temp=temp.next
    temp.next=n
insert_end(50)
def insert_mid(value,pos):
    n=node(value)
    temp=linkedlist.head
    while pos-1:
        temp=temp.next
        pos-=1
    n.next=temp.next
    temp.next=n
insert_mid(60,2)
display()