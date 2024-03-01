# This program given a string S finds out whether S is a valid regex or not.
# Input: The first line contains integer T, the number of test cases
#        The second line contains the string S
# Output: Print True or False for each test case without quotes
# Constraints: The validity of the regex patterns depends on the regex engine used.
#              Different Python implementations (e.g., CPython, PyPy) may have slight
#              differences in their regex support.
import re

# This function takes a valid string and checks using compile method of re whether
# it is valid and returns True if it is. if an error occurs, it returns False
def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False
    
T = int(input())
for _ in range(T):
    s = input()
    print(is_valid_regex(s))