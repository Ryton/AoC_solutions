## dependencies
from helperfunctions import * ## all related imports done there.
from collections import Counter
import sys
import logging
from logging.handlers import SysLogHandler

import logging



##### input 
inputtype  = "D" # D(emo) or P(ersonal)
runthese = ["a" ] #["a","b"]

submit = "none" #"a" , "b", "none"
demodata = """190: 10 19
                    3267: 81 40 27
                    83: 17 5
                    156: 15 6
                    7290: 6 8 6 15
                    161011: 16 10 13
                    192: 17 8 14
                    21037: 9 7 18 13
                    292: 11 6 16 20"""
##### end input 

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
    else:
        personaldata = get_data(year= year,day = day)
        data = personaldata # 
        #print("personal input ")
    return data

def  parse(data=0):

    return 0

def calc_a(a=0, b=0):
    
    return 0 # answer a 

def calc_b():

    return 0 # answer b
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
    parsedinput = parse(data)
    
    if "a" in runthese:
        # timed exeution
        tic()
        answer_a= calc_a(parsedinput)
        t_a = toc()
    else:
        answer_a = 0
        t_a = 0

    if "b" in runthese:
        tic()
        answer_b = calc_b()
        t_b = toc()
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


