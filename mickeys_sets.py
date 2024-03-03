# This program helps Ms. Gabriel Williams who is a botany professor at District 
# College. One day, she asked her student Mickey to compute the average of all 
# the plants with distinct heights in her greenhouse.
# Formula used: Sum of Distinct Heights / Total number of distinct heights.
# Input: The first line contains the integer, N , the size of arr.
#        The second line contains the N space-separated integers, arr[i] .
#Output: The average based on the formula above is printed
def calculate_avg(array):
    distinct_arr = set() # Create set distinct_arr
    # Loop through all elements in list and add to distinct_arr to have only
    # distinct heights
    for a in array:
        distinct_arr.add(a)
    # Compute average based on forumla sum of distinct heights / total number of 
    # distinct heights. Return average
    average = sum(distinct_arr) / len(distinct_arr)
    return average

if __name__ =='__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = calculate_avg(arr)
    print(result)
