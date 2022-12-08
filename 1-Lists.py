numList = []
n = int(input('Enter the size of the list: '))
print('Enter the elements now')
for i in range(0,n):
    ele = int(input())
    numList.append(ele)

print('The list elements are:',numList)

print("The maximum element is: ",max(numList))
print("The minimum element is: ",min(numList))

ele=int(input("Enter a new element into List: "))
numList.append(ele)

print('The list elements are:',numList)

dele = int(input('Enter a number in list to be deleted: '))

if dele in numList:
    numList.remove(dele)
    print('The list elements are:',numList)
else:
    print("Element not found!!")


    



