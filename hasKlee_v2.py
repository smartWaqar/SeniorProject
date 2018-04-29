
################################
####### Version 1###############

################################


import os
from z3 import *
import commands
import subprocess


myValue = 5
#myfilename = "factorial_trace2"
myfilename = "guardTrace"

command = "runghc " + myfilename+" " +str(myValue)  #+ " > tmp.txt"
print "Command: ", command


def checkError(mystr, val):
    tdata1 = ""
    for mychar in mystr:
        tdata1 +=  mychar 

    #print tdata1
    tdata1 = tdata1.replace("NOT(error)", "")
    #print tdata1

    if "error" in tdata1:
        print ""
        print "############### Attention ####################"
        print "Error occured at value: ", val
        print "##############################################"
        print "Exiting Further Checking"
        exit()
        


#os.system(command)
"""
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell = True)
out = p.stdout.read()
print out
print out

#result = subprocess.check_output(command, shell=True)
#print "Result: ", result
"""
ret = ""
ret = commands.getoutput(command)
#print "-------------Preview -------------------"
#print ret
#print "----------------------------------------"

checkError(ret, myValue)

firstLine = ""

for mychar in ret:
    if mychar == '\n':
        print "Breaking"
        break
    firstLine += mychar


print "First Line:", firstLine



def updateFirstLine():

    global firstLine

    command = "runghc " + myfilename + " " +str(myValue)  #+ " > tmp.txt"
    print "Command: ", command
    
    ret = ""
    ret = commands.getoutput(command)
    #print "-------------Preview -------------------"
    #print ret
    #print "----------------------------------------"
    checkError(ret, myValue)

    firstLine = ""

    for mychar in ret:
        if mychar == '\n':
            #print "Breaking"
            break
        firstLine += mychar


    #print "First Line:", firstLine

    

prev_checked = []
not_checked = []

def getConditions(tCond):
    #global prev_checked
    print "Condition Provided: ",  tCond
    myArray =  tCond.split(",")
    tempArray = []
    for i in myArray:
        if "VAR" not in i and "error" not in i:
            tempArray.append(i)
            
    #curr_cond = ''.join(tempArray)
    #if curr_cond not in prev_checked:
    #    prev_checked.append(curr_cond)
    
    #print "Temp Array: ", tempArray 
    if tempArray not in prev_checked: 
        #print "Appended"
        print prev_checked
        prev_checked.append(tempArray)
        #print "debug 1: ", prev_checked
    else:
        print "Not Appended"
    #----------- populate yet to be checked -----
   
   
    tempArray2 = list(tempArray)
    tSize = len(tempArray2)
     
    tk = 4
    
    #print  "debug 2: ", prev_checked
    
    while len(tempArray2) != 0:
        #print "Print 1"
        lastElem = tempArray2.pop()
        tArray2 = tempArray2[0:]
        if "NOT" in lastElem:
            tArray2.append(lastElem[3:])
        else:
            tArray2.append("NOT" + lastElem)
            
        if tArray2 not in not_checked and tArray2 not in prev_checked:
            not_checked.append(tArray2)
    
        #print "debug 3: ", prev_checked
    
        tk = tk -1
        if tk == 0:
            break

#prev_checked.append(firstLine)
#updateFirstLine()
getConditions(firstLine)

print "Prev_checked: ", prev_checked
print "Not checked: ", not_checked

k = 1000

checkedValues = []

numPaths = 0
numUniquePaths = 0

while len(not_checked) != 0:
    
    numPaths += 1

    curr_cond = not_checked.pop()
    mySolver = Solver()
    x1 = Int('X1')
    
    for i in curr_cond:
        i = i.replace("(", "")
        i = i.replace(")", "")
        
        if "NOT" in i:
            i = i.replace("NOT", "")
            f = eval(i)
            mySolver.add(Not(f))
    
        else:
            f = eval(i)
            mySolver.add(f)
            
    if str(mySolver.check()) == "sat":
        mySol = mySolver.model()
        solVal = mySol[mySol[0]]

        if (solVal in checkedValues):
            print "Value: ", solVal, "already checked"
            continue
        else:
            checkedValues.append(solVal)

        print "-------------------------------------------"
        print "For Cond: ", curr_cond, " Value: ", solVal
        print "-------------------------------------------"
        
        myValue = solVal
        updateFirstLine()
        getConditions(firstLine)
        
    else:
        print "Condition Not satisfiable: ", curr_cond
    
    
    print "Not Checked: ", not_checked
    print "Previously Checked: ", prev_checked
    
    k = k-1
    if k == 0:
        break

    numUniquePaths += 1


print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
print "--------- NO Error Found ------"
print "Number of Paths Explored: ", numPaths
print "Number of Unique Paths: ", numUniquePaths
if k == 0:
    print "Program Terminated after reaching depth limit"
else:
    print "Program Execution Completed"
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

