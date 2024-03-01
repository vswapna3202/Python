# This program inputs number of students and for each student accepts the name and 
# their scores. Finds the name of student whose average needs to be calculated and
# prints average score of the queried student.
# Input: first line accepts an integer of number of students
#        second line accepts the name of student and their scores all in one line
#        repeats input for all students
#        accepts name of student whose average score needs to be calculated in next 
#        line
# Output: Prints the average score of the student whose average was to be calculated 
if __name__ == '__main__':
    # Declare student_marks an empty dictionary
    student_marks = {}
    # For number of students specified in input loop
    for _ in range(int(input())):
        # Accept name and scores in same line
        name, *line = input().split()
        # Create a list for all the scores
        scores = list(map(float, line))
        # With name as key add scores for each key of dictionary student_marks
        student_marks[name] = scores
    # Obtain the name of the student whose average needs to be calculated
    query_name = input()
    # Obtain the student_mark array from dictionary for key name
    student_mark = student_marks[query_name]
    student_total = 0.0
    # Loop through student_mark and all the marks to student_total
    for index, value in enumerate(student_mark):
        student_total = student_total + value
    # Calculate average by dividing student_total by number of marks and print it
    student_avg = student_total / len(student_mark)
    print("{:.2f}".format(student_avg))
    