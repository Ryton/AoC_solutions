# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 4

from aocd import submit, get_data
import numpy as np
import pandas as pd
import os
from helperfunctions import *

def  parse(year, day):
    output =get_data(year=year,day=day)
    #print(": ",line)
    grid = [[*line] for line in output.splitlines()]
    return  np.array(grid)

def checker(grid, pos=(0,0),direction = (1,0),word = "XMAS"):
    found = 0
    #(a,b) = pos
    (i,j) = direction
    if i == 0 and j==0:
        return 0
    else:    
        try: # if out of bounds this will fail. & if (0,0) it will fail too.
            for n,l in enumerate(word): 
                p1 = pos[0] + i*n 
                p2 = pos[1] + j*n 
                if p1 >=0 and p2 >=0: ## else it overflows...
                    if grid[p1,p2]==l: 
                        found += 1
        except:
            pass
        if found == len(word):
            return 1
        else:
            return 0


def check_MAS(grid, pos=(0,0)):
    a = pos[0]
    b = pos[1]
    
    if not(grid[a,b] in ['A']):
        pass
    else:

        #print(f"grid({a},{b}) is { grid[a,b]}")    
        w1 = "".join([grid[a+1,b+1],grid[a,b],grid[a-1,b-1]])
        w2 = "".join([grid[a-1,b+1],grid[a,b],grid[a+1,b-1]])
        
        if w1 in ["MAS","SAM"]:
            if w2 in ["MAS","SAM"]:
                #print(f"grid({a},{b}) is { grid[a,b]}")    
                #print(f"{w1},{w2} at {a},{b} is a match")
                return 1
        
        
    return 0

def calc_a(grid):
    count = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for a in range(len(grid)):
                for b in range(len(grid[0])):
                    found = checker(grid, pos=(a,b),direction=(i,j))
                    if found == 1:
                        count += found
                        #print(f" word found at pos {a},{b} direction {i},{j}")
    return count
    
    return 0

def calc_b(grid):
    count = 0
    for a in np.arange(1,len(grid)-1,1):
        for b in np.arange(1,len(grid[0])-1,1):
            found = check_MAS(grid, pos=(a,b))
            if found == 1:
                count += found
                #print(f" MAS found at pos {a},{b}")
    return count
    
    return 0
    return 0

if __name__ == "__main__":
    print(f"Day {day}")    
    tic()
    bool_exampledata = False
    if bool_exampledata:
        
        exampledata = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"
        #exampledata ="....XXMAS.\n.SAMXMS...\n...S..A...\n..A.A.MS.X\nXMASAMX.MM\nX.....XA.A\nS.S.S.S.SS\n.A.A.A.A.A\n..M.M.M.MM\n.X.X.XMASX"
        data = np.array([[*line] for line in exampledata.splitlines()])
    else:
        data = parse(year= year,day = day)
    print(np.shape(data))
    print(data, sep = "\n")
    #

    #input = parse(data)
    answer_a= calc_a(data)
    print(answer_a)
    #submit(answer_a)
    t_a = toc()
    
    tic()
    answer_b = calc_b(data)
    t_b = toc()
    print(answer_b)
    # part = "a"
    # print(f"personal answer {part}:{answer_a}")
    # print(answer_a)
    # part = "b"
    # print(f"personal answer {part}:{answer_b}")
    # submit(answer_b)


    # print("CalcuationTime:")
    # print(f"Day {day} a: {t_a:2.3f}s")
    # print(f"Day {day} b: {t_b:2.3f}s")



