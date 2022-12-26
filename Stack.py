from Node import Node

class Stack:
    
    def __init__(self):
        
        self.size = 0
        self.top = None
        
    
    def push(self, data):
        
        if self.isEmpty():
            
            self.top = Node(data) 
        
        else:
            
            node = self.top 
            self.top = Node(data)
            self.top.next = node  
        
        
    def pop(self):
        
        if self.isEmpty():
            
            return 'Stack empty.'
        
        else:
            self.top = self.top.next
                
        
    def isEmpty(self):
        
        if self.top != None:
            return False
        else:
            return True
        
    
    def toString(self):
        
        if self.isEmpty():
            
            self.size = 0
            return "Stack empty."
        
        else:
            
            node = self.top
            stack = str(node.data)        

            while(node.next):
                stack = stack + ' -> ' + str(node.next.data)
                node = node.next
                   
            return stack
        
        
    def getTop(self):
        
        return self.top.data