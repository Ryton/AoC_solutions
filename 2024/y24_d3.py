# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 3

from aocd import submit, get_data
import numpy as np
import pandas as pd
import os
from helperfunctions import *
import re

def calc_a(personalinput):
    rawstring = r'{}'.format(personalinput)
    numbers = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",rawstring)
    #print(numbers)
    return sum([int(i)*int(j) for i,j in numbers])

def calc_b(personalinput):    
    rawstring = r'{}'.format(personalinput)
    numbers = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",rawstring)

    mults=re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    dos=re.compile(r"do\(\)" )         
    donts=re.compile(r"don\'t\(\)")

    nr_iter = mults.finditer(rawstring)
    do_iter = dos.finditer(rawstring)
    dont_iter = donts.finditer(rawstring)
    
    nrpos = np.array([match.end() for match in nr_iter])
    dopos = np.array([match.end() for match in do_iter])
    dontpos = np.array([match.end() for match in dont_iter])
    #print(nrpos)
    #print(dopos)
    #print(dontpos)
    
    count =0

    for n,i in enumerate(nrpos):
        #print(i)
        try:
            prevdo = dopos[dopos<i][-1]
        except:
            prevdo =0
        try:
            prevdont = dontpos[dontpos<i][-1]
        except:
            prevdont = -99
            
        if prevdo > prevdont:
            count += int(numbers[n][0])*int(numbers[n][1])
        else:
            #print(f"blocked {int(numbers[n][0])*int(numbers[n][1])}")
            pass
    return count

if __name__ == "__main__":
    print(f"Day {day}")    
    
    tic()
    personalinput = get_data(year= year,day = day)
    #parse(personalinput)
    answer_a= calc_a(personalinput)
    
    t_a = toc()
    
    tic()
    answer_b = calc_b(personalinput)
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


