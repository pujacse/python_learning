list1=[1, 'python',2,'is',3,'awesome']

list1.append(4)
print(list1)

list1.append([7,7])
print(list1)

list1.extend([5,6])
print(list1)

list1.remove(2) # only remove for mentioned position value
print(list1)

del list1[1] # only delete for mentioned index
print(list1)