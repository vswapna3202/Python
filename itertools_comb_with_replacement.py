# This program accepts a string S and integer k and prints all k possible replacement
# combinations of the string in lexicographic sorted order.
# Input: A single line containing the string S and integer value k separated 
#        by a space.
# Output: All k possible replacement combinations of the string in lexicographic 
#         sorted order.
from itertools import combinations_with_replacement
S, k = input().split()
sorted_string = "".join(sorted(S))
combo_arr = list(combinations_with_replacement(sorted_string, int(k)))
for letter in combo_arr:
    print("".join(letter))
    