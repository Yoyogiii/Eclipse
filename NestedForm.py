a=["java","python","html","C++"]
for x in a:
    for y in x:
        print(y,end= '')


b="Yogees"
for z in b:
    print(z)

list1=[["a","b","c"],["Aus","India","China","Japan"]]
for x in list1:
    for q in x:
        print(q)




list4=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
for b,c in list4:
        print("My Country is" +b+ "and I live in" +c )

#Dictionary TypeCasting
dict1=dict(list4)
print(dict1)

for m,n in dict1.items():
    print(m,n)

#Tuple Typecasting
tuple1=tuple(list4)
print(tuple1)

#Set
list5=["pen","pencil","Eraser"]
set1=set(list5)
print(set1)
