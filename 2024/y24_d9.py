year= 2024
day = 9 # change this!
inputtype  = "P" # D(emo) or P(ersonal)


from helperfunctions import *
from itertools import chain
##### helperfuntions


### recurring functoins
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
    items_and_gaps = [[n//2]*int(data[n]) if (n%2==0) else ["."]*int(data[n]) for n in range(len(data))]
    items_and_gaps = list(chain.from_iterable(items_and_gaps))
    print(items, gaps)
    print(items_and_gaps)
    
    return items,items_and_gaps


def calc_checksum(sorted_array= [[0],[1,1],[2,2,2]]):
    nel = np.prod(np.shape(sorted_array))
    ## To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position 0. If a block contains free space, skip it instead.
    return  list(chain.from_iterable(sorted_array))@np.arange(0,nel).T
def calc_a(items,items_and_gaps):
    sorted_list  = copy.deepcopy(items_and_gaps)
    
    itemlist = list(chain.from_iterable(items))
    reverse_itemlist  = list(chain.from_iterable(items))
    replace_counter = 0
    pos_counter = 0
    
    checksum =0
    
    print("itemlist", itemlist)
    print("items_and_gaps", itemlist)
    items_and_gaps
    savedlist = []
    n =0
    
    for i in range(len(itemlist)):

        
        if items_and_gaps[i]== ".":
            n -=1
            value = itemlist[n]
        else:
            value = items_and_gaps[i]
        savedlist.append(value)
        
    
    return savedlist@np.arange(0,(len(itemlist))) # answer:     #12839601725776     too low 
    

    


def calc_b():
    return 0

## main script when file is run as script
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    items,items_and_gaps = parse(data)
    
    # timed exeution
    tic()
    answer_a= calc_a(items, items_and_gaps)
    t_a = toc()

    tic()
    answer_b = calc_b()
    t_b = toc()

    #printout
    part = "a"

    print("*** Demo Input *"+ "*"*14 if inputtype == "D" else "*** Personal input *"+ "*"*14)
    print(f"* Answer {part}: {answer_a}")
    
    part = "b"
    print(f"* Answer {part}: {answer_b}")
    #submit(answer_b)


    print("* CalcuationTime:   ")
    print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


