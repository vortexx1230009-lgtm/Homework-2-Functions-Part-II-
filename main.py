from student_utilss import (
    calculate_average,
    get_highest_score,
    get_lowest_score,
    process_students,
    register_students,
)
students = ["Ali", "Leyla", "Kamran", "Aysel"]
scores = [78, 91, 85, 67, 95, 88]
print("Average Score: ", calculate_average(scores))
print("Highest Score: ", get_highest_score(scores))
print("Lowest Score: ", get_lowest_score(scores))
print()
process_students(students)
print()
register_students("Ali", "Leyla", "Kamran")
