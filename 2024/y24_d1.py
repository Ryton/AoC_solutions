# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 1

from aocd import submit, get_data
from itertools import count
import numpy as np
import pandas as pd
import os
from helperfunctions import *
filename_input = f"\\data\\input_y{year-2000}_d0{day:1d}.txt"

def  parse(data):
    l1,l2 = [],[]
    for line in str.split(data,sep="\n"):
        #print(line)
        i1,i2=str.split(line, sep="   ")
        l1.append(int(i1))
        l2.append(int(i2))

    print(np.shape(l1))
    print(np.shape(l2))

    l1= np.array(l1).astype(int)
    l2= np.array(l2).astype(int)
    return [l1, l2]

def calc_a(l1,l2):
    l1.sort()
    l2.sort()
    return sum(np.abs(l1-l2))

from collections import Counter
def calc_b(l1,l2):
    #d1 =Counter(l1)
    d2 =Counter(l2)
    #print(d2)
    s = 0
    for k in l1:
        aval = d2.get(k)
        #print(aval)
        if aval is not None:
            s += k * aval
    return s

if __name__ == "__main__":
    print(f"Day {day}")
    
    tic()
    data = get_data(year= year,day = day)
    l1,l2 = parse(data)
    answer_a= calc_a(l1,l2)
    #submit(answer_a)
    t_a = toc()
    
    tic()
    answer_b = calc_b(l1,l2)
    t_b = toc()

    part = "a"
    print(f"personal answer {part}:{answer_a}")
    print(answer_a)
    part = "b"
    print(f"personal answer {part}:{answer_b}")
    submit(answer_b)


    print("CalcuationTime:")
    print(f"Day {day} a: {t_a:2.3f}s")
    print(f"Day {day} b: {t_b:2.3f}s")


