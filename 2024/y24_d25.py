##### input 
inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"
demodata = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
##### end input 

## dependencies
from helperfunctions import * ## all related imports done there.
from itertools import product as itertools_product
# get year and day
fname =  os.path.basename(__file__)
yd_ =fname.split("_")
year = 2000+ int(yd_[0][1:])
try: #try to get from filename
    yd_ =fname.split("_")
    year = 2000+ int(yd_[0][1:])
    day = int(yd_[1][1:-3]) # drop .py
except:
    year = 2024
    day = 1 # change this!



##### helperfuntions for this day

################################################### begin of today's solution ###################################################
def load_data(inputtype="D"): #["D","P"]
    

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data=0):
    patterrepeat = 8
    nrows = patterrepeat-1
    ncols =6
    lock_line = 0
    keyline = patterrepeat-2
    onesymbol = "#"
    keylines =data.split("\n")
    nkeys = (len(keylines)+1)//patterrepeat
    #print(keylines)
    keylist,locklist = [],[]
    for n in range(nkeys):
        amap = np.array([[0 if l==onesymbol else 1 for l in line] for line in keylines[n*patterrepeat:(n+1)*patterrepeat -1]])
        iskey = sum(amap[keyline,:])< sum(amap[lock_line,:])
        pinheights = 6 - np.sum(amap,axis=0) 
        keylist.append(pinheights) if iskey else locklist.append(pinheights) 
    return keylist, locklist
        
def calc_a(keylist,locklist):
    return np.sum(list(map( lambda x: np.all((x[0]+x[1])<6),itertools_product(keylist,locklist))))

def calc_b():

    return 0 # answer b
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Year {year} Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    keylist, locklist = parse(data)
    
    # timed exeution
    tic()
    answer_a= calc_a(keylist,locklist)
    t_a = toc()

    tic()
    answer_b = calc_b()
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


