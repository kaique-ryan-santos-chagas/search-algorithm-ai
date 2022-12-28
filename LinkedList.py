from Node import Node

class LinkedList:
    
    def __init__(self):
        
        self.first = None
        self.size = 0
        
    def append(self, data):
        
        if self.first != None:
            
            node = self.first
            
            while(node.next):
                node = node.next
            
            node.next = Node(data)
        
        else:
            
            self.first = Node(data)
        
        
    def isEmpty(self):
        
        if self.first == None:
            return True
        else:
            return False
        
    def getSize(self):
        
        if self.first != None:
            
            self.size = self.size + 1
            
            node = self.first
            
            while(node.next):

                self.size = self.size + 1
                node = node.next
        
            return self.size

        else:
            
            self.size = 0
            return self.size
        
    def returnList(self):
        
        if self.first != None:
            
            node = self.first
            
            list = str(node.data)
            
            while(node.next):
                node = node.next
                list =  list + ' -> ' + str(node.data)
            
            return list
        
        else:
            
            return 'List empty.'
        
        
        
        
               