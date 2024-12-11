
from helperfunctions import * ## all related imports done there.

year= 2024
day = 11 # change this!
inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"
##### helperfuntions for this day
from functools import lru_cache

def blink(number):
        if number == 0:
            return [1]
        strnr = str(number)
        nel = len(strnr)
        if nel%2==0:            
            return [int(strnr[:nel//2]),int(strnr[nel//2:])]
        else:
            return [number*2024]


#@lru_cache
DP = dict()
def process_number(inputtuple):
    (number, niter) = inputtuple
    if niter == 0:
        return 1
    elif (number,niter) in DP:
        return DP[(number,niter)]
    else:
        if number == 0:
            return process_number((1,niter-1))
        strnr = str(number)
        nel = len(strnr)
        if nel%2==0:            
            left = int(strnr[:nel//2])
            right = int(strnr[nel//2:])
            DP[number,niter ] = process_number((left,niter-1)) + process_number((right,niter-1))
            return process_number((left,niter-1)) + process_number((right,niter-1))
        else:
            DP[(number, niter)]=process_number((number*2024,niter-1))
            return process_number((number*2024,niter-1))


################################################### begin of today's solution ###################################################
def load_data(inputtype="D"): #["D","P"]
    demodata = """125 17"""

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data=0):
    alist    =  [int(i) for i in data.split(" ")]
    return alist

def calc_a(thelist,nsteps = 25):
    

    #print(f"iteration {-1}: {thelist}")
    # nplist = np.array([0,1,245,24,2715])
    for iter in range(nsteps):
        thelist =[blink(i) for i in thelist]
        thelist  = [x for xs in thelist for x in xs]

        #print(f"iteration {iter}: len {len(thelist)}")                        
        
    return len(thelist)
        
    
    #print(thelist)
    #print(thelist)


def calc_b(thelist,nsteps=75):
    
    ## too slow;
    """
    for iter in range(nsteps):
        thelist =[blink(i) for i in thelist]
        thelist  = [x for xs in thelist for x in xs]

        print(f"iteration {iter}: len {len(thelist)}")                        
        
    return len(thelist)
    """

    """ no interaction/order doesnt matter so can process iteratively
         and store number of items.
    """
     
    total = 0
    for  i in thelist:
        total += process_number((i,nsteps))
    print(f"size of cache: {len(DP)}")                        

    return total
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    parsedinput = parse(data)
    # timed exeution
    tic()
    answer_a= calc_a(parsedinput,nsteps=25)
    t_a = toc()

    tic()
    answer_b = calc_b(parsedinput,nsteps = 75)
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



