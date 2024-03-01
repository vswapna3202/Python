if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_mark = student_marks[query_name]
    student_total = 0.0
    for index, value in enumerate(student_mark):
        student_total = student_total + value
    student_avg = student_total / len(student_mark)
    print("{:.2f}".format(student_avg))
    