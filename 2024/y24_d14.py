
from helperfunctions import * ## all related imports done there.
import matplotlib.pyplot as plt

year= 2024
day = 14 # change this!
inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"
##### helperfuntions for this day

################################################### begin of today's solution ###################################################
import re


from dataclasses import dataclass
currfloorsize = (7,11) if inputtype =="D" else (101,103)

    
def plotrobots(n,floor, robotpos, floorsize = currfloorsize):
    
    
    for pos in robotpos:        
        #print(pos)
        floor[pos]= 255
    
    plt.matshow(floor.T)
    plt.title=f"step {n}"
    plt.show()    


    
@dataclass
class arobot():
    pos: tuple[int] = (0,0)
    vel: tuple[int] = (0,0)
    

     

    def move(self, t=1):
        self.pos =self.pos

        self.pos = ( (self.pos[0] + self.vel[0]*t)  % currfloorsize[0], (self.pos[1] + self.vel[1]*t) % currfloorsize[1] )
            
        

def load_data(inputtype="D"): #["D","P"]
    demosize = (7,11)
    floor =np.array((7,12),int)
    demodata = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


    if inputtype =="D":
        data = demodata # personaldata

    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 

    mask = r"p=([\d]*),([\d]*) v=([-]?[\d]*),([-]?[\d]*)"
    robots =re.findall(mask,data)
    robot_dict = dict()
    for n,robot in enumerate(robots):
        robot_dict[n] = arobot(pos =(int(robot[0]),int(robot[1])),vel=(int(robot[2]),int(robot[3])))
        #print("demo input ")
    
    
        #print("personal input ")
    return robot_dict

def  parse(data=0):

    return 0

def evalquadrant(robotdict, Q = 0, floorsize =currfloorsize):
    
    if Q in  [0,3]:
        xmin = 0
        xmax = floorsize[0]//2
    else:
        xmin = floorsize[0]//2
        xmax = floorsize[0]

    if Q in  [0,1]:
        ymin = floorsize[1]//2
        ymax = floorsize[1]
    else:
        ymin = 0
        ymax = floorsize[1]//2

    
    print("Quadrant",Q)

    print(f"centerline at {floorsize[0]//2} and { floorsize[1]//2}")
    count = 0
    for n in robotdict:
        pos = robotdict[n].pos
        
        #print("pos",pos)
        if (pos[0] == floorsize[0]//2) or (pos[1] == floorsize[1]//2):
            print("on edge")
            continue
        if (pos[0] >= xmin) and (pos[0] <= xmax):
            if (pos[1] >= ymin) and (pos[1] <= ymax):
                count += 1
                print(f"{n} IN Q{Q},pos {pos}")
                                 
    return count

def calc_a(robotdict, t = 100):
    for robotnr in robotdict:
        robotdict[robotnr].move(t)
    ninquad = []
    for quadrant in range(4):
        n_in_quadrant =  evalquadrant(robotdict, Q = quadrant, floorsize =currfloorsize)
        ninquad.append(n_in_quadrant )
        
    print(ninquad)
    return np.prod(ninquad ) # answer a 

def calc_b(robotdict):
    nmax = int(1E6)

    centerareasize = 25
    c = (currfloorsize[0]//2,currfloorsize[1]//2)
    floor =np.zeros(currfloorsize) #np.full(currfloorsize, ".", dtype=str)
    
    areaaroundcenter = []
    for i in range(centerareasize):
        #for j in range(centerareasize):
        dx = 0 # i - centerareasize//2
        dy = i - centerareasize//2
        areaaroundcenter.append((c[0]+dx,c[1]+dy))
    treeat = []
    n = 1
    while n < nmax:
        for robotnr in robotdict:
            robotdict[robotnr].move(t=1)
        foundtree = True
        robotpos_ = [r.pos for r in robotdict.values()]
        if len(set(robotpos_))==len(robotpos_):
            foundtree = True
            
            print(n)
            treeat.append(n)
            #plotrobots(n,floor,robotpos_)
            if len(treeat) >1:
                return n
            
            
        
        if n % int(nmax/1000) == 0:
            print(f"{n} th thousand done")
        n += 1
        #print(n,end=";")
    return treeat # answer b            


################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    print(data)
    #parsedinput = parse(data)
    
    # timed exeution
    tic()
    answer_a= calc_a(data)
    t_a = toc()

    tic()
    data =  load_data(inputtype=inputtype) #"D","P"
    answer_b = calc_b(data)
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


