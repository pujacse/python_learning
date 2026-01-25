# using *kwargs function:

def my_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

my_keyword_arguments(a = 1, b = 2, c = 3, d = 4)