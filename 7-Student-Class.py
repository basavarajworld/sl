class Student: 
    def __init__(self):
       pass
    def accept(self):
        self.name = input("Enter Student name: ")
        self.age = input("Enter Student age: ")
        m1 = int(input("Enter the marks os subject 1: "))
        m2 = int(input("Enter the marks os subject 2: "))
        m3 = int(input("Enter the marks os subject 3: "))
        self.marks = [m1,m2,m3]
    def display(self):
        print("Name of the Student: ",self.name)
        print("Age of the Student: ",self.age)
        print("Marks of the Student: ",self.marks)

s1 = Student()
s1.accept()
print("*****Student Details*****")
s1.display()