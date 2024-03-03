# This program computes the cartesian product of input iterables.
# Input: Two lists A and B
# Output: Cartesian product of A X B space separated tuples
# Import relevant libraries
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(product(A,B))
for item in C:
    print(item, end=" ")
