# Print the 2nd highest number
numbers = [11, 54, 7, 96, 2, 33, 87, 25]
sorted_numbers = sorted(numbers, reverse=True)
if len(sorted_numbers) >= 2:
    second_highest = sorted_numbers[1]
    print("Second highest number:", second_highest)
else:
    print("The list does not have at least two numbers.")