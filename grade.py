# This program accepts the number of students n and their names and scores. It prints
# the second lowest scorer's name if multiple scorers are present it presents all
# second low scorer's names
# Input: first line accepts integer n
#        second line accepts name of student
#        third line accepts score of student
#        repeats this for all n students
# Output: Prints student name of second lowest scorer

scores = set() # Set to have distinct scores of students
names = set() # Set to have distinct name of students
students = [] # Array of students
for _ in range(int(input())): # Loop through for number of students by user
    # Accept name and score of student, score is float
    name =  input()
    score = float(input())    
    scores.add(score) # Add score to scores set
    students.append([name, score]) # Append name and score to students array
#students.sort(key=lambda i:i[1])
# Obtain second lowest score by sorting scores and getting score at index 1   
second_lowest_score = sorted(scores)[1]
# Loop through students using enumerate and check if second lowest score
# is same as student score from loop if so add name of student to names set
for index, student in enumerate(students):
    if (student[1] == second_lowest_score):
        names.add(student[0])
# Sort the names set into a alphabetical order
sorted_names = sorted(names)
# Loop through names set and print all names who have scored second lowest score
for name in sorted_names:
    print(name)