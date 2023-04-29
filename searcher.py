#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    
    def __init__(self, depth_limit):
        """constructs a new Searcher object by initializing an attribute states for the Searcher‘s list of untested
            states, an attribute num_tested that will keep track of how many states the Searcher tests, an attribute
            depth_limit that specifies how deep in the state-space search tree the Searcher will go
        """
        self.states = []    
        self.num_tested = 0 
        self.depth_limit = depth_limit  

    def add_state(self, new_state):
        """takes a single State object called new_state and adds it to the Searcher‘s list of untested states
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """takes a State object called state and returns True if the called Searcher should add state to its list of untested states, and False otherwise.
        """
        if state.creates_cycle() == True:
            return False
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        return True
        
    def add_states(self, new_states):
        """takes a list State objects called new_states, and that processes the elements of new_states one at a time as follows
        """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified initial state init_state and ends when the goal 
            state is found or when the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        
        while len(self.states) != 0:
            s = self.next_state() 
            self.num_tested += 1  
            
            if s.is_goal() == True: 
                return s  
            else:
                self.add_states(s.generate_successors())
        return None
    

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ perform breadth-first search (BFS) instead of random search
    """

    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher. Rather than choosing
        at random from the list of untested states, this version of next_state should follow FIFO 
        (first-in first-out) ordering – choosing the state that has been in the list the longest. 
        """
        s = self.states[0]  
        self.states.remove(s)  
        return s

class DFSearcher(Searcher):
    """perform depth-first search (DFS) instead of random search
    """
    def next_state(self):
        """ chooseing the next state to be tested from the list, removing it from the
            list and returning it
        """
        s = self.states[-1]  
        self.states.remove(s)  
        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###


