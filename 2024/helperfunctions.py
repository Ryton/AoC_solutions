# helperfunctions for AoC . Some found online , other selfdefined.

## all imports for main file.
from aocd import submit, get_data
from itertools import count
import numpy as np
import pandas as pd
import os
from collections import deque
import copy
from collections import Counter
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

class Map(dict):
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    if isinstance(v, dict):
                        v = Map(v)
                    if isinstance(v, list):
                        self.__convert(v)
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, dict):
                    v = Map(v)
                elif isinstance(v, list):
                    self.__convert(v)
                self[k] = v

    def __convert(self, v):
        for elem in range(0, len(v)):
            if isinstance(v[elem], dict):
                v[elem] = Map(v[elem])
            elif isinstance(v[elem], list):
                self.__convert(v[elem])

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]




def floodfill(grid,start=(0,0),obstructed_value = 9999,wallvalue = -1):
    
    gridsize = np.shape(grid)+ np.array([2,2]) #with walls.
    nrows, ncols = np.shape(grid)
    max_tries = np.max([obstructed_value,nrows*ncols])

    # naive, visit them all again... but only need to re-visit ones next to values that have been updated.
    #for n in np.arange(0,max_tries):
    n = 0
    if 1: #
        if n ==0:
            # init  surrounding 
            expandgrid = np.ones(gridsize)*max_tries
            expandgrid[0,:]  =  max_tries*2 +1
            expandgrid[-1,:]  =  max_tries*2 +1
            expandgrid[:,0]  =  max_tries*2 +1
            expandgrid[:,-1]  =  max_tries*2 +1

            tovisit_again = [] ##only visit again if adj was updated!
            possiblepath = []
            for a in np.arange(1,nrows+1):
                for b in np.arange(1,ncols+1):
                
                    if grid[a-1,b-1]<  0 :
                        expandgrid[a,b] = max_tries +1
                    else:
                        possiblepath.append(copy.copy((int(a),int(b))))
            expandgrid[start[0]+1,start[1]+1]= 0
            #print(possibleroute)
            # iterate over all positions.

            # go over them once!    

            a,b= start+np.array([1,1])
            tovisit_again = [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]
            next_list = []
        
        # iterate till len_tovisit_again <0
        
        while ((len(tovisit_again)>0) and n<max_tries):
            #print("listlength",len(tovisit_again))
            #print(tovisit_again)
            n = n+1
            for loc in tovisit_again:
                a,b = loc
                
                #grid3x3 = expandgrid[a-1:+a+1,b-1:b+1] #also diag ok
                try:
                    grid_cross = [expandgrid[a-1,b],expandgrid[a+1,b],expandgrid[a,b-1],expandgrid[a,b+1]]
                except: 
                    grid_cross = [obstructed_value]
                    print("grid cross generation failed for {a},{b}, with expanded grid size {np.shape(expandgrid)}")

                """ ## too slow
                    grid_cross = []
                    for thesetuples  in [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]:
                    try:
                        grid_cross.append(expandgrid[thesetuples])
                    except:
                        print("grid cross generation failed for {a},{b}")

                """
                minval = np.min(grid_cross)

                
                isedge = (a ==0 or a>nrows or b ==0 or b>ncols)
                if not(isedge):
                    iswall = (grid[a-1,b-1] ==wallvalue)
                else:
                    iswall = isedge 

                if (expandgrid[*loc] > minval+1) and not(iswall) and not(isedge):  
                    expandgrid[*loc] = minval+1
                    for adj in [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]:
                        #print("adj", adj)
                        a,b = adj
                        isedge = (a ==0 or a>nrows or b ==0 or b>ncols)
                        if not(isedge):
                            iswall = ( (grid[a-1,b-1])==wallvalue)
                        else:
                            iswall = isedge
                            
                        if iswall or isedge: # then  a wall or side  (==> skip those
                            pass
                        else:
                            #print("adj", adj)
                            #print("val", expandgrid[*adj])
                            #print("minval = ", minval) 
                            if expandgrid[*adj]>(minval+1):
                                next_list.append(adj)
                                
                
            #remove duplicates
            tovisit_again = copy.copy (next_list)
            next_list = [] 
    #print(expandgrid)
    return expandgrid



from collections import deque

import numpy as np
from collections import deque

def bfs_shortest_path_np(grid: np.ndarray, start: tuple, goal: tuple):
    rows, cols = grid.shape
    visited = np.zeros_like(grid, dtype=bool)
    queue = deque([(start, [start])])  # (current_position, path_so_far)

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx, ny] and grid[nx, ny] == 0:  # 0 = walkable
                    visited[nx, ny] = True
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # No path found
