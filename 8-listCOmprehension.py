# numList = [88,69,76,10,83,33]
from functools import reduce #dont forget to import it


numList = []
print("Enter 6 numbers to list: ")
for i in range(0,6):
    temp = int(input())
    numList.append(temp)

print("The original list is: ",numList)

newList = [3*x for x in numList ]
print("The new list after multiplying by 3: ",newList)

sum1 = reduce(lambda x,y: x+y, numList)
sum2 = reduce(lambda x,y: x+y,newList)

print("The sum of original list is : ",sum1)
print("The sum of new list is : ",sum2)

