# This program reads a given string, changes the character at a given index and 
# prints the modified string.
# Input: string to be modified
#        position, new character
# Output: prints the modified string
# This method modifies string by slicing the string until the position adding the 
# new character and joining the rest of the string.
def mutate_string(string, position, character):
    arr = string[:]
    arr = arr[:position] + character + arr[position+1:]
    return arr

# Inputs the string s, position i and character c and invokes mutate_string
# method and prints the modified new string s_new
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)