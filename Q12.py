# How to find a substring in a given string using string slicing ?
s = "Prithwiraj"
sub = "raj"
for i in range(len(s)):
    if s[i:i+len(sub)] == sub:
        print(f"The substring '{sub}' is found at index {i} in the string '{s}'")
        break
else:
    print(f"The substring '{sub}' is NOT found in the string '{s}'")
