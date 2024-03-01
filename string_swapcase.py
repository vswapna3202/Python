# This program inputs a string and if the string character is in upper case it is
# converted to lowercase and if it is in lower case it is converted to uppercase
# Input: A single line containing string s.
# Output: String modified with uppercase to lowercase and vice versa.
if __name__ == '__main__':
    # Input the string
    input_string = input()

    # This function swaps the case of the string passed to it.
    def swap_case(string):
        new_string = ""
        for s in string:
            # if the s character in string is in uppercase change it to lower
            # if the s character in string is in lowercase change it to upper
            if s.isupper() :
                new_string = new_string + s.lower()
            else:
                new_string = new_string + s.upper()
        return new_string
    result = swap_case(input_string)
    print(result)
    