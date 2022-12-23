#List Using ZIP
a=[1,2,3,4,5,6,7,8,9]
b=[100,200,300,400,500,600,700,800,900]
c=zip(a,b)
print(list(c))

#Tuple Using ZIP
a=(1,2,3,4,5,6,7,8,9)
b=("Apple","Mango","Grapes","Guava","Apple","Mango")
c=zip(a,b)
print(tuple(c))

#Set Using ZIP
a={1,2,3,4,5,6,7,8,9}
b={"Apple","Mango","Grapes","Guava","Apple","Mango"}
c=zip(a,b)
print(set(c))

BP=[100,200,300,400,500]
SP=[600,700,700,700,1000]
P=zip(BP,SP)
for  BP,SP in P:
    if BP<SP:
        x=SP-BP
        print("Profit",x)
    elif BP > SP:
        x = BP-SP
        print("Profit", x)


