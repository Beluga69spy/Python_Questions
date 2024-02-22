# Count the number of even and odd numbers in a tuple

tuple1 = (1, 2, 3, 4, 5, 6)
even = 0
odd = 0
for element in tuple1:
    if element % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers: ", even)
print("Odd numbers: ", odd)