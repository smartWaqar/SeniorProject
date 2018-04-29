#!/usr/bin/env python3


##############################################
############ Version 1 #######################
# Works for cases where:
# Only 1 function
# Function has only 1 variable
# Pattern matcing with equal and not equal
##############################################
##############################################



import os
from pyparsing import *
os.chdir(os.getcwd())




case1 = Word(alphanums) + ZeroOrMore(Word(alphanums) | Literal('-'))

f1 = open('src.hs', 'r')
f2 = open('factorial_trace2.hs', 'w')
results = ""
newLine=""


prev_conditions = []


for line in f1:
	if ("=" in line and "main" not in line and "instrxx3567" not in line and "let" not in line):
			print line
			results = case1.parseString( line )
			print results

			newLine = line[0:line.find("=")+1] + ' trace ('

			templine = ""

			for i in prev_conditions:
				templine = templine + "NOT"+ i + ','


			templine2 = ""
			item  = results[1:]
			item = ''.join(item)
			print "------------------------ ", item

			if item.isalpha():
				templine2 = '(' + 'x1' + "==" + "VAR" + ')' 
			else:
				templine2 = '(' + 'x1' +"=="+ item + ')'


			print type(templine2)

			prev_conditions.append(templine2)

			newLine  = newLine + '"'+templine + templine2 + '"'

			#newLine = newLine + ' val: "'
			#for item in results[1:]:
			#	newLine = newLine + " ++ show " + item + ' ++ " "'

			newLine = newLine + ") "
			newLine = newLine + line[line.find("=")+2:]
			print newLine
			f2.write(line.replace(line, newLine))
	else:
		f2.write(line.replace(line, line))


f1.close()
f2.close()
