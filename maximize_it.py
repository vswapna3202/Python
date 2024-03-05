# This program finds the maximum of sum of all squares of integer numbers input
# in N different lists.
# Input: The first line contains 2 space separated integers K and M.
#        The next K lines each contains an integer Ni, denoting the number of 
#        elements in the ith list, followed by Ni space separated integers 
#        denoting the elements in the list.
# Output: Output a single integer denoting the value Smax.
# Import relevant libraries
from itertools import product

# Input integers K and M
K, M = map(int, input().split())

# Declare an empty array arr
arr = []

# Loop through for every K element
for _ in range(K):
    # Obtain all the integers except the first which indicates size of the list
    # and them to row
    row = map(int, input().split()[1:])

    # For each list of integers, square each element and take modulo M and append
    # the resulting mapped iterator to arr
    arr.append(map(lambda x:x**2%M, row))
# Using lambda functions sum of all elements in arr and modulo by M and print
# the max of this sum out of all elements in product(*arr) this would give
# Smax
print(max(map(lambda x: sum(x)%M, product(*arr))))
