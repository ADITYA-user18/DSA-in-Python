class Node:
    def __init__(self,val):
        self.val = val
        self.next=None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

nodes = [n1,n2,n3,n4,n5]

for i in range(0,len(nodes)-1):
    nodes[i].next = nodes[i+1]

head = n1
temp = head

odd = head
even = odd.next

while odd and odd.next:
     print(odd.val,end='=>')
     odd = odd.next.next
if odd:
    print(odd.val,end='=>')
        
while even and even.next:
    print(even.val,end='=>')
    even = even.next.next
if even:
        print(even.val,end='=>')

print(None)
