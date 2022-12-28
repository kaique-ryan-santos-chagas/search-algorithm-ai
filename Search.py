
from Stack import Stack
from Queue import Queue

class DepthFisrt:
    
    def __init__(self, maze, initialState, goalState):
        
        self.maze = maze
        self.frontier = Stack()
        self.pathCost = 0
        self.initialState = initialState
        self.goalState = goalState
        self.solution = []
        self.explored = []
        
    def action(self, state):
        
        goalStateCoordinate = [None, None]
        
        # Find path in the maze. 
        
        if (state[1] + 1) < len(self.maze):
            
            nextStateRight = self.maze[state[0]][state[1] + 1]
            
            if nextStateRight == 2:
                goalStateCoordinate = [state[0], state[1] + 1]
                
        else:
            nextStateRight = None
        
        if (state[1] - 1) < len(self.maze):
            
            nextStateLeft = self.maze[state[0]][state[1] - 1]
            
            if nextStateLeft == 2:
                goalStateCoordinate = [state[0], state[1] - 1]
                
        else:
            nextStateLeft = None
        
        if (state[0] - 1) < len(self.maze):
            
            nextStateUp = self.maze[state[0] - 1][state[1]]
            
            if nextStateUp == 2:
                goalStateCoordinate = [state[0] - 1, state[1]]
                
        else:
            nextStateUp = None
        
        if (state[0] + 1) < len(self.maze):
            
            nextStateDown = self.maze[state[0] + 1][state[1]]
            
            if nextStateDown == 2:
                goalStateCoordinate = [state[0] + 1, state[1]]
                
        else:
            nextStateDown = None
               
        if nextStateRight == 2 or nextStateLeft == 2 or nextStateUp == 2 or nextStateDown == 2:
            
            self.goalState = goalStateCoordinate
            self.pathCost = len(self.explored)
            
            print('\n We found it!')
            print('\n Path cost: ' + str(self.pathCost))
            print('\n Goal State coordinate: ' + str(self.goalState))
            
            print()
            
            for x in range(len(self.maze)):
                for y in range(len(self.maze[x])):
                    print(self.maze[x][y], end=' ')
                print()
            
        else:
               
            if nextStateRight == 0:
                
                if state[0] >= 0 and (state[1] + 1) >= 0:
                
                    self.maze[state[0]][state[1] + 1] = '*'
                    self.frontier.push([state[0], state[1] + 1])
                    
            if nextStateLeft == 0:
                
                if state[0] >= 0 and (state[1] - 1) >= 0:
                    
                    self.maze[state[0]][state[1] - 1] = '*'
                    self.frontier.push([state[0], state[1] - 1])
                    
            if nextStateUp == 0:
                
                if (state[0] - 1) >= 0 and state[1] >= 0:
                
                    self.maze[state[0] - 1][state[1]] = '*'
                    self.frontier.push([state[0] - 1, state[1]])
                    
            if nextStateDown == 0:
                
                if (state[0] + 1) >= 0 and state[1] >= 0:
                    
                    self.maze[state[0] + 1][state[1]] = '*'
                    self.frontier.push([state[0] + 1, state[1]])
            
            print('\n Frontier: ' + self.frontier.toString())
            
            if(self.frontier.toString() == 'Stack empty.'):
                
                print('\n No solution.')
                
            else:
                self.transitionModel() 
        
        
    def transitionModel(self):
        
        state = self.frontier.getTop()
        print('\n State to explore: ' + str(state))
        
        self.explored.append(state) 
        self.frontier.pop()
        
        self.action(state)
        
    
    def startSearch(self):
        
        # Find the initial state in the maze.
        
        for x in range(len(self.maze)):
            for y in range(len(self.maze[x])):
                if self.maze[x][y] == 1:
                    print('\n Initial state found at: ' + str(x) + ', ' + str(y))
                    self.initialState = [x, y]           
        
        self.action(self.initialState)
        
        
        

class BreadthFirst:
    
    def __init__(self, maze, initialState, goalState):
        
        self.maze = maze
        self.frontier = Queue()
        self.pathCost = 0
        self.initialState = initialState
        self.goalState = goalState
        self.solution = []
        self.explored = []
        
    def action(self, state):
        
        goalStateCoordinate = [None, None]
        
        # Find path in the maze. 
        
        if (state[1] + 1) < len(self.maze):
            
            nextStateRight = self.maze[state[0]][state[1] + 1]
            
            if nextStateRight == 2:
                goalStateCoordinate = [state[0], state[1] + 1]
                
        else:
            nextStateRight = None
        
        if (state[1] - 1) < len(self.maze):
            
            nextStateLeft = self.maze[state[0]][state[1] - 1]
            
            if nextStateLeft == 2:
                goalStateCoordinate = [state[0], state[1] - 1]
                
        else:
            nextStateLeft = None
        
        if (state[0] - 1) < len(self.maze):
            
            nextStateUp = self.maze[state[0] - 1][state[1]]
            
            if nextStateUp == 2:
                goalStateCoordinate = [state[0] - 1, state[1]]
                
        else:
            nextStateUp = None
        
        if (state[0] + 1) < len(self.maze):
            
            nextStateDown = self.maze[state[0] + 1][state[1]]
            
            if nextStateDown == 2:
                goalStateCoordinate = [state[0] + 1, state[1]]
                
        else:
            nextStateDown = None
               
        if nextStateRight == 2 or nextStateLeft == 2 or nextStateUp == 2 or nextStateDown == 2:
            
            self.goalState = goalStateCoordinate
            self.pathCost = len(self.explored)
            
            print('\n We found it!')
            print('\n Path cost: ' + str(self.pathCost))
            print('\n Goal State coordinate: ' + str(self.goalState))
            
            print()
            
            for x in range(len(self.maze)):
                for y in range(len(self.maze[x])):
                    print(self.maze[x][y], end=' ')
                print()
            
        else:
               
            if nextStateRight == 0:
                
                if state[0] >= 0 and (state[1] + 1) >= 0:
                
                    self.maze[state[0]][state[1] + 1] = '*'
                    self.frontier.append([state[0], state[1] + 1])
                    
            if nextStateLeft == 0:
                
                if state[0] >= 0 and (state[1] - 1) >= 0:
                    
                    self.maze[state[0]][state[1] - 1] = '*'
                    self.frontier.append([state[0], state[1] - 1])
                    
            if nextStateUp == 0:
                
                if (state[0] - 1) >= 0 and state[1] >= 0:
                
                    self.maze[state[0] - 1][state[1]] = '*'
                    self.frontier.append([state[0] - 1, state[1]])
                    
            if nextStateDown == 0:
                
                if (state[0] + 1) >= 0 and state[1] >= 0:
                    
                    self.maze[state[0] + 1][state[1]] = '*'
                    self.frontier.append([state[0] + 1, state[1]])
            
            print('\n Frontier: ' + self.frontier.toString())
            
            if(self.frontier.toString() == 'Stack empty.'):
                
                print('\n No solution.')
                
            else:
                self.transitionModel() 
        
        
    def transitionModel(self):
        
        state = self.frontier.getFirst()
        print('\n State to explore: ' + str(state))
        
        self.explored.append(state) 
        self.frontier.pop()
        
        self.action(state)
        
    
    def startSearch(self):
        
        # Find the initial state in the maze.
        
        for x in range(len(self.maze)):
            for y in range(len(self.maze[x])):
                if self.maze[x][y] == 1:
                    print('\n Initial state found at: ' + str(x) + ', ' + str(y))
                    self.initialState = [x, y]           
        
        self.action(self.initialState)
        
        
        