a=[20,10,5,2,50,60]
maxi=a[0]   #Maxi = 20

#Greatest Number
for i in range(len(a)): #It will get length of the list and loop it
    if maxi < a[i] : # 20<10 20<5 20<2 20<50=true,now maxi is 50,next loop it will check 50<60 its is true in maxi the value is 60
        maxi=a[i]   #maxi=60
    i=i+1
print("The Greatest Value in the List is",maxi)

#Smallest Number
mini=a[0] #Mini=20
for i in range(len(a)):
    if mini > a[i] :
        mini=a[i]
print("The Smallest Value in the List is",mini)
