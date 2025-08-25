# nested dictionaries

myfamily = {
    "child1" : {
        "name" : "puja",
        "year" : 2002
    },
    "child2" : {
        "name" : "payel",
        "year" : 2003
    },
    "child3" : {
        "name" : "kemi",
        "year" : 2004
    }
}
print(myfamily)

# Or, if you want to add three dictionaries into a new dictionary:

child1: {
    "name": "puja",
    "year": 2002
}
child2: {
    "name": "payel",
    "year": 2003
}
child3: {
    "name": "kemi",
    "year": 2004
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3": child3
}
print(myfamily)