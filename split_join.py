# This program splits an input string based on space and then joins them again with
# hyphen
# Input: input string in a single line separated with spaces
# Output: input string in a single line separated with hypen (-)
def split_and_join(string):
    arr = string.split()
    return "-".join(arr)

line = input()
result = split_and_join(line)
print(result)
