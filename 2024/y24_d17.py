##### input 
import sys
print(sys.maxsize)

inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"
runthese = ["a","b"] #["a","b"]

demodata = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
##### end input 

# get year and day
from helperfunctions import * ## all related imports done there.
from collections import Counter

from multiprocessing import Pool
import multiprocessing
# A CPU heavy calculation, just
# as an example. This can be
# anything you like

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

## dependencies


##### helperfuntions for this day

################################################### begin of today's solution ###################################################
def load_data(inputtype="D"): #["D","P"]
    
    if inputtype =="D":
        data = demodata # personaldata

        # ... manual:
        registers = [729, 0,0]
        prog = [0,1,5,4,3,0]
     
        #print("demo input ")
    elif inputtype =="T":
        if 0:
            prog = [2,6]
            registers= [0,0,9] 
        elif 0:
            prog = [1,7]
            registers= [0,29,9] 

        elif 0:
            prog = [0,1,5,4,3,0]
            registers= [2024,29,9] 

        elif 0:
            prog = [1,7]
            registers= [0,29,9] 
        elif 0:
            prog = [4,0]
            registers= [0,2024,43690] 
        elif 0:
            prog = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]
            registers= [30899381,0,0] 
        elif 0:
            registers = [117440, 0,0]
            prog = [0,3,5,4,3,0]
        elif 1: ## testing my solution for B
            #9223372036854775807  
            registers = [164279024971453,0,0]
            prog = [2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0]

    else:
        #personaldata = get_data(year= year,day = day)
        #data = personaldata # 
        registers = [64854237, 0,0]
        prog = [2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0]

    return registers, prog

def  parse(data=0):

    return 0

def calc_a(reg, prog):
    
    pointer =0
    iter = 0
    UPPER_LIM = 1E8
    output = []
    #print(f"reg vals {[int(r) for r in reg]}, {output},{pointer}")
    while pointer < len(prog) and iter < UPPER_LIM:
        iter +=1
        instr = prog[pointer]
        operand = prog[pointer+1]
        
        f = instructions_map[str(instr)]
        #print(f"prog {pointer}: {instr},{operand},fun {f.__name__}")
        [reg, output, pointer] = f(reg,output,pointer, operand)
        #print(f"reg vals {reg}, {output},{pointer}")
    #print(f"n iterations {iter}" )
    return ",".join([str(o) for o in output]) # answer a 


def calc_a(reg, prog,max_out=99):
    
    pointer =0
    iter = 0
    UPPER_LIM = 1E8
    output = []
    #print(f"reg vals {[int(r) for r in reg]}, {output},{pointer}")
    while pointer < len(prog) and iter < UPPER_LIM:
        iter +=1
        instr = prog[pointer]
        operand = prog[pointer+1]
        
        f = instructions_map[str(instr)]
        #print(f"prog {pointer}: {instr},{operand},fun {f.__name__}")
        [reg, output, pointer] = f(reg,output,pointer, operand)

        if len(output)==max_out:
            return output
        #print(f"reg vals {reg}, {output},{pointer}")
    #print(f"n iterations {iter}" )
    return output # answer a 


def check_digit_n(full_n, GOAL,digit_n =1):
    
    for n in range(8):
        reg = [full_n+n, 0,0]
        values = calc_a(reg, GOAL,max_out =99)
        tocheck = GOAL[-digit_n:]
        
        try:
            GOAL[digit_n+1]
            if np.all(values == GOAL):
                print("DONE",full_n+n)            
                return full_n+n
        except:
            print("branch exhausted => moving on!")
            return False
        #print("target_value", GOAL[-digit_n])
    
        if len(values)== abs(digit_n+1):
            if values[digit_n+1] == GOAL[digit_n+1]:
                
                full_n = (full_n+n)<< 3            
                print(values, "OK; next ", full_n , "next digit",digit_n-1)
                for n in range(8):
                    reg = [full_n+n, 0,0]
                    
                    if val:= check_digit_n(full_n+n, GOAL,digit_n=digit_n-1):

                        return val
                    else: 
                        continue
                    # else continue.
            else: 
                continue

        else: 
                return False

def calc_b(reg,FULLGOAL):
    print("B", FULLGOAL)
    n=0 ## went well till last digit... n = 164279024971432 => fails
    final_val = check_digit_n(n, FULLGOAL,digit_n =-2) 
    #n = 1314232199771560
    #final_val = check_digit_n(n, FULLGOAL,digit_n =-2) 
            
    return final_val
    
################################################### end of solution ###################################################

def adv(reg,output,pointer,operand,writeto = 0):
    nomi  = int(reg[0])
    denomi = 2**combo(operand,reg)
    reg[writeto] = int(nomi//denomi)
    return [int(r) for r in reg],output,pointer+2

def bxl(reg,output,pointer,operand):
    reg[1]= np.bitwise_xor(reg[1],operand)
    return [int(r) for r in reg],output,pointer+2

def bst(reg,output,pointer,operand):
    reg[1] = int(combo(operand,reg)%8)
    
    return [int(r) for r in reg],output,pointer+2

def jnz(reg,output,pointer,operand):
    if reg[0]==0:
        return [int(r) for r in reg],output,pointer+2
    else:
        pointer = int(operand)
    #print(f'jumped to {pointer}')
    return [int(r) for r in reg],output,pointer

def bxc(reg,output,pointer,operand):
    reg[1] = int(np.bitwise_xor(reg[1],reg[2]))
    return [int(r) for r in reg],output,pointer+2

def out(reg,output,pointer,operand):
    output.append(int(combo(operand, reg)%8))
    return [int(r) for r in reg],output,pointer+2

def bdv(reg,output,pointer,operand):
    return adv(reg,output,pointer,operand,writeto = 1)

def cdv(reg,output,pointer,operand):
    return adv(reg,output,pointer,operand,writeto = 2)

def run_instructions(reg,output,pointer =0, instr=0, operand = 0):
    f = instructions_map[instr]
    return f(reg,output,pointer)


instructions_map = {'0':adv, '1':bxl,'2':bst,'3':jnz,'4':bxc,'5':out,'6':bdv,'7':cdv}

def combo(operand,reg): 
    return operand if (operand <=3) else reg[operand-4]

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    print(data)
    parsedinput = parse(data)
    

    if "a" in runthese:
        # timed exeution
        tic()


        answer_a_ints= calc_a(*data)
        answer_a =",".join([str(o) for o in answer_a_ints])
        t_a = toc()
    else:
        t_a = 0
        answer_a = 0
    
    if "b" in runthese:
        tic()
        answer_b = calc_b(*data)
        t_b = toc()
    else:
        t_b = 0
        answer_b = 0

    #printout
    part = "a"
    
    if inputtype == "D":
        coderuntype = "*** Demo Input *"+ "*"*14  
    elif inputtype == "P": 
        coderuntype = "*** Personal input *"+ "*"*14
    else: #other tests
        coderuntype = "*** TESTING input *"+ "*"*14
    
    print(coderuntype)

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


