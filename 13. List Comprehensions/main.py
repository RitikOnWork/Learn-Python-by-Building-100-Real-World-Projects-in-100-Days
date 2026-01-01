# Student Grade Manager by List Comprehensions
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
def get_passing_students(students, passing_grade=60):
    return [student for student in students if student['grade'] >= passing_grade]
def main():
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 58},
        {'name': 'Charlie', 'grade': 72},
        {'name': 'David', 'grade': 49},
        {'name': 'Eva', 'grade': 91}
    ]
    average_grade = calculate_average([student['grade'] for student in students])
    passing_students = get_passing_students(students)
    print(f"Average Grade: {average_grade:.2f}")
    print("Passing Students:")
    for student in passing_students:
        print(f"{student['name']}: {student['grade']}")
if __name__ == "__main__":
    main()  

