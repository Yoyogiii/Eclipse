#Formatting Of String
a="Hi,I am Yogees"
b="How Are You"
print("Welcome",a,b)
print("Welcome",b,a)
print(a+ " Welcome " +b)
print("Welcome {} {}".format(a,b))
print("Welcome {1} {0}".format(a,b))
print("Welcome {About} {Question}".format(About=a,Question=b))