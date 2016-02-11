'''
Author:Fei
'''

import sys

openNeg=open('negative-words.txt')
openPos=open('positive-words.txt')
setNeg=set()
setPos=set()
dicNeg=dict()
dicPos=dict()


for lines in openNeg:
	setNeg.add(lines.strip())

for lines in openPos:
	setPos.add(lines.strip())

inputFileOpen=open('input.txt')

for lines in inputFileOpen:
	words=lines.split()
	for word in words:
		if word in setPos:
			if word not in dicPos:
				dicPos[word]=1
				continue
			else:
				dicPos[word]+=1
				continue
		if word in setNeg:
			if word not in dicNeg:
				dicNeg[word]=1
				continue
			else:
				dicNeg[word]+=1
				continue

print 'neg:' 
print '--------------'
print dicNeg

print 'pso:'
print '--------------'
print dicPos

listNeg=list()
listPos=list()
for num in dicNeg:
	listNeg.append(dicNeg[num])
for num in dicPos:
	listPos.append(dicPos[num])

for negWord in dicNeg:
	if dicNeg[negWord]==max(listNeg):
		print 'Most number neg word:'
		print '------------------'
		print negWord
		break

for posWord in dicPos:
	if dicPos[posWord]==max(listPos):
		print 'Most number pos word:'
		print '------------------'
		print posWord
		break
