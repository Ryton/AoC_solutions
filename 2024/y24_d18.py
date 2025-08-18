
from helperfunctions import * ## all related imports done there.
import os 

import copy
fname =  os.path.basename(__file__)
print(fname)

yd_ =fname.split("_")
year = 2000+ int(yd_[0][1:])
print(yd_[1])



try: #try to get from filename
    #fname = sys.argv[0] ### os.path.basename(__file__)

    yd_ =fname.split("_")
    year = 2000+ int(yd_[0][1:])
    day = int(yd_[1][1:-3]) # drop .py

except:
    year = 2024
    day = 1 # change this!
#print(f"puzzle for {day} - {year}:")

inputtype  = "P" # D(emo) or P(ersonal)
if inputtype == "D":
    NBYTES = 12
else: 
    NBYTES = 1024
submit = "none" #"a" , "b", "none"
##### helperfuntions for this day
################################################### begin of today's solution ###################################################
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

def floodfill(grid,start=(0,0), nrows = 7, ncols = 7):
    max_tries = 9999 #nrows*ncols
    gridsize = np.shape(grid)+ np.array([2,2]) #with walls.

    

    # naive, visit them all again... but only need to re-visit ones next to values that have been updated.
    #for n in np.arange(0,max_tries):
    n = 0
    if 1: #
        if n ==0:
            # init  surrounding 
            expandgrid = np.ones(gridsize)*max_tries
            expandgrid[0,:]  =  max_tries*2 +1
            expandgrid[-1,:]  =  max_tries*2 +1
            expandgrid[:,0]  =  max_tries*2 +1
            expandgrid[:,-1]  =  max_tries*2 +1

            tovisit_again = [] ##only visit again if adj was updated!
            possiblepath = []
            for a in np.arange(1,nrows+1):
                for b in np.arange(1,ncols+1):
                
                    if grid[a-1,b-1]<  0 :
                        expandgrid[a,b] = max_tries +1
                    else:
                        possiblepath.append(copy.copy((int(a),int(b))))
            expandgrid[start[0]+1,start[1]+1]= 0
            #print(possibleroute)
            # iterate over all positions.

            # go over them once!    

            a,b= start+np.array([1,1])
            tovisit_again = [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]
            next_list = []
        
        # iterate till len_tovisit_again <0
        
        while ((len(tovisit_again)>0) and n<max_tries):
            #print("listlength",len(tovisit_again))
            #print(tovisit_again)
            n = n+1
            for loc in tovisit_again:
                a,b = loc
                
                #grid3x3 = expandgrid[a-1:+a+1,b-1:b+1] #also diag ok
                grid_cross = [expandgrid[a-1,b],expandgrid[a+1,b],expandgrid[a,b-1],expandgrid[a,b+1]]
                minval = np.min(grid_cross)
                
                isedge = (a ==0 or a>nrows or b ==0 or b>ncols)
                if not(isedge):
                    iswall = (grid[a-1,b-1]<0)
                else:
                    iswall = isedge 

                if (expandgrid[*loc] > minval+1) and not(iswall) and not(isedge):  
                    expandgrid[*loc] = minval+1
                    for adj in [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]:
                        #print("adj", adj)
                        a,b = adj
                        isedge = (a ==0 or a>nrows or b ==0 or b>ncols)
                        if not(isedge):
                            iswall = (grid[a-1,b-1])<0
                        else:
                            iswall = isedge
                            
                        if iswall or isedge: # then  a wall or side  (==> skip those
                            pass
                        else:
                            #print("adj", adj)
                            #print("val", expandgrid[*adj])
                            #print("minval = ", minval) 
                            if expandgrid[*adj]>(minval+1):
                                next_list.append(adj)
                                
                
            #remove duplicates
            tovisit_again = copy.copy (next_list)
            next_list = [] 
    #print(expandgrid)
    return expandgrid

def calc_a(grid, start,nrows, ncols):
    expandgrid = floodfill(grid, start,nrows, ncols)

    return expandgrid[*data.goal] # answer a 

def calc_b(data,NBYTES):

    ## would be faster with nomad or scipy. => one parametere minimisation.
    for n in np.arange(NBYTES,NBYTES*5): # np.arange( 3035,3036+5):# 

        corrupted_grid = parse(data, nbytes = n)
        #print(corrupted_grid)
        answer_a= calc_a(corrupted_grid, data.start , data.nrows, data.ncols)
        print(n,answer_a, data.data.split("\n")[n-1])
        if answer_a >= 9999:
            return data.data.split("\n")[n-1] # answer b
        

        
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    
    
    corrupted_grid = parse(data, nbytes = NBYTES)
    #print(corrupted_grid)
    # timed exeution
    tic()
    answer_a= calc_a(corrupted_grid, data.start , data.nrows, data.ncols)
    t_a = toc()

    tic()

    answer_b = calc_b(data,NBYTES)
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


