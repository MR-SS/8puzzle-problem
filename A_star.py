#!usr/bin/env python 

"""
8 puzzle algortim
    we have 4 condition :
        left
        right
        up 
        down
for solve this problem we need first state and goal state
we have goal state,so we need just first state.


we nedd 2 function g(n) and h(n)
g(n):number of movment to set one number in right place 
h(n):numer of misplace from the goal state

"""
#================================================
#!/usr/bin/python3
import numpy as np 


print("for add blank field add 0")
# initializing an empty matrix
matrix = []
#create matrix with user input
for i in range(3):
    row = []
    for j in range(3):
        print("add number for [",i,"][",j,"]")
        element = int(input())
        # appending the element to the 'row'
        row.append(element)
   # appending the 'row' to the 'matrix'
    matrix.append(row)
# printing the matrix
first_state =np.array(list(matrix)).reshape(3,3)
goal_state= np.arange(0,9).reshape(3,3)
#create curent_state for add current state for each child

current_state = []
current_state=first_state
print(current_state)
#defenetion h(n)

# global misplace
# misplace =0
def fscore (current_state):
    misplace = 0
    for i in range(0,3):
        for j in range(0,3):    
            if(current_state[i,j]!=goal_state[i,j]):
                misplace += 1
                print("now we have",misplace)
    return print(misplace)

fscore(current_state)
