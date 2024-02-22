# Convert a tuple of integers to a tuple of strings.

tuple1 = (1, 2, 3, 4, 5)
string_list = []
for element in tuple1:
    string_list.append(str(element))
string1 = tuple(string_list)
print("Tuple of string: ", string1)