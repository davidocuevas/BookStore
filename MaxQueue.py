from SLLStack import SLLStack
from SLLQueue import SLLQueue
from DLList import DLList
import numpy as np

class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.deque = DLList()

    def add(self, x :np.object) :
        super().add(x)
        if self.deque.size() == 0:
            self.deque.add(0, x)
        else:
            while self.deque.size() != 0 and self.deque.dummy.prev.x < x:
                self.deque.remove(self.deque.n - 1)
            self.deque.add(self.deque.n, x)
        #pass

    def remove(self) -> np.object:
        if self.n == 0:
            return None
        if self.head.x == self.deque.dummy.next.next.x:
            self.deque.remove(0)
        return super().remove()
    #pass

    def max(self) -> np.object:
        if self.deque.size() == None:
            return None
        return self.deque.dummy.next.x
    #pass



