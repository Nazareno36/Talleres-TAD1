from os import remove
from colorama import*
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
    
    def print_values(self):
        current_node = self.head
        while current_node != None:
            Fore.YELLOW
            print(current_node.value)
            current_node = current_node.next
        print(Fore.CYAN + f'longitud = {self.len}')
    
    def push_back(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.len +=1
    
    def unshift(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
        self.len +=1
    
    def shift_node(self):
        if self.head != None:
            removed_node = self.head
            self.head = removed_node.next
            removed_node.next = None
            self.head.previous = None
            self.len-=1
    
    def pop_node(self):
        if self.len == 1:
            self.head = None
            self.tail = None
            self.len-=1
        elif self.head != None:
            self.tail = self.tail.previous
            self.tail.next = None
    
    def get_node_at(self,index):
        if index == self.len:
            return self.tail
        if index <= 0 or index > self.len:
            return None
        else:
            current_node = self.head
            counter = 1
            while counter != index:
                current_node = current_node.next
                counter+=1
            return current_node
    
    def get_value_at(self,index):   
        node = self.get_node_at(index)
        if node != None:
            return node.value
        else:
            return 'Index out of range'
    
    def update_value(self,index,value):
        node = self.get_node_at(index)
        if node != None:
            node.value = value
        else:
            return 'Index out of range'
    
    def remove_node(self,index):
        if index == 1:
            self.shift_node()
        elif index == self.len:
            self.pop_node()
        else:
            removed_node = self.get_node_at(index)
            if removed_node .next != None:    
                removed_node.previous.next = removed_node.next
                removed_node.next.previous = removed_node.previous
                removed_node = None
            else:
                return 'Index out of range'
    
    def insert_node(self,index,value):
        if index == 1:
            self.unshift(value)
        elif index == self.len+1:
            self.push_back(value)
        else:
            current_node = self.get_node_at(index)
            if current_node .next != None:
                new_node = self.Node(value)    
                current_node.previous.next = new_node 
                current_node.previous = new_node
            else:
                return 'Index out of range'
    
    def reverse(self):
        counter = 1
        while counter <  self.len:
            self.insert_node(counter,self.tail.value)
            self.pop_node()
            counter+=1
    
