from Search import DepthFisrt
from Search import BreadthFirst

maze = [[4, 3, 4, 20, 8, 15], [0, 0, 2, 23, 9, 10], [0, 4, 7, 12, 20, 3], [0, 1, 0, 0, 4, 9], [0, 0, 0, 0, 0, 15]]

print('\n Search Algorithm from CS50 AI Harvard University Course ')
print(' ======================================================= ')
print()

print('Algorithms')
print('==========')
print()

print('1 - Depth Fisrt Search')
print('2 - Breadth First Search')
print()

option = input('Digit the number of options: ')
print()

if option == '1':
    
    initialState = input('Digit the Initial State Number: ')
    goalState = input('Digit the Goal State Number: ')

    depthFirst = DepthFisrt(maze, initialState, goalState)
    depthFirst.startSearch()
    
if option == '2':
    
    initialState = input('Digit the Initial State Number: ')
    goalState = input('Digit the Goal State Number: ')

    breadthFirst = BreadthFirst(maze, initialState, goalState)
    breadthFirst.startSearch()