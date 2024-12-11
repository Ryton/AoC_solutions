year= 2024
day = 10 # change this!
inputtype  = "P" # D(emo) or P(ersonal)
BOOL_verbose = False

from helperfunctions import *
from itertools import chain
##### helperfuntions


### recurring functions
def load_data(inputtype=inputtype): #"D","P"
    
    demodata = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data="12345"):
    n_rows = len(data.splitlines()[0])
    grid=np.ones((n_rows+2,n_rows+2))*(-1)
    n = 0
    for line in data.splitlines():
        n += 1
        for i in range(len(line)):
            grid[n,i+1]=int(line[i])
    return grid

def calc_a(grid,bool_calc_A = True):
    for val in np.arange(9,-1,-1):
        posval = np.where(grid==val)
        tuplepos = list(zip(posval[0],posval[1]))
        traildict= dict()
        if val==9:
            for xy in tuplepos:
                traildict[xy]= [int(xy[0])*100+int(xy[1])]
            print(traildict, " at  value ",val   )
        else:
            for xy in tuplepos:                
                reachablelist = []
                for neighbour in [(xy[0]-1,xy[1]),(xy[0]+1,xy[1]),(xy[0],xy[1]-1),(xy[0],xy[1]+1)]:
                    if neighbour in prev_traildict.keys():
                        for i in prev_traildict[neighbour]:
                            reachablelist.append(i)
                reachablelist = [    x     for x in reachablelist    ]    
                traildict[xy]= reachablelist
        prev_traildict = copy.deepcopy(traildict)
        
    if bool_calc_A:
        traillengths = [len(set(traildict[akey])) for akey in traildict]
        return sum(traillengths)
    else:
        trailrating = [len(traildict[akey]) for akey in traildict]
        return sum(trailrating)
    

def calc_b(grid): ## alternative solution, NOK!
    return calc_a(grid, bool_calc_A=False)

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

    #printout
    part = "a"

    print("*** Demo Input *"+ "*"*14 if inputtype == "D" else "*** Personal input *"+ "*"*14)
    print(f"* Answer {part}: {answer_a}")

    tic()
    answer_b = calc_b(parsedinput)

    t_b = toc()
    
    part = "b"
    print(f"* Answer {part}: {answer_b}")
    #submit(answer_b)


    print("* CalcuationTime:   ")
    print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


