# This python program finds the absolute time difference in seconds between 
# two timestamps.
# Input: T - the number of testcases
#        t1, t2 - the two valid timestamps where year <= 3000
# Output: absolute difference in seconds (t1 - t2)
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Convert timestamps to datetime objects
    format_str = "%a %d %b %Y %H:%M:%S %z"
    t1_datetime = datetime.datetime.strptime(t1, format_str)
    t2_datetime = datetime.datetime.strptime(t2, format_str)

    # Calculate the absolute time difference in seconds
    delta = abs((t1_datetime - t2_datetime).total_seconds())
    return int(delta)

t = int(input())

for t_itr in range(t):
    t1 = input()
    t2 = input()

    delta = time_delta(t1, t2)
    print(delta)