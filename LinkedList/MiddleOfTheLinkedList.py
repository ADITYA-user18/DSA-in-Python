class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)


Nodes = [a,b,c,d,e]

for i in range(0,len(Nodes)-1):
    Nodes[i].next = Nodes[i+1]


head = a

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next


print(f'Middle Element is : {slow.val}')