my_tuple = (1, 2, 3, 4, 5)
element_to_remove = 3
new_elements = []

for element in my_tuple:
    if element != element_to_remove:
        new_elements.append(element)
new_tuple = tuple(new_elements)
print("New tuple after removing element 3:", new_tuple)