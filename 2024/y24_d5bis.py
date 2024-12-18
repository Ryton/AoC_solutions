# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 5
inputtype = "P"

from aocd import submit, get_data
import numpy as np
import pandas as pd
import os
import copy
from helperfunctions import *
from collections import deque 

def parse(inputtype="D"):    

    ## manual split
    pairlist_ = []
    if inputtype=="P":
        pairlist_df =pd.read_csv("2024\d5_pairs.txt",header=None)
    else:
        pairdata = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""
        pairlist_df =pd.DataFrame(pairdata.splitlines())
        
    pairlist_ = []
    for pair in pairlist_df.values:
        #print(pair)
        strpair=pair[0].split("|")
        pairlist_.append((int(strpair[0]),int(strpair[1])))

    ## manual split
    if inputtype=="P":
        with open('2024\d5_order.txt') as f:        
            order_containerlist_ = [list(map(int,line.split(","))) for line in f]
    else:
            data = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
            order_containerlist_ = [list(map(int,line.split(","))) for line in data.splitlines()]

        

    return pairlist_,order_containerlist_

def checkone(alist,pairlist_):
    for n in range(len(alist)-1):
        for m in np.arange(n, len(alist)):
            if (alist[m],alist[n]) in pairlist_:
                #print(f"violates {(n,m)}")
                return False
            
    return True

def checkandfix(alist,pairlist_):
    newlist = copy.deepcopy(alist)
    while not(checkone(newlist,pairlist_)):
        
        for n in range(len(newlist)-1):
            for m in np.arange(n, len(newlist)):
                if (newlist[m],newlist[n]) in pairlist_:
                    tempcopy = newlist.pop(n)
                    newlist.append(tempcopy)
                    #print(f"violates {(n,m)}")
        
    return newlist



def calc_a(pairlist_,order_containerlist_):
    summed  = 0
    for order in order_containerlist_:
        if checkone(order,pairlist_):
           #print( f"{order} passes")
           summed += order[int(len(order)//2)] #  element nr 1 in a row of len 3; el 2 in row of 5
        else:
            #print( f"{order} FAIL")
            pass
    return summed

from itertools import permutations
def calc_b(personalinput):  
    summed_B  = 0
    print("part B")
    for order in order_containerlist_:
        if checkone(order,pairlist_):
           #print( f"{order} passes thus ignored")
           pass
        else:
            #print( f"{order} FAILED thus reordered")
            newconfig  = checkandfix(order,pairlist_)
            #print( f"{newconfig} is new list")
            summed_B += newconfig[int(len(newconfig)//2)] #  element nr 1 in a row of len 3; el 2 in row of 5
            

    return summed_B
    
    return 0

if __name__ == "__main__":
    print(f"Day {day}")    
    
    tic()
    
    
    
    #f.read():
    pairlist_,order_containerlist_  = parse(inputtype=inputtype)
    
    #print("pairlist:",pairlist_)
    #print("order_containerlist:",order_containerlist_)



    #parse(personalinput)
    answer_a= calc_a(pairlist_,order_containerlist_)
    
    t_a = toc()
    
    tic()
    answer_b = calc_b(input)
    t_b = toc()

    part = "a"
    print(f"personal answer {part}: {answer_a}")
    #submit(answer_a)
    #print(answer_a)
    part = "b"
    print(f"personal answer {part}: {answer_b}")
    #submit(answer_b)


    print("CalcuationTime:")
    print(f"Day {day} a: {t_a:2.3f}s")
    print(f"Day {day} b: {t_b:2.3f}s")


