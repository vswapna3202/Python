# This program finds the probability of atleast one of the k indices containing
# letter 'a' for input of N space-separated lower case english letters and K being
# the number of indices to select to check the probability.
#  Input: The first line contains the integer N, denoting the length of the list.
#         The next line consists of N space-separated lowercase English letters, 
#         denoting the elements of the list.
#         The third and the last line of input contains the integer K, denoting the number 
#         of indices to be selected.
# Output: Output a single line consisting of the probability that at least one of  
#         the K indices selected contains the letter:'a'.
# Note: The answer is corrected up to 3 decimal places.
# Import relevant libraries
from itertools import combinations

# Input the length of the list
n = int(input())

# Input the lower case space separated english letters
letters = input().split()

# Input the number of indices to be selected
k = int(input())

# Find all unordered combinations of letters of length 2
unordered_tuples = list(combinations(letters, k))

# Find the number of combinations having the letter 'a' from all
# unordered tuples
tuples_with_a = sum(1 for t in unordered_tuples if 'a' in t)

# Calculate the probability which is count of tuples having 'a' divided by
# total number of unordered tuples
probability = tuples_with_a / len(unordered_tuples)

# Print the probability by correcting it to 3 decimal places
print("{:.3f}".format(probability))
