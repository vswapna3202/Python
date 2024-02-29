# This python program for a given input string and an integer value k splits the string
# into k equal parts and removes an subsequent occurrences of non-distinct characters
# and prints each k sized distinct characters in separate lines
# Input: The first line containing a single string
#        The second line contains an integer k, the length of each substring
# Output: Each line has a string of distinct characters from input string of size k
# Import relevant libraries 
import textwrap
# This function adds distinct characters from string of size k
# and adds it to dictionary d. Uses wrap method from text wrap
# to split the string into substrings of size k and uses
# setdefault method from dictionary to set the distinct characters
# prints the distinct characters of size k
def merge_the_tools(string, k):
    
    for i in textwrap.wrap(string,k):
        d = {}
        print("".join([d.setdefault(c,c) for c in i if c not in d]))

# Input the string string and integer k and pass it to function merge_the_tools
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)