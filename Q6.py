# Count all letters, digits, and special symbols from a given string
s = "#Hello@123%#"
letter = 0
digit = 0
special = 0
for char in s:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        digit += 1
    else:
        special += 1
print("No of Letter:", letter)
print("No of Digit:", digit)
print("No of Special Symbol:", special)