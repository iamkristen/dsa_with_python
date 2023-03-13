class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None
    
class DLinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self,data):
        self.head = Node(data,self.prev,self.next)
    #     if self.head.next:
    #         next= self.head.next
    #         next.prev = self.head
    
    def print(self):
        itr = self.head
        next = None
        prev = None
        while itr:
            print("data =>" + str(itr.data))
            next = itr.next
            if(next is not None):
                print("Next =>"+str(next.data))
            prev = itr.prev
            if(prev is not None):
                print("prev =>"+str(prev.data))
            itr = itr.next
            

if __name__ == "__main__":
    root = DLinkedList()
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)

    root.head = n1
    n1.next = n2
    n2.next = n3
    n2.prev = n1
    n3.next = n4
    n3.prev = n2
    # root.push(5)
    # root.push(4)
    # root.push(6)
    # root.push(8)
    root.print()
