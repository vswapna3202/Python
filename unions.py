# This program shows the usage of union method on sets. The input is set of
# two student roll numbers one subscribed to english and the other subscribed to
# French newspapers and some students could subscribe to both. The program finds
# the total number of students subscribed to atleast one newspaper.
# Input: The first line contains an integer n the number of students who
#        have subscribed to the English newspaper
#        The second line contains n space separated roll numbers of those students.
#        The third line contains b the number of students who have subscribed to
#        the French newspaper
#        The fourth line contains b space separated roll numbers of those students.
# Output: Output the total number of students who have at least one subscription.
n = int(input())
eng_numbers = input().split()
s1 = set([int(number) for number in eng_numbers])

b = int(input())
french_numbers = input().split()
s2 = set([int(number) for number in french_numbers])

print(len(s1.union(s2)))
