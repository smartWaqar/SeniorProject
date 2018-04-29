#!/usr/bin/env python3

##############################################
############ Version 1 #######################
# Works for cases where:
# Only 1 function
# Function has only 1 variable
# Pattern matcing with equal and not equal and guards
##############################################
##############################################

import os

from pyparsing import *
os.chdir(os.getcwd())

inputFilename = "guards.hs"
#inputFilename = "src.hs"
#inputFilename = "guard2.hs"
interFilename = "guardTraceTemp.hs"
tempFilename = "anotherTemp.hs"
finalFilename = "guardTrace.hs"

def instrument():

    case1 = Word(alphanums) + ZeroOrMore(Word(alphanums) | Literal('-'))
    case2 = Word(alphanums) + ZeroOrMore(Word(alphanums) | Literal('&&') | Literal('==') | Literal('>=') | Literal('<=') | Literal('<') | Literal('>') | Literal('.'))
    f1 = open(inputFilename, 'r')
    f2 = open(interFilename, 'w')
    f3 = open(finalFilename,'w');

    results = ""
    newLine=""
    prev_conditions = []
    variableName=''
    funcVar = {}
    funcDef = {}
    prevline = ''

    for anotherline in f1:
        if ("|" in anotherline):
            if not '|' in prevline and prevline != '\n':
                arr = prevline.split(' ');
                funcVar[arr[0]] = map(str.strip,arr[1:])
                funcDef[arr[0]] = [];
            funcLines = funcDef[arr[0]];
            funcLines.append(anotherline);
            funcDef[arr[0]] = map(str.strip,funcLines);
        prevline = anotherline
    f1.close()
    f1 = open(inputFilename, 'r')
    
    yes = True;
    fl = 1;
    first = 1;
    foundVal = 0;

    while(yes):
        if(fl == 0):
            f1 = open(interFilename, 'r')
            f2 = open(tempFilename, 'w')
            #print "here1"

        elif(first == 0 and fl == 1): 
            f1 = open(tempFilename, 'r')
            f2 = open(interFilename, 'w') 
            #print "here2"
        #else:
            #print "here3"         
        first = 0;
        for someOtherLine in f1:
            if('|' in someOtherLine):
                let_try=someOtherLine[someOtherLine.find('|')+1:]
                results = let_try.split();
                for index,val in enumerate(results):
                    if val in funcVar:
                        foundVal = 1;
                        del results[0];
                        currentVariableName = results[0];
                        del results[0];
                        for condition in funcDef[val]:
                            condition = condition.replace('|','');
                            if ( 'otherwise' not in condition):\
                                condition = condition.replace('=','&&');
                            else:
                                condition = condition.split();
                                del condition[0]
                                del condition[0]
                                condition = ''.join(condition);
                            condition = condition.replace(funcVar[val][0],currentVariableName);
                            condition = '    |' + condition + ''.join(results)+'\n';
                            f2.write(condition);
                        break;

                    else:
                        if(index == len(results)-1):
                            f2.write(someOtherLine);
            else:
                f2.write(someOtherLine);
        f1.close();
        f2.close();

        if(fl == 0):
            fl=1;
        else:
            fl=0;

        if(foundVal == 1):
            yes = True;
        else:
            yes = False;
        foundVal = 0;

    if(fl == 1):
        f2 = open(tempFilename, 'r')
    else:
        f2 = open(interFilename, 'r')

    for line in f2:

            if ("=" in line and "|" not in line and "main" not in line and "instrxx3567" not in line and "let" not in line):

                            #print line
                            results = case1.parseString( line )
                            #print results
                            newLine = line[0:line.find("=")+1] + ' trace ('
                            #print newLine
                            templine = ""
                            for i in prev_conditions:
                                    templine = templine + "NOT"+ i + ','
                            #print templine

                            templine2 = ""
                            item  = results[1:]
                            #print item
                            item = ''.join(item)
                            #print "------------------------ ", item

                            if item.isalpha():
                                    templine2 = '(' + 'x1' + "==" + "VAR" + ')' 
                            else:
                                    templine2 = '(' + 'x1' +"=="+ item + ')'
                            #print type(templine2)
                            prev_conditions.append(templine2)
                            newLine  = newLine + '"'+templine + templine2 + '"'
                            #newLine = newLine + ' val: "'

                            #for item in results[1:]:

                            #	newLine = newLine + " ++ show " + item + ' ++ " "'

                            newLine = newLine + ") "
                            newLine = newLine + line[line.find("=")+2:]
                            #print newLine
                            f3.write(line.replace(line, newLine))
            elif ("|" in line):
                #print line
                if (not '|' in prevline and prevline != '\n'):
                    #print ('------------------here-----------');
                    prev_conditions=[];
                #print "found guard"

                let_try=line[line.find('|')+1:]
                results = case2.parseString(let_try)
                #print "                      "
                #print "                      "
                #print results
                #print "                      "
                #print "                      "
                newLine = line[0:line.rfind('=')+1] + ' trace ('

                templine = ""
                for i in prev_conditions:
                        templine = templine + 'NOT' + i + ','
                if 'otherwise' not in results:
                        if variableName == '':
                                variableName = results[0]

                multiCond = []
                flag = 0;
                lastIDX = 0;
                for idx, val in enumerate(results):
                        #print idx
                        if( val == "&&" or idx == len(results)):

                                multiCond.append(''.join(results[lastIDX:idx]));
                                lastIDX = idx+1
                                #print "here here ================="
                                flag = 1;

                if(flag == 1):
                        multiCond.append(''.join(results[lastIDX:]));
                #print multiCond;
                firstTime = 1
                anotherTemp = ''
                if(len(multiCond) != 0):
                        for i in multiCond:
                                prev_conditions.append('('+ i +')')
                                if(firstTime == 1):
                                        anotherTemp = anotherTemp+'('+ i +')'
                                        firstTime = 0
                                else:
                                        anotherTemp = anotherTemp+',('+ i +')'

                        newLine = newLine + '"' + templine + anotherTemp + '"' + ')'
                        newLine = newLine + " " + line[line.rfind('=')+2:]
                        #print newLine
                        f3.write(newLine);
                else:
                        results = ''.join(results);
                        if 'otherwise' not in results:
                                results = '('+results+')'
                        else:
                                results = '('+variableName+'==VAR)'
                        #print 'results',results
                        prev_conditions.append(results)
                        newLine = newLine + '"' + templine + results + '"' + ')'
                        newLine = newLine + " " + line[line.rfind('=')+2:]
                        #print newLine
                        f3.write(newLine);
            else:
                    f3.write(line.replace(line, line))
            prevline = line;
    f1.close();
    f2.close();
    f3.close();

    print "Instrumentation Successful..."
    print "Instrumented File Generated"

if __name__ == '__main__':
    instrument();

