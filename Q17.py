# Replace a list’s item with a new value if found
list1 = ["apple", "banana", "cherry", "date"]
old_value = "banana"
new_value = "orange"

try:
    index = list1.index(old_value)
    list1[index] = new_value
    print(f"Item '{old_value}' replaced with '{new_value}': {list1}")
except ValueError:
    print(f"Item '{old_value}' not found in the list.")