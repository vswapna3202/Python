# This program shows the uses of exception handling. It shows handling of divide by 
# zero error and Value error.
# Input the number of numbers
T = int(input())
input_list = []

# Input the numbers for calculating average
for i in range(T):
    input_list.append(input().split())

# Input the numbers into a and b and divide it and set it to variable c
# Have a try catch loop and add errors ValueError and ZeroDivisionError
# and prints out error messages
for i in range(T):
    try:
        a = int(input_list[i][0])
        b = int(input_list[i][1])
        c = a / b
        print(int(c))
    except ValueError as e:
        print("Error Code:",e)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
