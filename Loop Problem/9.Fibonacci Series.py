#Q9. Print Fibonacci series up to 10 terms

a , b = 0 , 1

count = 1

while count < 11:
    print(a, end=" ")

    a,b = b,a+b
    count = count + 1