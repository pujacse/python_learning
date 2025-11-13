# Two variables a = 5, b = 10. Swap their values so that a becomes 10 and b becomes 5.
# (Use a temporary variable and then try without temporary.)

a = 5
b = 10
temp = a
a = b
b = temp
print(a,b)

# without temp
a = 5
b = 10
a, b = b, a
print(a, b)