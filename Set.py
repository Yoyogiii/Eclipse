set1={'America','China','India','Japan','Australia','Africa','Amazon'}
set2={'Thailand','Malaysia','Singapore','India','Japan','Brazil'}
#Add
set2.add('Asia')
print(set2)
set2.add('France')
print(set2)

#Copy
# place=set1.copy()
# place1=set2.copy()
# print(place)
# print(place1)

#Difference
a=set1.difference(set2)
print(a)
b=set2.difference(set1)
print(b)

#Difference Update
set1.difference_update(set2)
print(set1)

#Discard
set3={'a','b','c','d','f','e','g','h',}
set3.discard('h')
print(set3)

#Intersection
set4={'h','i','j','k','l','m','c','d','g'}
z=set3.intersection(set4)
print(z)

#Intersection Update
set3.intersection_update(set4)
print(set3)

#Disjoint -Compare Both sets if two sets have different Values it print True.
x={1,2,3,4,5,6,7,8}
y={9,10,11,12,13,14,1}
print(x.isdisjoint(y))

#Subset - all value in m is present in n its true
m={1,2,4}
n={1,2,4,5,6,7}
print(m.issubset(n))

#Superset - All value in n is present in m its true
m={1,2,4,6,7}
n={1,2,4}
print(m.issuperset(n))

#Pop
check={1,3,2,5,6,7}
check.pop()
print(check)
check.pop()
print(check)

#Remove
m.remove(4)
print(m)

#Symmetric Difference -Remove the same item in both set and add the remaining set in same set
o={6,7,8,9,1,2}
m={6,7,4,99}
print(o.symmetric_difference(m))

#Union-Contains both values from the set and exclude a duplicate value
a1={'Cat','Dog','Cow','Hen','Goat'}
a2={'Cat','Horse','Mouse','Rabbit','Goat',}
print(a1.union(a2))













