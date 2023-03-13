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
        if self.head is None:
            self.head = Node(data,None)

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def pop(self):
        self.head = self.head.next


    def delete(self):
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None


    def insertAfterValue(self,findValue,insertValue):
        itr = self.head
        while itr:
            if itr.data == findValue:
                node = Node(insertValue, itr.next)
                itr.next = node
            itr = itr.next

    def deleteByValue(self,value):
        itr = self.head
        prev = None
        while itr:
            if itr.data == value:
                if prev is not None:
                    prev.next = itr.next
                else:
                    self.head = itr.next
            prev = itr
            itr = itr.next
    
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
        return count
    
    def insertAt(self,index,data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid index")
        if(index == 0):
            self.push(data)
            return
        
        itr  = self.head
        count = 0
        while itr:
            if(count == index-1):
                itr.next = Node(data,itr.next)
                break
            count+=1
            itr = itr.next


    def deleteAt(self,index):
        if(index < 0 or index > self.getLength()):
            raise Exception("Invalid Index")
        
        if(index == 0):
            self.pop()
        
        itr = self.head
        count = 0

        while itr.next:
            if count == index-1:
                itr.next = itr.next.next if itr.next.next is not None else None
            count +=1
            itr = itr.next
        
    def insertValues(self,dataList):
        if dataList is not None:
            for data in dataList:
                self.append(data)

    # def reverse(self):
    #     prev = None
    #     current = self.head #5-6-7-8-9
    #     while(current is not None): 
    #         next = current.next 
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
     

if __name__ == "__main__":
    root = LinkedList()
    root.push(3)
    root.push(6)
    root.push(4)
    root.printList()
    root.insertAt(1,8)
    root.printList()
    root.insertValues(["car","horse","Bus"])
    root.insertAfterValue("car","cart")
    root.printList()
    root.deleteByValue(4)
    root.printList()
    root.reverse()
    root.printList()
