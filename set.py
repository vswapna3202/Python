# This program counts the total number of distinct country stamps from a collection
# of N stamps
# Input: an integer N is input in first line which is total number of country stamps
#        each line has name of a country stamp there should be N lines
# Output: number of distinct country stamps

N = int(input())
s = set()
for _ in range(N):
    s.add(input())
print(len(s))