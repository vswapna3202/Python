# The students of District College have subscriptions to English and French 
# newspapers. Some students have subscribed only to English, some have subscribed 
# only to French, and some have subscribed to both newspapers.
# Given two sets of student roll numbers, one set has subscribed to the English 
# newspaper, one set has subscribed to the French newspaper. This program finds 
# the total number of students who have subscribed to both newspapers.
# Input:  The first line contains n, the number of students who have subscribed 
#         to the English newspaper.
#         The second line contains n space separated roll numbers of those students.
#         The third line contains b, the number of students who have subscribed to 
#         the French newspaper.
#         The fourth line contains b space separated roll numbers of those students.
# Output: Output the total number of students who have subscriptions to both 
#         English and French newspapers.
n = int(input())  # Input the number of english newspaper subscribers
eng_nos = map(int, input().split())  # Obtain the roll numbers of n students
s1 = set(eng_nos)  # Create set of all the eng_nos to have distinct rolls

b = int(input())  # Input the number of french newspaper subscribers
french_nos = map(int, input().split())  # Obtain the roll numbers of n students
s2 = set(french_nos)  # Create set of all the french_nos to have distinct rolls

# Using intersection of both sets find the students who subscribe to both english
# and french newspapers
print(len(s1.intersection(s2)))



