
class DoubleLinkedList:
    
    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0