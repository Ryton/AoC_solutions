# helperfunctions for AoC . Some found online , other selfdefined.

## all imports for main file.
from aocd import submit, get_data
from itertools import count
import numpy as np
import pandas as pd
import os
from collections import deque
import copy

import time

def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True, what=""):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    #if tempBool:
    #    print( f"Time {what}: %f seconds.\n" %tempTimeInterval )
    return tempTimeInterval

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)
