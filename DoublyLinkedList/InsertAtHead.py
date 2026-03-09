class DLL:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

n1 = DLL(10)
n2 = DLL(20)
n3 = DLL(30)


nodes = [n1,n2,n3]

for i in range(0,len(nodes)-1):
    nodes[i].next = nodes[i+1]
    nodes[i+1].prev = nodes[i]



head = n1

new_node = DLL(40)

new_node.next = head
head.prev = new_node
head = new_node


while head is not None:
    print(head.val,end='=>')
    head = head.next
print(None)