def calculate_average(scores):
    """Calculate and return the arithmetic mean of given scores."""
    total_points = 0
    for point in scores:
        total_points += point
    return total_points / len(scores)


def get_highest_score(scores):
    """Find and return the maximum score by sorting the list."""
    ordered_scores = sorted(scores)
    return ordered_scores[-1]


def get_lowest_score(scores):
    """Find and return the minimum score by sorting the list."""
    ordered_scores = sorted(scores)
    return ordered_scores[0]


def process_students(student_list):
    """Output all student names from a list along with the headcount."""
    print("Students: ")
    print("\n".join(student_list))
    print(f"Total Students: {len(student_list)}")


def register_students(*students):
    """Register multiple student names passed as arguments and show total."""
    print("Registered Students:")
    print("\n".join(students))
    print(f"Total: {len(students)}")
