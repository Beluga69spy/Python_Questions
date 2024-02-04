# Add a new item to the list after a specified item
list1 = ["Lamborghini", "Buggati", "Supra", "Ferrari"]
specified_item = "Buggati"
new_item = "Thar"

try:
    index = list1.index(specified_item)
    list1.insert(index + 1, new_item)
    print(f"New item '{new_item}' added after '{specified_item}': {list1}")
except ValueError:
    print(f"Specified item '{specified_item}' not found in the list.")