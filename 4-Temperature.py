def menu():
    print("MENU\n1.Celsius\n2.Farenheit\n3.Kelvin\n4.Exit")

def celsius(t):
    if t == 2:
        return str(tempnum*(9/5)+32)+'F'
    if t == 3:
        return str(tempnum + 273.15)+'K'

def farenheit(t):
    if t == 1:
        return str((tempnum-32)*(5/9))+'C'
    if t == 3:
        return str( (tempnum-32)*(5/9)+ 273.15)+'K'

def kelvin(t):
    if t == 2:
        return str((tempnum-273.15)*(9/5)+32)+'F'
    if t == 1:
        return str(tempnum - 273.15)+'C'



TemList = []

while True: 
    menu()
    fromN = int(input("Enter the unit of temperature to be converted: "))
    if(fromN == 4):
        print(TemList)
        exit
    tempnum = float(input("Enter the value of temperature: "))
    toN = int(input("Enter the unit of temprature to convert to: "))
    
    if(toN == 4):
        print(TemList)
        exit

    if(fromN == 1):
        newtemp = celsius(toN)
        print("Converted value is : ",newtemp)
        TemList.append(str(tempnum)+'C -> '+newtemp)
    elif(fromN == 2):
        newtemp = farenheit(toN)
        print("Converted value is : ",newtemp)
        TemList.append(str(tempnum)+'F -> '+newtemp)
    elif(fromN == 3):
        newtemp = kelvin(toN)
        print("Converted value is : ",newtemp)
        TemList.append(str(tempnum)+'K -> '+newtemp)
    else: 
       print("Please enter a valid option! ")










