# Loop dictionaries

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for key in thisdict:
    value = thisdict.get(key)
    print(key, value)