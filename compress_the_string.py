# This program accepts an input string S and for every character c that repeats
# consecutively replaces with x the number of times it repeats and displays
# the number of times the character repeats consecutively followed by the character 
# separated by a comma.
# Input: A single line of input consisting of the string s.
# Output: A single line of output consisting of the modified string.
from itertools import groupby
s = input().strip()
arr = list(s)
for digit, group in groupby(arr):
    count = len(list(group))
    print(f"({count}, {int(digit)})", end=" ")


