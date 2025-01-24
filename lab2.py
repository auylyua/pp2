#Python Booleans
'''The following will return False:'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#Python Operators
print(100 + 5 * 3) #the result is -> 115

#Python Lists
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #the result is -> 3

#Access List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#the result is -> ['cherry', 'orange', 'kiwi']

#Change List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)#the result is -> ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)#the result is -> ['apple', 'orange', 'banana', 'cherry']

#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#the result is -> ['apple', 'cherry']

#loop Lists
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])#the result is -> apple banana cherry

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)#the result is -> ['apple', 'banana', 'kiwi']

#Sort Lists
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)#the result is -> [100, 82, 65, 50, 23]

#Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #the result is -> ['apple', 'banana', 'cherry']

#Join Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Python Tuples
thistuple = ("apple",)
print(type(thistuple)) #the result is -> <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #the result is -> <class 'str'>

#Access Tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#the result is -> ('cherry', 'orange', 'kiwi')

#Update Tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) 
print(thistuple) #the result is -> ('banana', 'cherry')

#Unpack Tuples
'''If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be assigned to the variable as a list:'''
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)#the result is -> apple
print(tropic)#the result is -> ('mango', 'papaya', 'pineapple')
print(red)#the result is -> cherry

#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) #the result is -> apple banana cherry

#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Python Sets
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)#the result is -> {False, True, 'apple', 'banana', 'cherry'}

#Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Add Set Items
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Remove Set Items
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

#Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Access Items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Change Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Add Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Remove Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Loop Dictionaries
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Copy Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

#Python If...Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")#the result is -> b is greater than a

#Python While Loops
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) #the result is -> 1 2 4 5

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #the result is -> apple