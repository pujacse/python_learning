# A basic decorator that uppercases the return value of the decorated function

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())