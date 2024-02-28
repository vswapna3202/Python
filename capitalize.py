# This program given a full name capitalizes the name.
# Input: A single line of input containing the full name s
# Output: Print the capitalised string s

# This function returns a string which is capitalized 
# Input: string s
def solve(s):
    return " ".join([word.capitalize() for word in s.split(" ")])


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)