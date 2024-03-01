# This program removes an element x from set x.
# Operations: remove(x): If element x exists removes it from set s if it does not
#             exist it raises a KeyError. The print s.remove(x) operation returns
#             None.
#             discard(x) : If element exists removes it from set s if it does not
#             exist it does not raise a KeyError. The print s.discard(x) operation
#             returns None.
#             pop(): This operation removes and returns an arbitrary element from
#             set s. If there are no elements to remove raises KeyError.
# Input:    The first line contains integer n, number of elements in set s
#           The second line contains  space separated elements of set s. All of
#           the elements are non-negative integers, less than or equal to 9.
#           The third line contains integer N, the number of commands.
#           The next  lines contains either pop, remove and/or discard commands
#           followed by their associated value.
# Output:   Print the sum of the elements of set s on a single line.
N = int(input())
s = set(map(int, input().split()))

while len(s) != N:
    print(f"Enter exactly {N} number of elements in set.")
    s = set(map(int, input().split()))

n = int(input())
for _ in range(n):
    op = input().split()
    if op[0] == 'pop':
        if s:
            s.pop()
        else:
            print("KeyError: pop from an empty set")
    elif op[0] == 'remove':
        try:
            s.remove(int(op[1]))
        except KeyError as e:
            print("KeyError: ",int(op[1]))
    elif op[0] == 'discard':
        s.discard(int(op[1]))
sum = 0
for num in s:
    sum+=num
print(sum)
