import sys
sys.path.append("../list")
from circularLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.__queue = CircularLinkedList()

    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        return self.__queue.get(0)

    def isEmpty(self):
        return self.__queue.isEmpty()

    def dequeueAll(self):
        self.__queue.clear()

    def printQueue(self):
        print("Queue from front: ", end=' ')
        for i in range(self.__queue.size()):
            print(self.__queue.get(i), end=' ')
        print()
