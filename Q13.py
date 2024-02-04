# What will be the code block if we can’t find a substring within a string.
s = "Prithwiraj"
sub = "xzd"
for i in range(len(s)):
    if s[i:i+len(sub)] == sub:
        print(f"The substring '{sub}' is found at index {i} in the string '{s}'")
        break
else:
    print(f"The substring '{sub}' is NOT found in the string '{s}'")