# This program given an input N print a palindromic triangle of size N and a
# right-angled number triangle with repeated numbers
# Input: A single line of input containing the integer N.
# Output: Prints the palindromic triangle of size N as explained above.
#         Prints the right-angled number triangle with repeated numbers.
#         Prints a centered triangle with repeated numbers.
#         Prints a centered palindromic triangle

# This loop prints a palindromic triangle of size N
n = int(input())
print()
for i in range(1,n + 1):
    print(((10 ** i)//9) ** 2)

# This loop prints a right-angled triangle of repeated digits of size N
print()
for i in range(1,n + 1):
    print(((10**i)//9)*i)

# This loop prints a centered triangle of repeated digits of size N
print()
for i in range(1, n + 1):
    num = ((10**i) // 9) * i
    print((" ".join(str(num))).center(2 * n))

# This loop prints a centered palindromic triangle of size N
print()
for i in range(1,n + 1):
    num = ((10 ** i)//9) ** 2
    print((" ".join(str(num).center(2*n))))
