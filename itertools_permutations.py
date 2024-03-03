# This program accepts input string S and integer k and prints all possible
# k permutations of string S in lexicographic sorted order
# Input: A single line containing the space separated string S and the integer 
#        value k.
# Output: All possible k permutations of string S printed in lexicographic sorted 
#         order in separate lines.
from itertools import permutations
S, k = input().split()
sorted_string = "".join(sorted(S))
result_arr = list(permutations(sorted_string, int(k)))
for item in result_arr:
    print("".join(item))
