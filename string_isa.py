# This python program inputs a string and checks if given string contains:
# alphanumeric characters,alphabets, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    print("alphanumeric: ", any(c.isalnum() for c in s))
    print("alphabetic: ",any(c.isalpha() for c in s))
    print("numeric: ",any(c.isdigit() for c in s))
    print("lower case: ",any(c.islower() for c in s))
    print("upper case: ",any(c.isupper() for c in s))