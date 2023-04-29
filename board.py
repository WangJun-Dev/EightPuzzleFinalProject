#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3 * r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c


    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """returns a string representation of a Board object"""
        br = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    br += '_'
                else:
                    br += self.tiles[r][c]
                br += ' '
            br += '\n'
        return br
    
    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction in which the
        blank should move, decide if the move is possible return true or false, and that
        attempts to modify the contents of the called Board object accordingly"""
        if direction == 'up':
            if self.blank_r != 0:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
                self.blank_r -= 1
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
            else:
                return False
        elif direction == 'down':
            if self.blank_r != 2:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
                self.blank_r += 1
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
            else:
                return False
        elif direction == 'right':
            if self.blank_c != 2:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
                self.blank_c += 1
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
            else:
                return False
        elif direction == 'left':
            if self.blank_c != 0:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
                self.blank_c -= 1
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
            else:
                return False
        else:
            return False
        
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the called object (i.e., of the object represented by self)."""
        digitstr = ''
        for r in self.tiles:
            for c in r:
                digitstr += c
        new_board = Board(digitstr)
        return new_board        
    
    def digit_string(self):
        """creates and returns a string of digits that corresponds to the
        current contents of the called Board object's tiles attribute."""
        digit_str = ""
        for r in range(3):
            for c in range(3):
                tile = self.tiles[r][c]
                if tile == "_":
                    digit_str += "0"
                else:
                    digit_str += tile
        return digit_str
            
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object that are not where they should be in the goal state"""
        result = -1
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    result += 1
        return result
        
    def __eq__(self, other):
        """compare two Board objects, return true if the same, else returns false"""
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
        



