#!C:/anaconda3/envs/AoC/python.exe 
 
## dependencies
from helperfunctions import * ## all related imports done there.
from collections import Counter
import sys
import logging
from logging.handlers import SysLogHandler

import logging
from collections import defaultdict


##### input 
inputtype  = "P" # D(emo) or P(ersonal) "O" or "I" or "B"
runthese = ['a',"b" ] #["a","b"]

submit = "none" #"a" , "b", "none"
demodata = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

##### end input 
XOR = lambda x: x[0]^x[1]
AND = lambda x: x[0]&x[1]
OR  = lambda x: x[0]|x[1]

thisblob='''{"x00": 1,
    "x01": 1,
    "x01": 1,
"x02": 1,
"y00": 0,
"y01": 1,
"y02": 0}
'''

"""n =  eval(thisblob)
v = SimpleNamespace(**n)
v.z00 = AND((v.x00,v.y00))
v.z01 = XOR((v.x01,v.y01))
v.z02 = XOR((v.x02,v.y02))

# get all Z's out, and calc the binary.
a = sorted(v.__dict__)
zs = list(filter(None,[key if 'z' in key else False for key in a ]))[::-1]
print(zs)
val  = np.sum([2**int(v.__dict__[z]) for z in zs])
print(val)

## => inject line by line, then eval if available => then sort

"""
# get year and day
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

##### helperfuntions for this day

################################################### begin of today's solution ###################################################
def load_data(inputtype="D"): #["D","P"]
    

    if inputtype =="D":
        data = demodata # personaldata
        #print("demo input ")
    elif inputtype == "I":
        data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
    elif inputtype =="B":
        data ="""x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""

    elif inputtype =="O":
        data = """x00: 1
x01: 1
x02: 0
x03: 1
y00: 1
y01: 0
y02: 1
y03: 1

z00: 0
z01: 0
z02: 0
z03: 1
z04: 1
"""
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data=0):
    return data

def calc_a(data):
    v = {}
    to_recalc = []
    

    for line in data.split("\n"):
        if ':' in line:
            ##move to dict.
            vals =line.split(': ')
            name , b = vals

            b = int(b)
            v[name] = b
            #print("to eval:", name ,b)

        elif '>' in line:
        
            vals = line.split(" ")
            
            #print("to dict:", vals)
            XOR = lambda x: x[0]^x[1]
            AND = lambda x: x[0]&x[1]
            OR  = lambda x: x[0]|x[1]
            mapto={}
            mapto["AND"]=AND
            mapto["XOR"]=XOR
            mapto["OR"]=OR

            WHAT = vals[1]
            arg1 = vals[0]
            arg2 = vals[2]
            res = vals[4]

            
            ## good way to do it: check if v_arg exists.
            if (arg1 in v) and (arg2 in v):
                v[f"{res}"] = int(mapto[f"{WHAT}"]((v[f"{arg1}"],v[f"{arg2}"])))
            else:
                to_recalc.append((res,WHAT,arg1,arg2))
            print(f"assigned {res}")

    print("keys",v.keys())
    #print("to repeat")
    print(*to_recalc)
    iteration = 0
    currlen = len(v)
    
    while len(to_recalc) and iteration< 1000:
        
        iteration +=1
        print(iteration, len(to_recalc))
        for item in copy.deepcopy(to_recalc):

            res,WHAT,arg1,arg2 = item
            if (arg1 in v) and (arg2 in v) and not (res in v):
                
                v[f"{res}"] = int(mapto[f"{WHAT}"]((v[f"{arg1}"],v[f"{arg2}"])))
                print(f"Assigned {res} in it {iteration}")
                #to_recalc.pop(item)
            else:
                pass #go another round.
            

    
        if len(v)>currlen:
            #print("keys", v.keys())
            currlen = len(v)
        else:
            print(f"no more improvements after iteration {iteration}")
            break
    #print(v)
    #return v



    # get all Z's out, and calc the binary.
    zs = list(filter(None,[key if 'z' in key else False for key in v ]))[::-1]
    zs.sort()
    print("z's are:", zs, [v[z] for z in zs ])
    
    calcbin = lambda alist : np.sum([2**n * int(v[z]) for n,z in enumerate(alist)])
    result  = calcbin(zs)
    print(result)

    return result # answer a 

## code from HyperNeutrino, https://raw.githubusercontent.com/hyperneutrino/advent-of-code/4988973ae38cce707ff983d8c1df3bc3c3465c72/2024/day24p2.py
def make_wire(char, num):
    return char + str(num).rjust(2, "0")

def verify_z(wire, num):
    # print("vz", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "XOR": return False
    if num == 0: return sorted([x, y]) == ["x00", "y00"]
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify_intermediate_xor(wire, num):
    # print("vx", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "XOR": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    # print("vc", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND": return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": return False
    return verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)

def verify_direct_carry(wire, num):
    # print("vd", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "AND": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    # print("vr", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "AND": return False
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify(num):
    return verify_z(make_wire("z", num), num)
def progress():
    
    i = 0
    
    while True:
        if not verify(i): break
        i += 1
    
    return i



def calc_b(data,till_nr = 45):
    global formulas
    formulas = {}
    for line in data.split("\n"):
        try:
            x, op, y, z = line.replace(" -> ", " ").split()
            print(x,op,y,z)
            formulas[z] = (op, x, y)
        except:
            pass
        print(formulas)

    ## first build v and to_recalc
    #
    #print("to dict:", vals)
    XOR = lambda x: x[0]^x[1]
    AND = lambda x: x[0]&x[1]
    OR  = lambda x: x[0]|x[1]

    swaps = []

    for _ in range(4): # 4 swaps
        baseline = progress()
        for x in formulas:
            for y in formulas:
                if x == y: continue
                formulas[x], formulas[y] = formulas[y], formulas[x]
                if progress() > baseline:
                    break
                formulas[x], formulas[y] = formulas[y], formulas[x]
            else:
                continue
            break
        swaps += [x, y]

    print(",".join(sorted(swaps)))

    return formulas # answer b
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    # Create a logger
    logger = logging.getLogger(os.path.basename(__file__[:-3]))
    # Create a console handler and set the level to debug
    console_handler_stdout = logging.StreamHandler()
    console_handler_stdout.setLevel(logging.DEBUG)
    filehandler = logging.FileHandler("debug.log")
    #filehandler.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG, handlers = [console_handler_stdout,filehandler])


    logger.warning('Start')

    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    
    time.perf_counter() # tic()
    parsedinput = parse(data)
    t_a = time.perf_counter()/1E6
    if "a" in runthese:
        # timed exeution
        
        answer_a= calc_a(parsedinput)
        t_a = time.perf_counter()/1E9 # = toc()
    else:
        answer_a = 0
        t_a = 0

    if "b" in runthese:
        tic()
        start = time.perf_counter()
        answer_b = calc_b(parsedinput)
        t_b = time.perf_counter() # = toc()
    else:
        answer_b = 0
        t_b = 0

    if inputtype == "D":
        coderuntype = "*** Demo Input *"+ "*"*14  
    elif inputtype == "P": 
        coderuntype = "*** Personal input *"+ "*"*14
    else: #other tests
        coderuntype = "*** TESTING input *"+ "*"*14


    #printout
    print(coderuntype)
    part = "a"
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
    logger.info('Finished')


