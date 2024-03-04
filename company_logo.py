# A newly opened multinational brand has decided to base their company logo on the 
# three most common characters in the company name. They are now trying out various 
# combinations of company names and logos based on this condition. Given a string , 
# which is the company name in lowercase letters, the task is to find the top three 
# most common characters in the string.
# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
# Input: A single line of input containing the string s.
# Output: Prints the three most common characters along with their occurrence count 
#         each on a separate line. Sorts the output in descending order of occurrence 
#         count. If the occurrence count is the same, sorts the characters in 
#         alphabetical order.
# Import relevant libraries
from itertools import groupby

s = input().strip() # Get input string
count_arr = [] # Initialise empty array

# Using groupby from itertools loop and get the digit and count of each digit
# append the count and digit to count_arr. Do this on sorted string s
for digit, group in groupby(sorted(s)):
    count = len(list(group))
    count_arr.append((count, digit))

# Sort count_arr based on count and then based on alphabet
sorted_arr = sorted(count_arr, key=lambda x: (-x[0], x[1]))

# Loop through sorted_arr for top 3 counts and print them
for digit, count in sorted_arr[:3]:
    print(digit, count)
