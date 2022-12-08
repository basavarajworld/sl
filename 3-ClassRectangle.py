class Rectangle:
    def __init__(self,l,b):  #type two _ _ together for init 
        self.l = l
        self.b = b
        
    def area(self):
        return self.l*self.b

x = int(input("Enter the length: "))
y = int(input("Enter the breadth: "))
obj = Rectangle(x,y)
print("Area of the rectangle is: ",obj.area())