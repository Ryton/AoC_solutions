
from helperfunctions import * ## all related imports done there.
import os 
import pprint
import copy

from collections import Counter
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

    demodata = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    obj.target =-50
    if inputtype =="D":
        obj.data = demodata # personaldata
    else:
        obj.data = get_data(year= year,day = day) # personaldata

    allines = obj.data.split("\n")
    obj.nrows = len(allines)
    obj.ncols = len(allines[0])
    obj.field = np.zeros((obj.nrows,obj.ncols))
    for a, lines in enumerate(allines):
        for b,field in enumerate(lines):
            if field =="#":
                obj.field[a,b] = -1 # wall value
            if field =="S":
                obj.start = (a-1,b-1) ## calculated w/o edges;
            if field =="E":
                obj.goal = (a-1,b-1) ## calculated w/o edges;
    obj.target = -100
    return obj


def calc_a(grid, start,goal, target_savings = -100):
    #print(grid)
    
    expandgrid = floodfill(grid, start,obstructed_value = 9999) ## no edges
    

    pprint.pprint(np.array(expandgrid))
    fair_race =  expandgrid[*goal+np.array([1,1])] # answer a 
    print(f"fair_race takes {fair_race} picosec")
    gains = []
    rows,cols = np.shape(grid)
    print(f"exp start: {start+np.array([1,1])}, value {expandgrid[*start+np.array([1,1])]}")
    print(f"exp goal: {goal+np.array([1,1])}, value {expandgrid[*goal+np.array([1,1])]}")
    
    bfsgrid = -grid
    
    opt_path =bfs_shortest_path_np(bfsgrid,(start[0],start[1]),(goal[0],goal[1]))
    #print("len opt_path",opt_path)
    # print(max = opt_path*2)
    n =0
    for a in range(rows):
        for b in range(cols):

            if grid[a,b]== -1: # #if wall
                top =(a,b+1)
                bottom =(a,b-1)
                left =(a+1,b)
                right =(a-1,b)
                if ((bottom in opt_path) or (top in opt_path)) or ((left in opt_path) or (right in opt_path)):
                    print(f"eval shotctut # {n}/10k at {a},{b}")
                    n +=1
                    shortcut_grid = copy.copy(grid)
                    shortcut_grid[a,b]= 0
                    expandgrid = floodfill(shortcut_grid, start,obstructed_value = 9999) ## no edges

                    saved_time = expandgrid[*goal+np.array([1,1])]-fair_race
                    if saved_time <= target_savings :
                        gains.append(saved_time)
                        print(f'... {saved_time} time saved')

    savings = Counter(gains)
    total = sum(savings.values)
    #for akey in  savings:
    #    if akey <= -100:
    #        total +=    savings[akey]
    return total
    
    
def calc_b(grid,start,goal,target_savings = -100):
    total= 0
    orig_grid = floodfill(grid, start,obstructed_value = 9999) ## no edges
    pprint.pprint(np.array(orig_grid))
    bfsgrid = -grid
    opt_path =bfs_shortest_path_np(bfsgrid,(start[0],start[1]),(goal[0],goal[1]))
    print("len opt_path",len(opt_path),opt_path[0:5] )
    
    for n,pos in enumerate(opt_path):
        future_goals = opt_path[n+1-target_savings:]
        time_for_firstpart = orig_grid[pos[0]+1,pos[1]+1]
        print(f" iteration # {n}/10k")

        for goal in future_goals:
            manh_dist = abs(goal[0]-pos[0]) + abs(goal[1]-pos[1])
            orig_dist_to_goal =  orig_grid[*goal+np.array([1,1])] # for example 240
            poss_saving = time_for_firstpart - orig_dist_to_goal +manh_dist

            if (manh_dist<=20) and ((poss_saving) <= target_savings):
                total += 1
        print(f" total so far:  {total}")
    return total
        

        
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":


    print(f"**** Day {day} *"+ "*"*14)

    # preprocessing

    data =  load_data(inputtype=inputtype) #"D","P"
    
    
    # timed exeution
    #tic()
    #answer_a= calc_a(data.field[1:-1,1:-1], data.start,data.goal,data.target)
    #t_a = toc()

    tic()
    answer_b = calc_b(data.field[1:-1,1:-1], data.start,data.goal,data.target)
    t_b = toc()

    #printout
    part = "a"
    print("*** Demo Input *"+ "*"*14 if inputtype == "D" else "*** Personal input *"+ "*"*14)
    #print(f"* Answer {part}: {answer_a}")
    #if submit == "a":
    #    submit(answer_a)
    
    ## optimisations for A: only update walls next to current path.
    part = "b"
    print(f"* Answer {part}: {answer_b}") ## not :8996, too low. => and makes sense.
    if submit == "b":
        submit(answer_b)

    print("* CalcuationTime:   ")
    #print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


