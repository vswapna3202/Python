# This program accepts a list of commands and values and does the operations of the 
# command on the list and prints the list if the command is print
# Input: n number of commands an integer value is first line
#        command integer valid commands are insert, append, remove, sort, pop, print
#        and reverse.
# Output: print of the array whenever the command is so
if __name__ == '__main__':
    arr = [] # Declare an empty array to be populated
    N = int(input()) # Obtain number of commands from user
    for _ in range(N): # Loop through number of commands
        command, *line = input().split() # Accept command and numbers
        line = [int(x) for x in line] # Convert number(s) to int
        if command == 'append': # If command is append, append number to arr
            arr.append(line[0])
        elif command == 'insert': # If command is insert, insert numbers to arr
            arr.insert(line[0],line[1])
        elif command == 'remove': # If command is remove, remove number from arr
            arr.remove(line[0])
        elif command == 'sort': # If command is sort, sort arr
            arr.sort()
        elif command == 'pop': # If command is pop, pop arr
            arr.pop()
        elif command == 'reverse': # If command is reverse, reverse arr
            arr.reverse()
        else:
            print(arr) # Print arr
            