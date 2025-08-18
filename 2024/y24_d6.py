# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 6
EVALLENGTH = 6161+5  # = lowest acceptable bound in my example 
            # 20999 ## less conservative bound 1 min
            # 99999 very conservative bound, 3 mins
from aocd import submit, get_data
import numpy as np
import pandas as pd
import os
from helperfunctions import *
import copy 
from tqdm import tqdm

def  parse(data):
    #print(np.shape(data))
    grid=np.array([[l for l in line] for line in data.split()])

    return grid

def move_one(grid, pos=(0,0), dirindex = 2):
    dirs = [(-1,0), (0,1),(1,0),(0,-1)]
    step =dirs[dirindex]

    nextmoveallowed =False
    while not(nextmoveallowed):
        nextpos= (pos[0]+step[0],pos[1]+step[1] )        
        
        if (nextpos[0]< 0) or (nextpos[0] >=np.shape(grid)[1])  or  (nextpos[1]<0) or (nextpos[1] >=np.shape(grid)[0]):
            nextmoveallowed=False    # beyond edge, skip   
            nexttile ="N"
            #print(f"nextmove beyond grid? {nextpos}")
            return [pos,-1]
        else:
            try:
                nexttile =  grid[nextpos[0],nextpos[1]]
                nextmoveallowed = not (nexttile in ["#","E","O"]) # [".","^","X","?"])
                
            except:
                nexttile ="?"
                print("shouldntoccur?")
                pass

        #if this direction is not acceptable, update direction and step
        if not(nextmoveallowed): 
                dirindex = (dirindex +1 ) % 4 #eval next direction.
                step = dirs[dirindex]
                #print(f"failed to take {pos[0]+step[0]},{pos[1]+step[1]},nexttile = {nexttile}")

    if nextmoveallowed:
        #print(f"possible: {pos[0]+step[0]},{pos[1]+step[1]}")
        #print(nextpos)
        step = dirs[dirindex]
        nextpos= (pos[0]+step[0],pos[1]+step[1] )  
        return [nextpos,dirindex]

def calc_a(grid,BOOL_activate_loopdetection =False):
    #print(np.shape(grid))
    findpos = np.where(grid=="^")

    currpos = (int(findpos[0][0]),int(findpos[1][0]))
    currdirindex = 0 

    path = []
    path.append(currpos)
    #print(currpos,currdirindex)
    
    pathset= set()
    for i in range(EVALLENGTH):
            
        [nextpos,nextdirindex] = move_one(grid, pos=currpos, dirindex = currdirindex)
        
        if BOOL_activate_loopdetection:
            if (nextpos,nextdirindex) in pathset:
                return [] #loopie
            else:
                pathset.add((nextpos,nextdirindex))
        [currpos,currdirindex] = [nextpos,nextdirindex]

        if currdirindex==-1: # goes outside bound.
            break
        
            
        path.append(currpos)
        

        #print(f"move {i}:{currpos},direction{currdirindex}")
        grid[currpos]='X' # been there.
        


    #print(grid)
    #print(set(path))
    #print(f"path length: {len(path)}")
    return path
    


def calc_b(stargrid,normalpath,BOOL_activate_loopdetection=False):
    #naive method.
    #print(np.shape(stargrid))
    startpos = np.where(stargrid=="^")
    n_loops = 0
    maxlength =0
    #with alive_bar(len(normalpath)) as bar:  # your expected total
        
    #for n,(x_obst,y_obst) in enumerate(normalpath):
    for n in tqdm(range(len(normalpath))):
        (x_obst,y_obst) = normalpath[n]
        inputgrid = copy.deepcopy(startgrid)
        if not(startpos== (x_obst,y_obst)):
            #print(f" pos of new obj ({x_obst},{y_obst})")
            inputgrid[x_obst,y_obst]="O" #add object in grid
            #print(inputgrid)
        path = calc_a(inputgrid,BOOL_activate_loopdetection =BOOL_activate_loopdetection) # # for now, slower, work in progress)
        #print(f"progress: val {n}/{len(normalpath)}: Eval obst at ({x_obst},{y_obst}):Answ so far:{n_loops}).pathlength {len(path)}")
        #print(f"{n/len(normalpath)*100:2.2f}%",)
        if BOOL_activate_loopdetection:
            if len(path)==0:
                n_loops +=1 
        else:
            if len(path) >= EVALLENGTH-1 :
                n_loops +=1
            else:
                maxlength = max(maxlength,len(path))
            print(f"max length of cycle in my example: {maxlength}")
    return n_loops

if __name__ == "__main__":
    print(f"Day {day}")    
    tic()
    bool_exampledata = False
    if bool_exampledata:
        data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
        #exampledata ="....XXMAS.\n.SAMXMS...\n...S..A...\n..A.A.MS.X\nXMASAMX.MM\nX.....XA.A\nS.S.S.S.SS\n.A.A.A.A.A\n..M.M.M.MM\n.X.X.XMASX"
        
    else:
        data = get_data(year= year,day = day)
        
    #
    
    startgrid = parse(data)
    grid = copy.deepcopy(startgrid)
    #print(grid)
    #print(np.shape(grid))
    
    
    path= calc_a(grid)
    
    #print(path)
    answer_a =len(set(path))
    print(f"answer_a: {answer_a}")
    #submit(answer_a)
    t_a = toc()
    
    tic()
    print("calculating answer b (slow!):")
    answer_b = calc_b(startgrid,list(set(path)),BOOL_activate_loopdetection = True)
    t_b = toc()
    
    print(f"answer_b: {answer_b}")
    # part = "a"
    # print(f"personal answer {part}:{answer_a}")
    # print(answer_a)
    # part = "b"
    # print(f"personal answer {part}:{answer_b}")
    # submit(answer_b)


    # print("CalcuationTime:")
    # print(f"Day {day} a: {t_a:2.3f}s")
    # print(f"Day {day} b: {t_b:2.3f}s")



