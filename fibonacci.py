# This program finds the N numbers of the fibonacci series and cubes each number and
# prints the list
# Input:  One line of input: an integer N.
# Output: A list on a single line containing the cubes of the first N fibonacci 
#         numbers.

# Assign cube as x*x*x
cube = lambda x: x*x*x

# Define function fibonacci which generates the first N Fibonacci numbers.
def fibonacci(n):
    # declare an empty fib_arr list to store fibonacci numbers
    fib_arr = []
    for i in range(0, n):
        if i  == 0:
            fib_arr.append(0)
        elif i == 1:
            fib_arr.append(1)
        else:
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
    return fib_arr


if __name__ == '__main__':
    # Accept integer n
    n = int(input())

    # Call function fibonacci with parameter n to generate the first N Fibonacci numbers, 
    # apply cube function to each number using map, and print the resulting list.
    print(list(map(cube, fibonacci(n))))
