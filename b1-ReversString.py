class RevString:
    reverse = ""
    vowels = ['a','e','i','o','u']
    
    def __init__(self,sentence):
        self.sentence = sentence
        
    def reverse(self):
            return " ".join(reversed(self.sentence.split()))
    def vowelcnt(self):
            return sum(x in self.vowels for x in self.sentence)     

items =[]
for i in range(0,3):
       objrev = RevString(input("Enter a Sentence: "))
       print("The reversed sentence is: ",objrev.reverse())
       items.append(objrev) 

print("*****displaying in descending order of number of vowels*****") 

for i in sorted(items, key = lambda item:item.vowelcnt(), reverse= True):
    print(i.reverse(), "->",i.vowelcnt())