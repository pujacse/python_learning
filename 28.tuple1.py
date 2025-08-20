#tuple

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
print(thistuple[1])
print(thistuple[-3])

thistuple = tuple(("apple","banana","cherry","orange","kiwi","melon","mango"))
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))