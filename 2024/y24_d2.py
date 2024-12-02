# pip install advent-of-code-data
#from aocd.models import Puzzle
year= 2024
day = 2

from aocd import submit, get_data
import numpy as np
import pandas as pd
import os
from helperfunctions import *
filename_input = f"../../../data/input_{year}_0{day:1d}.txt"

def  parse(filename_input):
    reports =pd.read_csv(os.path.abspath(os.getcwd()+"\\" + filename_input),header=None)
    return reports

def accepted(diffarray):
    return ((np.all(-3<=diffarray) and np.all(diffarray<=-1))  or (np.all(3>=diffarray) and np.all(diffarray>=1)))

def calc_a(reports,BOOL_partb=False):
    s,sb=0,0
    for i in reports.index:
        txtrapport =reports.iloc[i].values[0]
        rapport=np.array(txtrapport.split(" ")).astype(int)
        d = np.diff(rapport)
        if accepted(d):
            s+= 1 # a
            #print("part A accepted:", rapport, d)
        else:
            ok =False
            if partB:
                for k in range(len(rapport)):
                    shorterrapport=np.delete(rapport,k)
                    shorterd = np.diff(shorterrapport)
                    if accepted(shorterd):
                        ok=True
                        break
                if ok:
                    sb +=1 
        if not BOOL_partb:  
            return s
        else:
            return s+ sb

def calc_b(reports):    
    return calc_a(reports,BOOL_partb=True)

if __name__ == "__main__":
    print(f"Day {day}")    
    tic()
    data = get_data(year= year,day = day)
    reports = parse(data)
    answer_a= calc_a(reports)
    #submit(answer_a)
    t_a = toc()
    
    tic()
    answer_b = calc_b(reports)
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


