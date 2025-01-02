import json

import time

seedList = ["dlp","bag","rtm","ieo"] 

def allLetterUsedCheck(needleList, haystack):

    needle = ""

    for wordCheck in needleList:

        needle = needle + wordCheck

    for i in range (0,len(needle)):

        if (needle[i] in haystack):

            haystack.remove(needle[i])

            #print(needle, haystack, len(haystack))

    if (len(haystack) <=0):

        retValue = True

    else:

        retValue = False

    return retValue

 

def getLastLetterInList(nextPassLineList):

    lastword = nextPassLineList[-1]

    #print (lastword)

    lastletter = lastword[-1]

    #print (lastletter)

    return lastletter

 

def getNextWordList(searchLetter,fullList):

    searchList = []

    for x in fullList:

        if x[0] == searchLetter:

            searchList.append(x)

    #print (searchList)

    return searchList

 

print("This is boxWord")



wordList = []

 

possibleLetters = []

for x in seedList:

    for i in range(0,3):

        possibleLetters.append(x[i])

print ("Possible Letters : ",possibleLetters)

 

impossibleCombinations = []

for x in seedList:

    #print ("This is X:",x)

    for i in range(0,3):

        for j in range (0,3):

            impossibleCombinations.append(x[i]+x[j])

            #print (x,i,x[i],j,x[j])

    print("Impossible combinations : ", impossibleCombinations)

 

impossibleLetters = [ "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]

for x in seedList:

    impossibleLetters.remove(x[0])

    impossibleLetters.remove(x[1])

    impossibleLetters.remove(x[2])

print("Impossible Letters :", impossibleLetters)

 

#with open('common-short.txt') as f:

with open('words_alpha.txt') as f:

    wordList = f.read().splitlines()

wordListIndex = len(wordList) -1

#print(type(wordList))

 

#wordListIndex = 99

while wordListIndex:

    wordListIndex = wordListIndex-1

    x = wordList[wordListIndex]

 

    resLetters = any(ele in x for ele in impossibleLetters)

    if resLetters:

        wordList.pop(wordListIndex)

    else:

        resCombinations = any(ele in x for ele in impossibleCombinations)

        #print(res)

        if resCombinations:

            #print("XXXXIMPOSSIBLEXXXX:", wordListIndex, x, impossibleCombinations )

            #wordList.remove(x)

            wordList.pop(wordListIndex)

        elif len(x)<3:

            #print("XXXX LENGTH   XXXX:", wordListIndex, x, impossibleCombinations )

            wordList.pop(wordListIndex)

         

    if not(wordListIndex % 100000):

        print(wordListIndex)

   

 

wordListByLen = sorted(wordList, key=len, reverse=True)

 

#print(len(wordList))

 

targetList = []

foundList = []

 

#for firstPass in wordListByLen:

for firstPass in wordList:

    foundLine = []

    foundLine.append(firstPass)

    workingPossibleLetters = possibleLetters.copy()

    #print("Possible Letters: ", possibleLetters)

    if allLetterUsedCheck(foundLine,workingPossibleLetters):

        #print("Adding to FoundList in First Pass :", foundLine, possibleLetters.copy())

        foundList.append(foundLine)

    else:

        targetList.append(foundLine)

    #print("Possible Letters: ", possibleLetters)

 

maxDepth = 0

i=0

while i<len(targetList) and (maxDepth < 2) :

    workingLineList = targetList[i].copy()

    searchLetter = getLastLetterInList(workingLineList)

    nextWordOptionList = getNextWordList(searchLetter,wordList)

    for newWordToAdd in nextWordOptionList:

            if newWordToAdd == workingLineList[-1]:

                #print ("Ignoring repeated word ::: ", workingLineList, newWordToAdd)

                dummy=0

            else:

                workingLineList.append(newWordToAdd)

                #print("New List Line - ", workingLineList)

                workingPossibleLetters = possibleLetters.copy()

                if allLetterUsedCheck(workingLineList,workingPossibleLetters):

                    foundList.append(workingLineList)

                    print("Added to FoundList",workingLineList)

                else:

                    #if workingLineList in targetList:

                    #    print("Found Already :", workingLineList)

                    #else:

                        targetList.append(workingLineList)

                        #print("Added to TargetList", workingLineList)

                workingLineList = targetList[i].copy()

                #print("-------------------------------------")

    maxDepth = len(workingLineList)

    #print("maxDepth is", maxDepth)

    i=i+1

    if not (i % 1000):

        print("Checking Index : ",i, len(targetList),workingLineList)

 

for xLines in foundList:

    print (xLines)









#print(foundList)

 

#allLetterUsedCheck(["abdklmnopqrt"], possibleLetters)

#allLetterUsedCheck(["aklmnopqrt"], possibleLetters)

#allLetterUsedCheck(["aaaaaaabcdefghijklmpqrt"], possibleLetters)

 

print("boxWord Complete")

 

 
