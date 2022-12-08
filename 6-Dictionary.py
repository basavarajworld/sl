elements = {
   "H": "Hydrogen",
   "He": "Helium",
   "C": "Carbon",
   "N": "Nitrogen",
   "Al": "Aluminium"
}

print("Initial elements in list are: ",elements)

symbol = input("Enter a new symbol: ")
name = input("Enter the element's name: ")
elements.update({symbol : name})

print("Elements in the dictionary now: ",elements)

print("Number of atomic elements in dictionary: ",len(elements))

a = input("Enter an element to search: ")
if a in elements:
   print("element found: ",elements.get(a))
else: 
   print("Element not found!")
