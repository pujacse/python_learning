#string concatenation or format string
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print (message)
msg = f"{first} [{last}] is a coder"
print (msg)

#string methods
course =  "python for beginners"
print(len(course))

#lower and upper case
course =  "python for beginners"
print(course.upper())
print(course.lower())
print(course)

#find character
course =  "python for beginners"
print(course.find('p'))
print(course.find('o'))
print(course.find('beginners'))

#character fide and replace method
course =  "python for beginners"
print(course.replace('beginners','absolute beginners'))