"""
A SCRIPT THAT FINDS THE NEGATIVE WORD THAT APPEARS IN THE MOST REVIEWS.
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex


#load the positive and negative lexicons
negLex=loadLexicon('negative-words.txt')

freq=dict()

data_conn=open('input.txt')
for line in data_conn: # for every line in the file (1 review per line)
    negSet=set() #list of unique negative words in the review

    line=line.strip()    
    words=line.split(' ') # slit on the space to get list of words
    
    for word in words: #for every word in the review
        if word in negLex: # if the word is in the negative lexicon
            negSet.add(word) #update the negative set for this review
           
   
    for word in negSet:
        if word in freq:
            freq[word]=freq[word]+1
            #freq[word]+=1
        else:
            freq[word]=1


for word in freq:
    print word, freq[word]

#go over the frequencies and find the pos word with the highest one
winner=None# initial value for winner
maxF=-1# initial value for winner's frequency
for term in freq:  
    if freq[term]>maxF: # if this freq is higher than the best so far
        maxF=freq[term]
        winner=term

print winner

data_conn.close()
