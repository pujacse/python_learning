# Exception:

try:
    age = int(input("Enter your age: "))

    income = 20000
    risk = income / age

    print(age)

except ValueError:
    print("Invalid value")

except ZeroDivisionError:
    print("Dividing by zero is not possible")