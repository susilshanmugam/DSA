class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


node1=Node(1)
node2=Node(2)

node1.next=node2
print("linked list starts:")
current_node=node1
while current_node.next is not None:
    print(current_node.data,end='->')
    current_node=current_node.next
print(current_node.data)