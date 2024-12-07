# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 7

from aocd import submit, get_data
from itertools import count
import numpy as np
import pandas as pd
import os
from collections import deque
from helperfunctions import *
import copy

def eval_one(current, inputdeque, operator):
    localdeque = copy.deepcopy(inputdeque)
    if len(localdeque) == 0:
        value = localdeque
        localdeque = []
    else:
        value = localdeque.popleft()
    return [operator(current,value),localdeque]

#fastish but failz on userinput
def recurse_eval_next(level,current, nextdeque, operatorlist, answer):
    items_to_go = len(nextdeque)
    if items_to_go == 0:
        return (current == answer)
    else:
        #print(items_to_go, "nrs to go")
        resultslist = []
        for o in operatorlist:
            #print("level",level,"apply", o, "from" ,current, "to",nextdeque)
            [newresult,dequetopass] = eval_one(current,nextdeque, o) # here you pop nextdeque, will shorte, one.
            
            if recurse_eval_next(level+1,newresult, dequetopass, operatorlist , answer):

                return True  #can skp the rest then
    
        
    
    return False #else fail


def dosum(a,b):
    return a+b
def doprod(a,b):
    return (a*b)

import itertools as it
def list_all_permutations(operatorlist=[dosum,doprod],n_steps = 4):
    return list(it.product(operatorlist, repeat=n_steps))
        
            
        
    return False #else fail

import sys
sys.set_int_max_str_digits(100002)


p1operators = [dosum, doprod]

def  parse(data):
    answer_to_terms = dict()
    for line in data.splitlines():
        #print(line)
        
        alist =line.split()
        answer = int(alist[0][0:-1])
        #print(alist)
        answer_to_terms[answer] = [np.int64(a) for a in alist[1:]]
    return answer_to_terms

def calc_a(answer_to_terms, p1operators):
    
    tot = 0
    if 0:
        # works for example, not own data
        for answer in  answer_to_terms: #keys
            outputdeque = deque(answer_to_terms[answer])
            level = 0
            if recurse_eval_next(level,0, outputdeque, p1operators,answer):
                print("found a match for ",answer)
                tot += answer
            else:
                print("no sol for ",answer)
        return tot # answer:     #12839601725776     too low 
    
    else:
        for answer in  answer_to_terms: #keys
            solved= False
            startdeque = deque(answer_to_terms[answer])
            # print(outputdeque)
            # print(n_operations)
            
            
            n_operations = len(startdeque)-1
            poss_operations = list(list_all_permutations(operatorlist=[dosum,doprod],n_steps = n_operations))
            # print(current)
            # print(outputdeque)
            
            for operationslist in poss_operations:
                #print(Os)
                localdeque = copy.deepcopy(startdeque)
                result = localdeque[0]
                #print(operationslist)
                for n,o in enumerate(operationslist):
                    result = o(result,localdeque[n+1]) # sum or prod
                #print(result) 

                if answer == result:
                    solved = True
                    break
                        
            if solved:
                tot += answer
                print("found solution for ",answer, "with ",operationslist )
            else:
                print("no result for",answer)
        return tot  # answer: also     #12839601725776     too low 
    


    


def calc_b():
    
    return 0

if __name__ == "__main__":
    print(f"Day {day}")
    
    tic()
    personaldata = get_data(year= year,day = day)
    
    demodata = """190: 10 19
                    3267: 81 40 27
                    83: 17 5
                    156: 15 6
                    7290: 6 8 6 15
                    161011: 16 10 13
                    192: 17 8 14
                    21037: 9 7 18 13
                    292: 11 6 16 20"""

    if 0:
        data = demodata # personaldata
        print("demo input ")
    else:
        data = personaldata # 
        print("personal input ")

    
    answer_to_terms = parse(data)
    
    answer_a= calc_a(answer_to_terms, p1operators)
    t_a = toc()
    
    tic()
    answer_b = calc_b()
    t_b = toc()

    part = "a"
    print(f"personal answer {part}:{answer_a}")
    print(answer_a)
    part = "b"
    print(f"personal answer {part}:{answer_b}")
    #submit(answer_b)


    print("CalcuationTime:")
    print(f"Day {day} a: {t_a:2.3f}s")
    print(f"Day {day} b: {t_b:2.3f}s")


