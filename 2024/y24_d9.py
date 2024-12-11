year= 2024
day = 9 # change this!
inputtype  = "P" # D(emo) or P(ersonal)
BOOL_verbose = False

from helperfunctions import *
from itertools import chain
##### helperfuntions


### recurring functions
def load_data(inputtype=inputtype): #"D","P"
    
    demodata = "2333133121414131402"

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data="12345"):
    items,gaps = [], []
    
    [items.append([n//2]*int(data[n])) if (n%2==0) else gaps.append(int(data[n])) for n in range(len(data))]

    length_and_itemid = [(int(data[n]),n//2)  if (n%2==0) else (int(data[n]),-1) for n in range(len(data))]
    #print(length_and_itemid)

    items_and_gaps = [[n//2]*int(data[n]) if (n%2==0) else ["."]*int(data[n]) for n in range(len(data))]
    items_and_gaps = list(chain.from_iterable(items_and_gaps))
    #print(items, gaps)
    #print(items_and_gaps)
    
    
    return gaps,items,items_and_gaps,length_and_itemid


def calc_checksum(sorted_array= [[0],[1,1],[2,2,2]]):
    nel = np.prod(np.shape(sorted_array))
    ## To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position 0. If a block contains free space, skip it instead.
    return  list(chain.from_iterable(sorted_array))@np.arange(0,nel).T

def calc_a(items,items_and_gaps):
    
    itemlist = list(chain.from_iterable(items))
    n = 0
    #print("itemlist", itemlist)
    #print("items_and_gaps", itemlist)
    savedlist = []
    
    for i in range(len(itemlist)):
        if items_and_gaps[i]== ".":
            n -=1
            value = itemlist[n]
        else:
            value = items_and_gaps[i]
        savedlist.append(value)
        
    
    return savedlist@np.arange(0,(len(itemlist))) # answer:     #12839601725776     too low 
    

    


def slow_calc_b(length_and_itemid):
    
    immutable = copy.deepcopy(length_and_itemid)
    nel = len(length_and_itemid)
    nblocks = max([lenid[1] for lenid in length_and_itemid ])
    #print("shape ",np.shape(length_and_itemid))
    #print(immutable)
    r_counter = np.arange(nblocks,-1,-1)
    #print(r_counter)
    deltapos = 0
    #for n in r_counter: # evaluate each block exactly once.
    for n in tqdm (r_counter, desc="To go..."):

        #print(" evaluating block #",n)
        possibleloc = copy.deepcopy(length_and_itemid)
        for currpos, item in enumerate(length_and_itemid):
            (itemlen,itemtype)  = item # split it.
            if itemtype == n: # only move that one.
                #print("found ", itemtype, "at pos ", currpos, "length ",itemlen)
                break #there will always be just one.        

        if itemtype >0: # ifts not a gap, try to move it.
            #print(" moving  item ", itemtype, "block " ,item)
            
            for m, possibleloc in enumerate(possibleloc):
                if (possibleloc[1] == -1) and possibleloc[0]>=itemlen:
                    #print("first possible location: ", possibleloc)
                    if m < currpos: #only move if it is an improvement.
                        
                        length_and_itemid[currpos] = [itemlen,-1]    #replace old row with a gap
                        
                        length_and_itemid[m] = item # replace the gap w this new value.

                        #print(iter, "moved to ",m)
                        if possibleloc[0]>itemlen:
                            length_and_itemid.insert(m+1, (possibleloc[0]-itemlen,-1)) #gap is shortened.
                            deltapos -= 1
                            #print("remaining gap added: ")
                        break
                        #print("first possible location: ", possibleloc)
    
            #print("next iteration is:", length_and_itemid)
            
    sorted_array = list(chain.from_iterable([pos[0]*[int(pos[1])] if pos[1]> -1  else [0]*pos[0] for pos in length_and_itemid]))
    #print("sorted array ", sorted_array)
    
    cumsum = 0
    for n,i in enumerate(sorted_array):
        cumsum += n*i
    return cumsum



from tqdm import tqdm
 

def calc_b(length_and_itemid): ## alternative solution, NOK!
    blocksizes = np.array([item[0] for item in  length_and_itemid])
    blocktypes = np.array([item[1] for item in  length_and_itemid])
    blocknrs = np.unique(blocktypes)
    #print(blocknrs)
    nblocks = len(blocknrs) -1
    r_counter = np.arange(nblocks-1,0,-1)
    #print(r_counter)
    deltapos = 0
    
    for n in tqdm (r_counter, desc="To go..."):

        try:
            currloc = np.argwhere(blocktypes==n)[0][0]
            #print (currloc)
            
            #currloc = np.argwhere(blocktypes ==n)[0] # will be just one.
            reqsize = blocksizes[currloc]
            gaps = np.argwhere(blocktypes==-1)
            bigspaces = np.argwhere(blocksizes> reqsize)
            spaces = np.union1d(gaps, bigspaces)
            
            if len(spaces)>0:
                to_loc = spaces[0] # take first
                
                if to_loc< currloc:
                    # then move.
                    remaining = blocksizes[to_loc]- reqsize 
                    #A) replace old row with a gap
                    blocktypes[currloc] = -1    
                    blocksizes[currloc] = reqsize    

                    blocktypes[to_loc] = n    
                    blocksizes[to_loc] = reqsize    
                    
                    if remaining>0:

                        blocktypes = np.insert(blocktypes, to_loc+1, -1    )
                        blocksizes = np.insert(blocksizes,to_loc+1, remaining)
                        #A) replace old row with a gap
        except:
            print("failed for item ", n)
        sorted_array = list(chain.from_iterable([blocksizes[n]*[int(blocktypes[n])] if blocktypes[n]> -1  else [0]*blocksizes[n] for n in range(len(blocktypes))]))
        #print("sorted array ", sorted_array)

    cumsum = 0
    for n,i in enumerate(sorted_array):
        cumsum += n*i
    return cumsum

## main script when file is run as script
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    gaps,items,items_and_gaps,length_and_itemid = parse(data)
    
    # timed exeution
    tic()
    answer_a= calc_a(items, items_and_gaps)
    t_a = toc()

    #printout
    part = "a"

    print("*** Demo Input *"+ "*"*14 if inputtype == "D" else "*** Personal input *"+ "*"*14)
    print(f"* Answer {part}: {answer_a}")

    tic()
    answer_b = slow_calc_b(length_and_itemid)
    t_b = toc()

    
    part = "b"
    print(f"* Answer {part}: {answer_b}")
    #submit(answer_b)


    print("* CalcuationTime:   ")
    print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


