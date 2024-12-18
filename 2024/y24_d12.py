
from helperfunctions import * ## all related imports done there.
from dataclasses import dataclass, field

year= 2024
day = 12 # change this!
inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"
##### helperfuntions for this day
from functools import lru_cache
from dataclasses import dataclass
"""
Learning to apply dataclasses properly?
https://docs.python.org/3/library/dataclasses.html
"""
    
@dataclass
class patch:
    #def __init__(self, letter=,pos=(0,0), neighbours =:
    cropletter: str =  "."
    pos: tuple[int] = (0,0)
    neigbours: list[str] = "...." # 4 items
    neigbourpos: list[tuple[int]]  = field(default_factory=list) #= [(1,0),(-1,0),(0,1),(0,-1)] # 4 items

    #def calc_same_neighbours(self) -> int:
    #    return 4 - self.neigbour[self.letter]
    def __repr__(self):
        return f"Patch of {self.cropletter} at {self.pos}, w neigbours {self.neigbours}"

@dataclass
class cropfield:
    
    included_patches: list[patch]
    area: int = field(init=False)
    perimeter: int = field(init=False)
    straight_perimeter: int = field(init=False)
    cost: int = field(init=False)
    costB: int = field(init=False)
    index: int = 0
    cropletter: str = "."

    def calc_area(self):
        self.area = len(self.included_patches)

    def calc_perimeter(self):
        
        temp = 0
        for p in self.included_patches:
             
                #if self.cropletter == "C":
                summed = sum([0 if str(c) == str(self.cropletter) else 1 for c in p.neigbours])
                #print(p.cropletter, ":", p.neigbours, "=>",summed)
                temp += summed

        self.perimeter = temp
    def calc_cost(self):
        self.cost = self.area * self.perimeter

    def calc_straight_perimeter(self):
        # [(1,0),(-1,0),(0,1),(0,-1)] == E,W,N,S
        
        direction = {0:0,1:1,2:0,3:1}
        directionstr = {0:"E",1:"N",2:"W",3:"S",}
        count = 0
        for d in direction: #key
            d_rowcol = direction[d]
            anti_d_rowcol = int(abs(direction[d]-1))
            tocheck =[]
            alongaxis = []
            
            for p in self.included_patches:
                n =  p.neigbours[d] # first to fourht neighbour.
                neighpos =  p.neigbourpos[d] # first to fourht neighbour.

                if not(n == self.cropletter):
                    tocheck.append(neighpos[anti_d_rowcol]) # append the tuple pos
                    alongaxis.append(neighpos[d_rowcol]) # append the tuple pos
            #print("direction:",d)
            #print("direction", directionstr[d])
            #print("along",alongaxis)
            #print("tocheck",tocheck)
            if len(alongaxis)>0:
                
                for loc in np.unique(alongaxis):
                    alongaxis
                    lenline= len(np.where(loc==alongaxis)[0])  
                    #print(lenline)
                    if lenline == 0:
                        pass
                    elif lenline ==1:
                        count += 1
                    else:
                        #print(np.where(loc==alongaxis)[0])
                        tosort = np.array([tocheck[i] for i in np.where(loc==alongaxis)[0]])
                        tosort.sort()
                        counted =  sum(np.diff(tosort)> 1)+1
                        count += counted
                
        self.straight_perimeter = count

    def calc_costB(self):
        self.costB = self.area * self.straight_perimeter
        



    def __post_init__(self):
        self.calc_area()
        self.calc_perimeter()
        self.calc_cost()
        self.calc_straight_perimeter()
        self.calc_costB()
    def __repr__(self):
        #[print(*zip(p.neigbours,p.neigbourpos)) for p in self.included_patches]
        #return f"A region of {self.cropletter} plants with price {self.area} * {self.perimeter} = {self.cost}."
        return f"A region of {self.cropletter} plants with reduced price {self.area} * {self.straight_perimeter} = {self.costB}."
        
# cached?
def neighbour_coords(position):
    neigbourpos = []
    
    for (i, j) in [(1,0),(0,1),(-1,0),(0,-1)]:
        evalpos = (int(position[0]+i), int(position[1]+j))
        #if grid[pos] == grid[*evalpos]:
        neigbourpos.append(evalpos)
    return neigbourpos


def get_neigbours(grid,position = (10,10)):

    neigbourpos = []
    neigbourletters = []
    
    for evalpos in neighbour_coords(position):
        neigbourpos.append(evalpos)
        neigbourletters.append(grid[*evalpos])

    return neigbourletters,neigbourpos


