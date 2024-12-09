# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 5

from aocd import submit, get_data
import numpy as np
import pandas as pd
import os
import copy
from helperfunctions import *
from collections import deque 

def parse():    

    ## manual split
    pairlist_df =pd.read_csv("2024\d5_pairs.txt",header=None)
    pairlist_ = []
    for pair in pairlist_df.values:
        #print(pair)
        strpair=pair[0].split("|")
        pairlist_.append((int(strpair[0]),int(strpair[1])))

    ## manual split
    with open('2024\d5_order.txt') as f:        
        order_containerlist_ = [list(map(int,line.split(","))) for line in f]
    
    return pairlist_,order_containerlist_

def buildmanual(pairlist_):
    order_container = deque()
    bool_allsorted = True

    #print(counter, order_container)
    for (a,b) in  pairlist_:    
        smallerns = [checka if checkb == b else None for (checka,checkb) in pairlist_]
        biggernrs = [checkb if checka == a else None for (checka,checkb) in pairlist_]

        
        if not (b in order_container):
            if len(smallerns)==0:
                order_container.append(b)
            else:
                idx_smaller = []
                for v in smallerns:
                    if v in order_container:
                        idx_smaller.append(order_container.index(v))
                if len(idx_smaller)>0:
                    minb_index=max(idx_smaller)
                else:
                    minb_index = 0
                order_container.insert(minb_index+1,b)

        if not (a in order_container):
            if len(biggernrs)==0:
                order_container.append(a)
            else:
                idx_bigger = []
                for v in biggernrs:
                    if v in order_container:
                        idx_bigger.append(order_container.index(v))
                if len(idx_bigger)>0:
                    maxa_index=min(idx_bigger)
                else:
                    maxa_index = 0
                order_container.insert(maxa_index,a)

    return(order_container)


def buildmanual_checking(pairlist_,order_container):
    #order_container = deque()
    
    bool_allsorted = False
    counter = 0
    #order_container = []
    while not bool_allsorted:

        bool_allsorted = True
        counter +=1
        #print(counter, order_container)
        for (a,b) in  pairlist_:    
            if (a in order_container) and (b in order_container):
                posa  = order_container.index(a)
                posb =  order_container.index(b)

                if posa < posb:
                    pass  # only if all here ,pass
                else:
                    
                    lastcase =f"swap. moved {a},{b} to {posa},{posb}"
                    bool_allsorted = False    
                    #swap them
                    order_container.remove(b)
                    order_container.insert(posa,b) # move to a pos
                    order_container.remove(a)
                    order_container.insert(posb,a)
                    
                    
            elif (a in order_container) and not (b in order_container):
                lastcase = "new"
                order_container.append(b)
                bool_allsorted = False    
            elif not (a in order_container) and (b in order_container):        
                lastcase = "new a"
                order_container.insert(0, a)
                bool_allsorted = False    
            else: # neither in it: a up front, B in back
                lastcase = "new b"
                order_container.insert(0 , a)
                order_container.append( b)
                bool_allsorted = False    

        if bool_allsorted:
            print(order_container)
        else:
            print(counter,":", lastcase)
        
    return(order_container)

def eval_pages(rightorder_container, testcase= [23,34,33]):
    indiches = [ rightorder_container.index(t) for t in testcase]

    if sorted(indiches) == indiches:
        print("indiches",indiches , "OK")
        return testcase[len(indiches)//2]
    else:
        print("indiches",indiches , "NOT OK")
        return 0
def builddict(pairlist_):
    pairdict = dict()
    for (a,b) in pairlist_:
        pairdict[a]  =[ checkedb if checkeda == a else None for (checkeda,checkedb) in pairlist_ ]
    return pairdict
def checkone(pairlist_, order_container= [12,24,43]):

    pairdict = builddict(pairlist_)
    status = "OK"
    for v in order_container: # loop every item.
        if v in pairdict: # if there is an order_container defined (after).
            requiredorder_container= pairdict[v]
            fromindex =order_container.index(v)
            for p in order_container[fromindex:]: # check all pages after it
            
                if requiredorder_container.index(p) > fromindex: # should be met => OK.
                    pass
                else: 
                    status = "fails"
    if status == "OK":
        return 1
    else:
        return 0 #fails
            



def calc_a(pairlist_,order_containerlist_):
    
    return sum([checkone(pairlist_, order_container)  for order_container in order_containerlist_])

def calc_b(personalinput):  
    return 0

if __name__ == "__main__":
    print(f"Day {day}")    
    
    tic()
    
    
    
    #f.read():
    pairlist_,order_containerlist_  = parse()
    
    print("pairlist:",pairlist_)
    print("order_containerlist:",order_containerlist_)



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


