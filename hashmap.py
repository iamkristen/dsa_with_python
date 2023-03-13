class Node:
    def __init__(self,key,value,next,prev) -> None:
        self.key= key
        self.value = value
        next = next
        prev = prev

class HashMap:
    def __init__(self,key,value) -> None:
        self.head= Node()