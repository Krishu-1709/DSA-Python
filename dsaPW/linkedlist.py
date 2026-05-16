class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
a= Node(1)
b= Node(2)
c= Node(3)
d= Node(4)
a.next = b
b.next = c
c.next = d
d.next = None




# e = insertAtStart(12)
def printLinkedList(head):
    curr = head
    print("head -> ", end="")

    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


def insertAtStart(head,data):
    temp = Node(data)
    temp.next = head
    return temp
def insertAtLast(head,data):


def insertAtKIndex(head,k,data):
    curr = head
    temp = Node(data)
    if k ==0:
        insertAtStart(head,data)
    for i in range(k-1):
        curr = curr.next
    temp.next = curr.next

    curr.next = temp
    

# head = insertAtStart(a,25)
# print(head.data)
insertAtKIndex(a,2,123)
printLinkedList(a)