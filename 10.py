#operator precedence
#0. parenthesis
#1. first- exponentiation 2 ** 3
#2. second- multiplication or division
#3. third- addition or subtraction

x = 10 + 3 * 2
print(x)

x = 10 + 3 * 2 ** 2
print(x)

x = (10 + 3) * 2 ** 2
print(x )

x = (2 + 3) * 10 - 3
print(x)