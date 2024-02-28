# This python program finds the number of times a substring occurs in a given string.
# Input: String and substring in next line
# Output: number of times substring occurs in string
# This function counts of times substring occurs in string
def count_substring(string, sub_string):
    count = 0
    # Loop through the string and check if substring is part of the string
    # if so increase the count
    for i in range(0,len(string)):
        check_string = string[i:i+len(sub_string)]
        if(check_string == sub_string):
            count += 1
    return count

if __name__ == '__main__':
    # Input the string and substring
    string = input().strip()
    sub_string = input().strip()
    
    # Print the count obtained from function count_substring
    count = count_substring(string, sub_string)
    print(count)