# This program validates given n email addresses and prints only valid email
# addresses in lexicographical order.
# Valid email address rules are:
#   - It must have the username@websitename.extension format type.
#   - The username can only contain letters, digits, dashes and underscores
#   [a-z][A-Z][0-9][_-] .
#   - The website name can only have letters and digits [a-z][A-Z][0-9].
#   - The extension can only contain letters [a-z][A-Z].
#   - The maximum length of the extension is 3.
# Input: n the number of email addresses
#        list of n email addresses with one email in each line
# Output: List of valid email addresses separated by comma

# Import relevant libraries
import re

# Function takes a string input and returns True if valid email
# else returns False.
def is_valid_email(s):
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    return re.match(pattern, s)

# Function takes email_list entered by user invokes filter function
# and adds email to list if is_valid_email function returns true.
def filter_emails(email_list):
    return list(filter(is_valid_email, email_list))

# Accept number of input from user
n = int(input())
emails = [] # Declare empty emails array
valid_emails = [] # Declare empty valid_emails array

# Loop for all n email addresses
for _ in range(n):
    # Obtain email address and append to emails array
    emails.append(input().strip())

valid_emails = filter_emails(emails)

# Sort valid_emails array in lexicographical order
valid_emails.sort()

# Display valid email addresses
print(valid_emails)