# Access Items in Nested Dictionaries:

# To access items from a nested dictionary,
# you use the name of the dictionaries,starting with the outer dictionary:

myfamily = {
    "child1" : {
        "name" : "puja das",
        "birth" : 2002,
        "age" : 23
    },
    "child2" : {
        "name" : "mitu",
        "birth" : 2002,
        "age" : 22
    },
    "child3" : {
        "name" : "kina",
        "birth" : 2001,
        "age" : 20
    }
}
print(myfamily["child1"]["name"])
print(myfamily["child2"]["birth"])