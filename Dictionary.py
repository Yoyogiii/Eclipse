a={"url1":"google.com","url2":"amazon.com"}
b={1:"Yogee",2:"Sivakasi"}
print(b[1])
print(a["url1"])#url1(key)p
b[3]="Flipkart"
print(b)
print(b.get(2))
print(b.keys())     # It Will Print the keys In Dictionary
print(b.values())   # It Will Print the Values In Dictionary
print(b.items())    #It Will Print the item in Dictionary and It will print it in tuples
c={ "Name":"Yogee",
    "Dept":"CSE",
    "Age":"21",
    "DOB":"June 7",
    "Place":"Svks",
    "State":"TN",
    }
#REMOVE
print(b.pop(3))
print(b.items())
b.popitem()
print(b.items())
#Update
print(c)
c.update({"Place":"SIVAKASI"})
print(c)

