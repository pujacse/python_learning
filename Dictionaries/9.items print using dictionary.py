# Print all values in the dictionary, one by one

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for item in thisdict.keys():
    print(item)

for item, value in thisdict.items():
    print(item, value)