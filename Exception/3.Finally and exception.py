# Finally exception:

# The finally block, if specified,
# will be executed regardless if the try block raises an error or not.

try :
    list = [20,0,30]
    result = list[0] / list[3]  # index 3 is not possible in this list
    print("result")
    print("Done")

except ZeroDivisionError:
    print("Dividing by zero is not possible")

finally:
    print("successful")