def show_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------\n")


def show_student_details(name, department, semester):
    print("--- Student Details ---")
    print(f"Name: {name}")
    print(f"Department: {department}")
    print(f"Semester: {semester}\n")


def show_subject_marks(marks):
    print("--- Subject Marks ---")
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}")
    print()


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    show_grade_criteria()

    while True:
        print("Enter Student Details")

        name = input("Enter student name: ")
        department = input("Enter department: ")
        semester = input("Enter semester: ")

        n = int(input("Enter number of subjects: "))
        marks = []

        for i in range(n):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)

        print("\n===== RESULT =====")
        show_student_details(name, department, semester)
        show_subject_marks(marks)

        avg = calculate_average(marks)
        print(f"Average Marks: {avg:.2f}")
        print(f"Final Grade: {calculate_grade(avg)}")
        print("==================\n")

        choice = input("Do you want to enter another student? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you! Program ended.")
            break


if __name__ == "__main__":
    main()
