import sys
from functools import reduce
from collections import Counter
f = open("file.txt")
contents = f.read().split()
dict = Counter(contents)
print("Number of occurences of words in the file: ")
print(dict)

s = sorted(dict.items(), key = lambda x:x[1], reverse= True)  
#.items() converts key-value pair to tuples , and
#  x[1] is the second element in the tuple which is the number of occurence.

print("Top 10 occuring words: ")
print(s[:10])

print("The length of each word : ")
wordlen = [len(x) for x,y in s[:]]
print(wordlen)


avg = reduce(lambda x,y: x+y, wordlen)/len(wordlen)
print("Average length of words is: ",avg)

odd_sq = [x*x for x in wordlen if x%2 !=0]

print("The squares of odd number of wordlen is : ",odd_sq)






