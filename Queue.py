from Node import Node

class Queue:
    
    def __init__(self):
        
        self.first = None
        self.size = 0
    
    def isEmpty(self):
        
        if self.first == None:
            return True
        else:
            return False
    
    def append(self, data):
        
        node = Node(data)
        
        if self.isEmpty():
            self.first = node
        else:
            firstNode = self.first
            
            while(firstNode.next):
                firstNode = firstNode.next
                
            firstNode.next = node
            
    def pop(self):
        
        if self.isEmpty():
            return 'Queue empty'
       
        self.first = self.first.next
    
    def getFirst(self):
        
        if self.isEmpty():
            return 'Queue empty.'
        
        return self.first.data
    
    def toString(self):
        
        node = self.first 
        
        if self.isEmpty():
            return 'Queue empty.'
        
        queue = str(node.data)
        
        while(node.next):
            queue = queue + ' -> ' + str(node.next.data)
            node = node.next
        
        return queue