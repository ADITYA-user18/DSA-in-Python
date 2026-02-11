class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)

nodes = [n1,n2,n3,n4,n5,n6]

for i in range(0,len(nodes)-1):
    nodes[i].next = nodes[i+1]


head = n1
temp = head

while temp.next.next is not None:
    temp = temp.next
temp.next=None


temp = head
while temp is not None:
    print(temp.val,end='=>')
    temp = temp.next
print(None)