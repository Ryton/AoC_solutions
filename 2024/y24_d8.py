# pip install advent-of-code-data
#from aocd.models import Puzzle

# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 8 # change this!
inputtype  = "P" # D(emo) or P(ersonal)


from aocd import submit, get_data
from itertools import count
import numpy as np
import pandas as pd
import os
from collections import deque
from helperfunctions import *
import copy 

##### helperfuntions
solveB = False
def calc_center_and_dist(apos, bpos):
    xa,ya = apos
    xb,yb = bpos
    center = ((xa+xb)/2,(ya+yb)/2)
    deltabetw_nodes = ((xa-xb),(ya-yb))
    return center,deltabetw_nodes


def calc_antinodes(apos, bpos):
    center,deltabetw_nodes =calc_center_and_dist(apos, bpos)
    ## fix diagonal_up or down, as 
    return [(int(center[0] + deltabetw_nodes[0]*1.5),
             int(center[1] + deltabetw_nodes[1]*1.5 ) ),
             (int(center[0] - deltabetw_nodes[0]*1.5),
            int(center[1] - deltabetw_nodes[1]*1.5) )
             ]

def calc_harmonics(apos, bpos,x_max,x_min):
    center,deltabetw_nodes =calc_center_and_dist(apos, bpos)
    ## fix diagonal_up or down, as 
    
    harmpos = []
    for i in range(-150,150,1):
        X_step = deltabetw_nodes[0]*(i+ .5)
        Y_step = deltabetw_nodes[1]*(i+ .5)
        xval = int(center[0] + X_step)
        yval = int(center[1] + Y_step)
        if xval == center[0] and xval == center[0]:
            pass
        elif xval <0 or xval > x_max or yval < 0 or yval > x_max:
            pass
        else:

            harmpos.append((xval,yval))
    return harmpos


### recurring functoins
def load_data(inputtype=inputtype): #"D","P"
    
    demodata = """##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##"""

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")

    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(parsedinput=0):
    df = pd.DataFrame([[p for p in l] for l in data.splitlines()])
    #print(df)
    gridshape = np.shape(df)
    #print(gridshape)
    return df


from itertools import permutations, combinations


def calc_a(df,solveB = False):
    #print(df.values)
    symbols = np.unique(df.values)
    #print(symbols)
    gridshape = np.shape(df.values)
    antennapos = dict()
    solution = []
    for s in symbols:
        if s not in [".","#"]:
            antennapos[s]=list(zip(*np.where(df.values == s)))
        if s in ["#"]:
            solution=list(zip(*np.where(df.values == s)))
    #print(antennapos)
    list_antinodes =[]
    for ant in antennapos:
        loc =antennapos[ant]
        one_antenna_comb = list(combinations(loc,2))
        #print("combinations")
        
        for pairs in one_antenna_comb:
            if not solveB:
                antinodepos =calc_antinodes(*pairs)
            else:
                antinodepos =calc_harmonics(*pairs,x_min = 0, x_max = gridshape[0]-1)
            #print(pairs, " =>", antinodepos)
            for pos in antinodepos:
                if pos[0]>=0 and  pos[0]< gridshape[0]:
                    if pos[1]>=0 and  pos[1]< gridshape[1]:            
                        list_antinodes.append(pos)
    #print("result:")
    #print(list_antinodes)
    #print("solution:")
    #print(solution)
    return len(set(list_antinodes)) # answer:     #12839601725776     too low 
    # 439 too high...       


def calc_b(df):
    return calc_a(df,solveB = True)


## main script when file is run as script
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    parsedinput = parse(data)
    
    # timed exeution
    tic()
    answer_a= calc_a(parsedinput)
    t_a = toc()

    tic()
    answer_b = calc_b(parsedinput)
    t_b = toc()

    #printout
    part = "a"

    print("*** Demo Input *"+ "*"*14 if inputtype == "D" else "*** Personal input *"+ "*"*14)
    print(f"* Answer {part}: {answer_a}")
    
    part = "b"
    print(f"* Answer {part}: {answer_b}")
    #submit(answer_b)


    print("* CalcuationTime:   ")
    print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


