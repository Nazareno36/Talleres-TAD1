
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

    def is_in_list(self,value):
        current_node = self.head
        found = False
        while current_node != None and (not found):
            found = current_node.value == value
            current_node = current_node.next
        return found
    
    def push_back(self, value):
        if(self.is_in_list(value)): return 'repited value'
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.len +=1
        return 'succesful'
    
    def push_back_v2(self, value):
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
        if(self.is_in_list(value)): return 'repited value'
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
        self.len +=1
        return 'succesful'
    
    def unshift_v2(self, value):
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
            removed_node = None
            self.head.previous = None
            self.len-=1
            return 'succesful'
        return 'Empty List'
    
    def pop_node(self):
        if self.len == 1:
            self.head = None
            self.tail = None
            self.len-=1
            return 'succesful'
        elif self.head != None:
            self.tail = self.tail.previous
            self.tail.next = None
            self.len-=1
            return 'succesful'
        return 'Empty List'
    
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
        if(self.is_in_list(value)): return 'repited value'
        node = self.get_node_at(index)
        if node != None:
            node.value = value
            return 'Succesful'
        else:
            return 'Index out of range'
    
    def update_value_square(self,index,value):
        node = self.get_node_at(index)
        if node != None:
            if  node.previous != None and node.previous.value == pow(value,0.5):
                node.value = value
                return 'Succesful'
            else:
                return 'No es el cuadrado del numero anterior'
        else:
            return 'Index out of range'
    
    def remove_node(self,index):
        if index == 1:
            return self.shift_node()
        elif index == self.len:
            return self.pop_node()
        else:
            removed_node = self.get_node_at(index)
            if removed_node != None:    
                removed_node.previous.next = removed_node.next
                removed_node.next.previous = removed_node.previous
                removed_node = None
                self.len-=1
                return 'succesful'
            else:
                return 'Index out of range'
    
    def insert_node(self,index,value):
        if(self.is_in_list(value)): return 'repited value'
        if index == 1:
            return self.unshift(value)
        elif index == self.len+1:
            return self.push_back(value)
        else:
            current_node = self.get_node_at(index)
            if current_node != None:
                new_node = self.Node(value)    
                current_node.previous.next = new_node 
                current_node.previous = new_node
                self.len+=1
                return 'succesful'
            else:
                return 'Index out of range'
    
    def insert_node_v2(self,index,value):
        if index == 1:
            self.unshift_v2(value)
        elif index == self.len+1:
            self.push_back_v2(value)
        else:
            current_node = self.get_node_at(index)
            if current_node != None:
                new_node = self.Node(value)    
                current_node.previous.next = new_node 
                current_node.previous = new_node
                self.len+=1
            else:
                return 'Index out of range'
    
    def reverse(self):
        counter = 1
        while counter <  self.len:
            self.insert_node_v2(counter,self.tail.value)
            self.pop_node()
            counter+=1

    def especial_reverse(self):
        counter = 1
        while counter <  self.len:
            self.insert_node_v2(counter,pow(self.tail.value,0.5))
            self.pop_node()
            counter+=1