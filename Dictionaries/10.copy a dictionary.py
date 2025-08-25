# copy a dictionary

# Make a copy of a dictionary with the copy() method:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
copy = thisdict.copy()
print(copy)

#another way:

copy = dict(thisdict)
print(copy)