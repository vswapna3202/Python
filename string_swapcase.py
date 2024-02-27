# This program inputs a string and if the string character is in upper case it is
# converted to lowercase and if it is in lower case it is converted to uppercase
if __name__ == '__main__':
    # Input the string
    s = input()

    # This function swaps the case of the string passed to it.
    def swap_case(s):
        new_string = ""
        for str in s:
            # if the str character in string is in uppercase change it to lower
            # if the str character in string is in lowercase change it to upper
            if str.isupper() :
                new_string = new_string + str.lower()
            else:
                new_string = new_string + str.upper()
        return new_string
    
    result = swap_case(s)
    print(result)

