# Find all occurrences of a substring in a given string by ignoring the case

def find(string, substring):
    string_lower = string.lower()
    substring_lower = substring.lower()
    occurrence  =[]
    for i in range(len(string_lower)):
        if string_lower.startswith(substring_lower, i):
            occurrence.append(i)
    return occurrence
string = "The quick brown fox jumps over the lazy dog"
substring = "the"
occurrence = find(string, substring)
print("Occurrences of '{}' :".format(substring))
print(occurrence)