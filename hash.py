# This program given n integers and n separated integers as input creates a tuple
# t of the n integers and computes and prints hash(t).
# Input: First line containing an integer denoting number of elements in the
#        tuple
#        Second line contaning n space separated integers or elements of the
#        tuple t.
# Output: Prints result of hash(t)
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
