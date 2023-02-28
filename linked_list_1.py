class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data,self.head)
        self.head = node

    def append(self,data):
        itr = self.head
        last = itr
        while itr:
            if(itr.next is None):
                last = itr
            itr = itr.next
        last.next = Node(data,None)

    def pop(self):
        itr = self.head
        itr.data = itr.next.data
        itr.next = itr.next.next


    def delete(self):
        itr = self.head
        prev = itr
        while itr:
            
            if(itr.next is not None):
                prev = itr
            itr = itr.next
        prev.next = None



    def printList(self):
        itr  = self.head
        lst = ''
        while itr:
            suffix ="==>"if itr.next else''
            lst +=str(itr.data)+suffix
            itr = itr.next
        print(lst)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        print(count)

if __name__ == "__main__":
    root = LinkedList()
    root.push(3)
    root.push(6)
    root.push(4)
    root.printList()
    root.append(8)
    root.printList()
    root.pop()
    root.printList()
    root.delete()
    root.printList()
    root.getLength()