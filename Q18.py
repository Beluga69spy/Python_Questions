# Remove all occurrences of a specific item from a list
my_list = [1, 2, 3, 2, 4, 2, 5]
item_to_remove = 2

while item_to_remove in my_list:
    my_list.remove(item_to_remove)

print("List after removing all occurrences of", item_to_remove, ":", my_list)