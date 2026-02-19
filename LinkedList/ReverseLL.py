class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

nodes = [n1,n2,n3,n4]
for i in range(0,len(nodes)-1):
    nodes[i].next =nodes[i+1]

head = n1
prev=None
current = head


while current is not None:
    new_node = current.next
    current.next = prev
    prev = current
    current = new_node
head = prev

temp = head

while temp is not None:
    print(temp.val,end='=>')
    temp = temp.next
print(None