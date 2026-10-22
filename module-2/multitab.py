#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math

def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
    None
    """
    assert (type(n) is int) and (n > 0), "n must be positive integer"

    for row in range(1, n+1):                 #loop through rows 1 to n
        for col in range(1, n+1):             #loop through columns 1 to n
            print(f"{row*col:4d}", end="")    #multiply row and column, 4 char wide, no newline
        print()                                #newline after each row

    return None

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)