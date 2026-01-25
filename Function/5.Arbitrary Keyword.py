# Arbitrary Keyword Arguments, **kwargs:
def my_keyword_arguments(**kwargs):
    for key , value in kwargs.items():
        print(key, value)

my_keyword_arguments(a = 1, b = 2, c = 3, d = 4)
my_keyword_arguments(x = 's',y = 'e')