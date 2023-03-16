from collections import deque
import time
import threading

class Queue: 
    def __init__(self):
        self.buffer = deque()
    
    def enque(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)


queue = Queue()

def orderFood(arr):
    for a in arr:
        time.sleep(0.5)
        queue.enque(a)
        print(a+ ":: Order Placed")

def orderDone():
    time.sleep(1)
    while queue.size() != 0:
        time.sleep(1)
        order = queue.dequeue()
        print(order+ ":: Done")

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=orderFood,args=(orders,)) 
    t2=threading.Thread(target= orderDone) 
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print("Resturant close::)")
