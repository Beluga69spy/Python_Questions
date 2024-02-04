# Calculate the sum and average of the digits present in a string
string = "Hello 123 hi 456"
digits = []
for char in string:
    if char.isdigit():
        digits.append(int(char))
sum_digits = sum(digits)
if len(digits) > 0:
    average = sum_digits / len(digits)
else:
    average = 0
print("Sum of digits: ", sum_digits)
print("Average of digits: ", average)