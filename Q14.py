# Remove empty strings from the list of strings
original_list = ["Beluga", "", "Skittle", "", "Hecker", ""]
filtered_list = list(filter(None, original_list))

print(filtered_list)