def build_arealist(input_patchlist):
    #print("NOK??")
    #print(*input_patchlist, sep = "\n")
    
    ## pseudocode:
    ## idea 2: split to visit list patchlist for each unique patchtype.
    # pick one, remove from tovisit. Expand by finding neigbours from every patch, add em.
    crops = np.unique([p.cropletter for p in input_patchlist] )
    cropfield_list = []
    cropfield_idx = -1

    #print("crops", *crops)
    
    for c in crops:
        copied_patchlist= copy.deepcopy(input_patchlist)
        cropfield_idx += 1
        #print("crop ", c)
        if c == ".":
            break
        tovisit = [] #gather all fields of this type.
        alreadyvisited = []
        for p in copied_patchlist:
            if (p.cropletter==c):
                tovisit.append(p.pos)
        #print(f"{len(tovisit)} patches for crop {c} ")
        curr_positions= []


        lastonewritten = False

        while not lastonewritten:
            thispatchdone = True
            if len(curr_positions)==0:
                # print("starting new patch.  To visit: ",  len(tovisit))
                if len(tovisit)>= 1:
                    curr_positions.append(tovisit[0]) 
                    tovisit.remove(curr_positions[0])
                    
                
                #print("start pos ", curr_positions , "for  crop",c)
                
                    

            for p in curr_positions:
                for pos in neighbour_coords(p):
                    if pos in tovisit:
                       
                       if not  (pos in curr_positions) and not (pos in alreadyvisited):
                        
                           #print(f"adding {pos} to area {cropfield_idx}, sizepatch= {len(curr_positions)}")
                           curr_positions.append(pos) 
                           tovisit.remove(pos)
                           thispatchdone = False # if something changed, do over.
            
            if thispatchdone: 
                #print("building area with")
                lastarea = buildarea(cropfield_idx=cropfield_idx, cropletter=c, curr_positions=curr_positions,localpatchlist=input_patchlist)
                [alreadyvisited.append(p) for p in curr_positions]
                cropfield_list.append(lastarea)
                cropfield_idx += 1
                curr_positions = []
                #print(f"Wrote patch. {len(alreadyvisited)} visited; {len(tovisit)}  left to visit: ")
                if len(tovisit)==0:
                    lastonewritten =True
            

    return  cropfield_list
                

def buildarea(cropfield_idx= 0, cropletter= ".", curr_positions= [(0,0),(1,1)], localpatchlist=None):
    poslist = [p.pos for p in localpatchlist]

    included_patches  = []
    
    for n, pos in enumerate(poslist):
        if pos in curr_positions:
            included_patches.append( localpatchlist[n])
    
    currarea = cropfield( index = cropfield_idx, cropletter = copy.copy(str(cropletter)), included_patches = included_patches)
    #print(currarea)

    """ # done in __post_init__
    currarea.calc_area()
    currarea.calc_perimeter()
    currarea.calc_cost()
    """
    #currarea.calc_area()
    #currarea.calc_perimeter()

    return currarea



    ''' idea 1:
    # loop all positions (tocheck locations)
    #   # if no neigbour w same name make new area .
    #   # if (one or more neigbours w same name patch, add to seen list)
    #   # if 2+ same neighbours in different patches: merge, 
    
    #   # if any change: allfound =False, and repeat.
    '''
    ## if done, calc areas and return arealist
    postocheck_ = [ p.pos for p in patchlist]
    arealist = []
    seen  = []
    
    allfound = False
    while not(allfound):
        allfound = True

        for pos in tocheck:

            pass

        
        get_neigbours(grid, pos())


        ## finally pass again and rerun calc area.

    return arealist
################################################### begin of today's solution ###################################################
def load_data(inputtype="D"): #["D","P"]
    small_demodata = """AAAA
BBCD
BBCC
EEEC"""

    big_demodata="""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    if inputtype =="D":
        data = big_demodata # personaldata
        print("demo input ")
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        print("personal input ")
    #print(data)
    return data


def  parse(data="12345"):
    n_rows = len(data.splitlines()[0])
    #grid=np.array((n_rows+2,n_rows+2),dtype=bytes)
    grid = np.array([['.']*(n_rows+2) for _ in range(n_rows+2)])
    n = 0
    for line in data.splitlines():
        n += 1
        for i in range(len(line)):
            grid[n,i+1]=line[i]
    return grid


def build_patchlist(grid):
    patchlist= []
    print("building patches")
    for x in range(np.shape(grid)[0]):
        for y in range(np.shape(grid)[1]):
            currpos = (x,y)
            if not grid[*currpos]==".": # skip sides
                neigbourletters,neigbourpos = get_neigbours(grid,currpos)
                current = patch(cropletter = grid[x,y], pos = (x,y) ,neigbours=neigbourletters,neigbourpos=neigbourpos)
                #print(current, "w neighbours", current.neigbours, "at ", current.neigbourpos,)
                patchlist.append(current)
    return patchlist


def calc_a(cropfieldlist):
    #[print(cropfield) in cropfieldlist]
    return sum(cropfield.cost for cropfield in cropfieldlist)
        

def calc_b(cropfieldlist):
    print("part B:")
    [print(cropfield) for cropfield in cropfieldlist]
    return sum(cropfield.costB  for cropfield in cropfieldlist)

    for area in arealist:        
        print(area)

    return 0
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)

    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    grid = parse(data)
    tic()
    patchlist = build_patchlist(grid)
    #print(f"len patchlist: {len(patchlist)}")
    #[print(p) for p  in patchlist]
    print("OK")
  
    arealist = build_arealist(patchlist)

    # timed exeution
    
    answer_a= calc_a(arealist)
    t_a = toc()

    tic()
    answer_b = calc_b(arealist)
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



