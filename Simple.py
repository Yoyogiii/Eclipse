a=5
print(a ** 2)

#Precedence Operator
print(a+5-10)

#String Manipulation
#Length
str1="Yogeeswaran"
print(len(str1))
#Replace
print(str1.replace("Yogees","Yogesh"))

#Get the value
str1="Yogii"
print(str1[4])

#Change The Type
z=7620
c = str(z)
print(type(c))

#Operation Of String
#Find()
p="HelloWorld"
print(p.find("l"))
print(p.find("o"))
#UpperCase
print(p.upper())
print(p)
#Count The character
print(p.count('l'))
print(p.isupper())
#Repeat a String
o="Good Morning" * 2
print(o)
#Remove the space
x=" Good Evening "
print(x)
print(x.strip())
print(x.lstrip())
print(x.rstrip())
v="thiruvananthapuram"
print(v)
print(v.replace("a","o").upper())

#Multiline Strings
long="""Hii,
How are you,
Bye"""
print(long)

#Title-it will change the first letter capital
ab="this is my program"
print(ab.title())

#Split the String
ab1="Supplementing with selenium may provide a way to enhance your thyroid function in a natural way"
print(ab1.split('selenium'))

#Swap
m="ThiS is MY ProGram"
print(m.swapcase())

#Escape
y="Yogees \" waran"
print(y)

#Check String is empty
str4=''
if not str4:
    print("My string is Empty")
str5 = 'Hii'
if str5:
 print("My string is Not Empty")

#
 o="Vishakhapattinam is a beautiful city in the south"
print(o)
print('is' in o)
print('what' in o)




