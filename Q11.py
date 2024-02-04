# How to find a substring in a given string ?
s = "Prithwiraj"
sub = "raj"
find = s.find(sub)
if find != -1:
    print(f"The substring '{sub}' is found at the index '{find}'")
else:
    print(f"The substring '{sub}' is NOT found in the string '{s}'")