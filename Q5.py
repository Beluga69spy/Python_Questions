# Arrange string characters such that lowercase letters should come first
s = "PriThwiRajMazumDaR"
for char1 in s:
    if 'a' <= char1 <= 'z':
        print(char1, end=' ')
for char2 in s:
    if 'A' <= char2 <= 'Z':
        print(char2, end=' ')
print()