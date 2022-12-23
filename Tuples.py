#Tuples
tuple=("Apple","Mango","Grapes","Guava")
print(tuple)

#Its Allow Duplicate Values
tuple=("Apple","Mango","Grapes","Guava","Apple","Mango")
print(tuple)

#Membeship Operator
print("Mango" in tuple)
print("Fruit" in tuple)

#Length
tuple=("Apple","Mango","Grapes","Guava","Apple","Mango")
print(len(tuple))
tuple=("Apple","Mango","Grapes","Guava")
print(len(tuple))

# DataTypes
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))

#Access Tuple
tuple_1=("Cat","Dog","Fish","Lion","Tiger","Hen","Duck","Cow")
print(tuple_1[2])

#Access Tuple With Negative Indexing
print(tuple_1[-1])

#Access Tuple With Range
print(tuple_1[2:5])

# If Give Like This it Will print before the 5th Value
print(tuple_1[:5])

# If Give Like This it Will print After the 5th Value
print(tuple_1[5:])

#Access Tuple With Negative Indexing and Range
print(tuple_1[-5:-2])

#Check
if "Cow" in tuple_1:
    print("Cow in the tuple")
if "Crow" in tuple_1:
    print("Crow is Not in the tuple")

#Count
a={1,2,3,4,5,6,3,2,1}