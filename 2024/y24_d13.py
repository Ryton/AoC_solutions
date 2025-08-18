
from helperfunctions import * ## all related imports done there.

year= 2024
day = 13 # change this!
inputtype  = "P" # D(emo) or P(ersonal)
submit = "none" #"a" , "b", "none"
OFFSET_VALUE = 10000000000000


##### helperfuntions for this day

################################################### begin of today's solution ###################################################
demodata = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
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
    alllines=data.split('\n')
    parsed = []
    for n in range(len(alllines)//4):
        a_text = alllines[n*4]
        b_text = alllines[n*4+1]
        prize_text = alllines[n*4+2]
        
        xy_a=a_text.split(":")[1].split(" ")
        xy_b=b_text.split(":")[1].split(" ")
        xy_p=prize_text.split(":")[1].split(" ")
         
        
        x_a,y_a=[int(xy[2:].replace(",",'')) for xy in xy_a[1:]]
        x_b,y_b=[int(xy[2:].replace(",",'')) for xy in xy_b[1:]]
        p_x,p_y=[int(xy[2:].replace(",",'')) for xy in xy_p[1:]]
        parsed.append([x_a,y_a,x_b,y_b,p_x,p_y])        


    return parsed

#b =  (- ya/ xa * px  + py  ) / ( x_b * ( - ya/ xa ) + y_b ) 
#a  =  (- yb/ xb * px  + py  ) / ( x_a * ( - yb/ xb ) + y_a )
# 
# px = a * xa + b * xb    ==> * ya
# py = a * ya + b * yb     ==> * -xa
#  
# ya * px - xa * py 

def n_m_from_vector( vector, offset_px_py = False):
    [xa,ya,xb,yb,px,py]  = vector
    if offset_px_py:
        px += OFFSET_VALUE
        py += OFFSET_VALUE
    try:
        
        N  = (px * ya -  py *xa) 
        n = (xb * ya - xa * yb)  
        b = abs(N/n)
        M  = (px * yb -  py *xb)  
        m =  (xa * yb - ya * xb)
        a = abs(M/m)

        multiplier = px/(a * xa + b * xb)
        print(f"a,b, {a} ,{b}, multiplier {multiplier}" )
        if abs(a*multiplier - np.round(a*multiplier) ) < 1E-4:
            if abs(b*multiplier - np.round(b*multiplier))< 1E-4:
                a = np.round(a*multiplier)
                b = np.round(b*multiplier)
                
                print(f"found {a}, {b}")
                return a*3+b 
        else: 
            print(f"no whole number {a}, {b}")
            return 0
    except: 
        print("failed")
        pass

def calc_a(parsed, add_offset=False):
    tot = 0

    for line in parsed:
        #if add_offset:
            #line[4]+=10000000000000
            #line[5]+=10000000000000
        n = n_m_from_vector(line,offset_px_py=add_offset)    
        print("n",n)
        if n is not None:
            tot += n

    return tot # answer a 

def calc_b(parsed):
    return calc_a(parsed, add_offset=True) # answer b
################################################### end of solution ###################################################

## main script when file is run as script. 
if __name__ == "__main__":
    print(f"**** Day {day} *"+ "*"*14)
    # preprocessing
    data =  load_data(inputtype=inputtype) #"D","P"
    parsedinput = parse(data)
    
    # timed exeution
    tic()
    answer_a= calc_a(parsedinput)
    t_a = toc()

    tic()
    answer_b = calc_b(parsedinput)
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
        submit(answer_b) ##83232379451012 fixed!

    print("* CalcuationTime:   ")
    print(f"* Day {day} a: {t_a:2.3f}s")
    print(f"* Day {day} b: {t_b:2.3f}s")
    print("*"*30)


