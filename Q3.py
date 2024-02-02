# Append new string in the middle of a given string
s = "Belugaa"
s1 = s[:len(s)//2] + "abc" + s[len(s)//2:]
print(s1)