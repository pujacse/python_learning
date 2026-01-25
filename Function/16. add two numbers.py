# 1. add two numbers:

def add_numbers(a,b):
    return a + b

sum = add_numbers(2,3)
print("sum: ",sum)


# 2. square of a number:

def square_of_a_number(num):
    return num * num

square = square_of_a_number(5)
print("square of a number is: ",square)


# 3. even odd check

def check(num):

    if num % 2 == 0:
        return "even"

    else:
        return "odd"

number = check(5)
print(number)

# 4. convert celsius to fahrenheit:

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print ("convert: ",celsius_to_fahrenheit(20))


# 5. find out the maximum number:

def max_number(a, b, c):
    if a<b and c>b:
        return "b"
    elif b<a and c<a:
        return "a"
    else:
        return "c"

maximum_number = max_number(2,1,5)
print("maximum number is: ",maximum_number)
