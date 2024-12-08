# pip install advent-of-code-data
#from aocd.models import Puzzle

# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 12345 # change this!
inputtype  = "D" # D(emo) or P(ersonal)


from aocd import submit, get_data
from itertools import count
import numpy as np
import pandas as pd
import os
from collections import deque
from helperfunctions import *
import copy

##### helperfuntions


### recurring functoins
def load_data(inputtype=inputtype): #"D","P"
    
    demodata = """190: 10 19
                    3267: 81 40 27
                    83: 17 5
                    156: 15 6
                    7290: 6 8 6 15
                    161011: 16 10 13
                    192: 17 8 14
                    21037: 9 7 18 13
                    292: 11 6 16 20"""

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data=0):
    return 0

def calc_a(a=0, b=0):
    
    return 0 # answer:     #12839601725776     too low 
    


    


def calc_b():
    return 0

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
    answer_b = calc_b()
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


