# Create a new string made of the first, middle, and last characters of each input string
s1 = "Beluga"
s2 = "Skittle"
s3 = "Hecker"
s = s1[0] + s2[len(s2)//2] + s3[-1]
print(s)