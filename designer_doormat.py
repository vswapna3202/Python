# This program prints a designer door mat in a specific design as shown below
#   Size: 7 X 21
#   ---------.|.---------
#   ------.|..|..|.------
#   ---.|..|..|..|..|.---
#   -------WELCOME-------
#   ---.|..|..|..|..|.---
#   ------.|..|..|.------
#   ---------.|.---------
# The design pattern should have WELCOME in the center and use only |.- characters
# The mat is N X M where N is an odd number and M is N X 3
# Input: N M integers in a single line separated by spaces
# Output: The designer mat is printed
# Import relevant libraries
import math
rows, cols = map(int, input().split()) #Input rows, cols

# Initialise odd_count to identify count of pattern with |.- in each row
odd_count = 1
# Initialise welcome_row which is in middle by number of rows/2
welcome_row = math.floor(rows/2)
# Initialise patterns to allowed chracters
pattern_side = "-"
pattern_mid = ".|."
# Initialise letter to WELCOME
letter = "WELCOME"
letter_count = len(letter)
# Loop through for rows from 0
for i in range(0, rows):
    # If not middle row
    if i != welcome_row:
        # Find number of dashes - and display it
        no_dash = int((cols - (odd_count * 3)) / 2)
        print(pattern_side*no_dash,end="")
        # Print the pattern in the middle starting with odd_count
        print(pattern_mid*odd_count,end="")
        # Print same number of dashes as before the pattern
        print(pattern_side*no_dash)
        # Increment odd_count to next odd number if top of welcome_row
        # decrement odd_count to next off number if below welcome_row
        if i < welcome_row:
            odd_count += 2
        else:
            odd_count -= 2
    else:
        # If middle row calculate number of dashes - to print 
        # Print dashes, letter and dashes again
        dash_count = int((cols - letter_count) / 2)
        print(pattern_side*dash_count,end="")
        print(letter,end="")
        print(pattern_side*dash_count)
        odd_count -= 2
