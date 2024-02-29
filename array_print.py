# This program finds the runner-up score given the participants' score sheet.
# Input: n number of scores in first line
#        scores list of all n scores in second line separated with space
# Output: prints the score of the runner up from list of n scores
# Input n and list of scores 
n = int(input("Enter n: "))
arr = map(int, input().split())
# Create a set from arr and call it as unique_elements
unique_elements = set(arr)
# If unique_elements size is 1 then there is just one winner and no runner up so 
# print this message to user else, sort unique_elements set and print
# sorted_arr[-2] which prints the second last element which is the runner up.
if len(unique_elements) == 1:
    print("All elements are same, no runner-up")
else:
    sorted_arr = sorted(unique_elements)
    print("Runner up is: ",sorted_arr[-2])
