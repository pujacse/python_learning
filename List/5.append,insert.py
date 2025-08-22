#List method / List function

numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.remove(2)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

numbers = [5, 2, 1, 5, 7, 4]
print(numbers.index(5))
print(50 in numbers)
print(numbers.count(5))
