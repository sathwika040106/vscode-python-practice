from collections import defaultdict

student_marks = defaultdict(int)

student_marks["Math"] += 90
student_marks["Science"] += 85

print(student_marks["Math"])
print(student_marks["English"])