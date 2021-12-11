# https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue:

    def __init__(self, k: int):
        self.q : list = [4000 for i in range(k)]
        self.front : int = 0      
        self.rear : int = 0
        self.len : int = k

    def enQueue(self, value: int) -> bool:
        if not(self.isEmpty()):
            if self.isFull():
                return False
        self.q[self.rear] = value
        self.rear += 1
        self.rear %= self.len     
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front] = 4000
        self.front += 1
        self.front %= self.len      
        return True

    def Front(self) -> int:
        if self.q[self.front] == 4000:
            return -1
        else:
            return self.q[self.front] 
        
    def Rear(self) -> int:   
        if self.isEmpty():
            return -1
        else:
            return self.q[(self.rear+self.len-1)%self.len]                  

    def isEmpty(self) -> bool:
        if sum(self.q) == 4000*self.len:
            return True
        else:
            return False        

    def isFull(self) -> bool:
        if self.front == self.rear:
            return True
        else:
            return False
            


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(496)
print(obj.enQueue(255))
print(obj.enQueue())
print(obj.enQueue())
print(obj.isFull())
print(obj.enQueue(37))
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()