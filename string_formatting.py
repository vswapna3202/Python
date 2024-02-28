# This python program given an integer n prints the values of each integer i from
# 1 to n in decimal, octal, hexadecimal (capitalized) and binary.
# Input: integer n
# Output: integer i from 1 to n in decimal, octal, hexadecimal (capitalized)
# and binary formats in each columns
def print_formatted(number):
    #
    max_width = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i).rjust(max_width)
        octal = oct(i)[2:].rjust(max_width)
        hexa = hex(i)[2:].upper().rjust(max_width)
        binary = bin(i)[2:].rjust(max_width)
        print("{:<{width}} {:<{width}} {:<{width}} {:<{width}}".format(str(decimal), octal, hexa, binary, width=max_width))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)