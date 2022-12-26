list1=[1,2,3,4,5,6,7,8,9,10]
for x in list1:
    print(x)

#print all odd and even number till 100 using range function
for even in range(1, 100 ):
    if even % 2 == 0:
        print(even, end=" ")
print("\n")
for odd in range(1, 100):
    if odd % 2 != 0:
        print(odd, end=" ")

#print table of 23 till 10 using range
num=24 #Store variable 24 in Num
for i in range(1, 11): #Range=1 to 10
   print(i, 'x', num, '=', i*num) # 1*24=24 ,2*24=48

#print all even and odd using only range not condition satement
#odd
for i in range(1,100,2):
    print(i,end= ' ')
print("\n")
#Even
for i in range(0,100,2):
    print(i, end=' ')

