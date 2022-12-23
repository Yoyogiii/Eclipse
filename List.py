#List
List=["abc", 34, True, 40, "male",222,"Cow","Man",False]
print(List[2])
print(List[3])
print(List[-2])
print(List[2:4])
print(List[-4:-1])
print(List[-4:])
print(type(List))

#List Method
#Append Means Adding Something In The List
pet=["Dog","Cat","Cow","Hen","Goat"]
pet.append("Parrot")
print(pet)

#Extend means Joining one to another list
wild=["Lion","Tiger","Hyena","Elephant","Leopard"]
pet.extend(wild)
print(pet)

#Copy means Copying the pet list and past it in the Animal
Animal=pet.copy()
print(Animal)

#Count means counting number of values by given value
Animal.append("Lion")
print(Animal)
x=Animal.count("Lion")
print(x)

#Insert a value in between list using index
Animal.insert(3,"Hippo")
print(Animal)

#Pop means Remove the data from the list using "Index"
Animal.pop(7)
print(Animal)

#Remove the data from the list using "Value"
Animal.remove('Hyena')
print(Animal)

#Reverse the List
Animal.reverse()
print(Animal)

#Sort the list in ascending
Animal.sort()
print(Animal)

#Sort the list in descending
Animal.sort(reverse=True)
print(Animal)

#len means finding length of the List
print(len(Animal))


