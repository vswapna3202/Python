# This program wraps a given string S to a given width w.
# Input: The first line containing string, string
#        The second line containing the width, max_width
# Output: A string wrapped to width max_width
import textwrap

# This function wraps the string to max_width using text_wrap fill method
# and returns the output
def wrap(string, max_width):
    output = textwrap.fill(string,max_width) # returns string
    #output = textwrap.wrap(string, max_width) # returns list
    return output

# Accepts input max_width and string and passes these to function wrap
# Prints result 
if __name__ == '__main__':
    max_width, string = int(input()), input()
    result = wrap(string, max_width)
    print(result)