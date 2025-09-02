# Max & Min in List - Write a program to find
# the largest and smallest element in a list.

My_list = [5,3,6,9,10,33,2,20,5,55,22]

largest_element = My_list[0]
smallest_element = My_list[0]

for item in My_list:
    if item > largest_element:
        largest_element = item
    elif item < smallest_element:
        smallest_element = item

print(f"Largest element: {largest_element}")

print(f"Smallest element: {smallest_element}")