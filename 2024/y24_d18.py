
from helperfunctions import * ## all related imports done there.
import os 

import copy
fname =  os.path.basename(__file__)
print(fname)

yd_ =fname.split("_")
year = 2000+ int(yd_[0][1:])
print(yd_[1])



try: #try to get from filename
    yd_ =fname.split("_")
    year = 2000+ int(yd_[0][1:])
    day = int(yd_[1][1:-3]) # drop .py
except:
    year = 2024
    day = 1 # change this!


inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"

 
################################################### begin of today's solution ###################################################

##### helperfuntions for this day

#def floodfill() moved to helperfunctions

def load_data(inputtype="D"): #["D","P"]
    obj = Map()
    demodata = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    obj.data = demodata # personaldata
    obj.nrows = 7
    obj.ncols = 7
    obj.start = (0,0)
    obj.goal = (7,7)
    if inputtype =="D":
        
        #print("demo input ")
        print(demodata)
    else:
        personaldata = get_data(year= year,day = day)
        
        obj.data = personaldata # personaldata
        
        obj.nrows = 71
        obj.ncols = 71
        obj.goal = (71,71)#value in EXPANDED grid!
        #print("personal input ")
    return obj

def  parse(data=None, nbytes = 12):
    if data ==None:
        print( "Got to pass input for parse")
    else:
        corrupted_field = np.zeros((data.nrows,data.ncols))
        for n,line in enumerate(data.data.split("\n")):
            
            a,b = map(int,line.split(","))
            #print(a,b)
            if n < nbytes:
                corrupted_field[b,a] = -1
    return corrupted_field


""" IDEA: 
Do floodfill check of value for end square.
Test w empty => 12.
"""

def calc_a(grid, start):
    expandgrid = floodfill(grid, start)

    return expandgrid[*data.goal] # answer a 

def calc_b(data,NBYTES,NBYTES_MAX):

    ## would be faster with nomad or scipy. => one parametere minimisation.
    for n in np.arange(NBYTES,NBYTES_MAX): # np.arange( 3035,3036+5):# 

        corrupted_grid = parse(data, nbytes = n)
        #print(corrupted_grid)
        answer_a= calc_a(corrupted_grid, data.start )
        print(n,answer_a, data.data.split("\n")[n-1])
        if answer_a >= 9999:
            return data.data.split("\n")[n-1] # answer b
        

        
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":


    print(f"**** Day {day} *"+ "*"*14)
    
    if inputtype == "D":
        NBYTES = 12
    else: 
        NBYTES = 1024
        NBYTES_MAX = 1024 *3
        
    

    # preprocessing

    data =  load_data(inputtype=inputtype) #"D","P"
    
    
    corrupted_grid = parse(data, nbytes = NBYTES)
    #print(corrupted_grid)
    # timed exeution
    tic()
    answer_a= calc_a(corrupted_grid, data.start)
    t_a = toc()

    tic()

    answer_b = calc_b(data,NBYTES,NBYTES_MAX)
    t_b = toc()

    #printout
    part = "a"

    print("*** Demo Input *"+ "*"*14 if inputtype == "D" else "*** Personal input *"+ "*"*14)
    print(f"* Answer {part}: {answer_a}")
    if submit == "a":
        submit(answer_a)

    part = "b"
    print(f"* Answer {part}: {answer_b}")
    if submit == "b":
        submit(answer_b)

    print("* CalcuationTime:   ")
    print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


