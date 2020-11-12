#!/usr/bin/env python3

"""
Simple implementation of A* algorithm to solve 8 Puzzle.
It uses the sum of Manhattan distance of each number compared to where it should be in the puzzle as hirostic method.
"""
__author__ = "MR-SS"


class State(object):
	#np means the number of movement
    def __init__(self, np, moves):
        self.np = tuple(np)
        self.moves = moves

    def child(self):
#for add cordinate we can make function for each cordinate like ( def left(self): and get the state in it )
#or can define a range of matrix for add cordinate 
#like if  0(blank field)>3 we can use up cordinate .because in firt line we can't do up cordinate
        current = []
        blank = self.np.index(0)
        if blank >= 3:  # can go up
            new_state = list(self.np)
            new_state[blank] = new_state[blank - 3]
            new_state[blank - 3] = 0
            new_moves = self.moves + 'Up / '
            current.append(State(new_state, new_moves))
        if blank < 6:  # can go down
            new_state = list(self.np)
            new_state[blank] = new_state[blank + 3]
            new_state[blank + 3] = 0
            new_moves = self.moves + 'Down / '
            current.append(State(new_state, new_moves))
        if blank % 3 > 0:  # can go left
            new_state = list(self.np)
            new_state[blank] = new_state[blank - 1]
            new_state[blank - 1] = 0
            new_moves = self.moves + "Left / "
            current.append(State(new_state, new_moves))
        if blank % 3 <= 1:  # can go right
            new_state = list(self.np)
            new_state[blank] = new_state[blank + 1]
            new_state[blank + 1] = 0
            new_moves = self.moves + 'Righ / '
            current.append(State(new_state, new_moves))
        return current

    def state_print(self):
        print(f"|{self.np[0]}|{self.np[1]}|{self.np[2]}|")
        print(f"|{self.np[3]}|{self.np[4]}|{self.np[5]}|")
        print(f"|{self.np[4]}|{self.np[5]}|{self.np[6]}|")

    def __hash__(self):
        return hash(self.np)

    def __eq__(self, other):
        return self.np == other.np

    def __repr__(self):
        return "State({}), h={}, path={}".format(self.np, hirostic(self), self.moves)


def hirostic(state):
    h = 0
    for i, n in enumerate(state.np):
        h += abs(int(n / 3) - int(i / 3)) + abs(n % 3 - i % 3)
    return h

#cost= hirsotic +g   (A*+sum of movement)
def cost(state):
    return hirostic(state) + len(state.moves)

#we sorted the list and find the best child for solution with a* alogithm and pop the best child best state
def pop_best(current):
    list_current = list(current)
    list_current.sort(key=cost)
    best_state = list_current[0]
    current.remove(best_state)

    return best_state


# Algorithm got from https://datawookie.netlify.app/blog/2019/04/sliding-puzzle-solvable/
#check the current state that user added is solveble or not
def check_solvable(state):
    zero = []
    state = list(state)
    state.remove(0)
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[j] > state[i]:
                inversions += 1

    return inversions % 2 == 0


def solve(current):
    visited = set()
    while True:
        if not current:
        #need more than 31 and 'we can't create it
            raise Exception("FAILD!!")
        #pop best state and add it to visited.because we donlt want to make child with this number again
        best_state = pop_best(current)
        visited.add(best_state.np)

        h = hirostic(best_state)
        if h == 0:
            return best_state

        if len(best_state.moves) > 31:  # The hardest 8 Puzzle state takes 31 moves to solve 
            continue

        new_current = best_state.child()
        current |= set([np for np in new_current if np.np not in visited])


if __name__ == "__main__":
    while True:
        print("for add blank field add 0")
        print(" ")
        print("each number must be in rage [0,1,2,3,4,5,6,7,8] and not be Repetitious")
        print("")
        # initializing an empty matrix
        state_start = []
        for i in range(3):
            row = []
            for j in range(3):
                #get input for array from user 
                print("add number for [",i,"][",j,"]")
                element = int(input())
                if element in range(9):
                # appending the element to the 'row'
                    # row.append(element)
                    state_start.append(element)
                else:
                    raise Exception("the input number is out of range")
        # appending the 'row' to the 'state sart'
            # state_start.append(row)
        flag =0
        print("your input state is : ",state_start)
        if (check_solvable(state_start)==True):
            state = State(state_start, "")
            state.state_print()
            print("Solving...")
            flag =1
            solution = solve({state})
            print(f"Solved! {len(solution.moves)} moves: {solution.moves}")
            print()
        else:
            print("it's not sovleble")
        if(flag==1):
            import sys
            sys.exit()

#use this site for fint input state or see the unput state have answer or not https://tristanpenman.com/demos/n-puzzle/