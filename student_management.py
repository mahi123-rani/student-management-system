# Simple Student Management Program

# List to store student details
student_list = []

def add_student():
    print("\n-- Add New Student --")
    s_name = input("Enter name: ")
    s_roll = input("Enter roll no: ")
    s_course = input("Enter course: ")

    student = {
        "Name": s_name,
        "Roll": s_roll,
        "Course": s_course
    }

    student_list.append(student)
    print("Student added successfully!\n")

def show_students():
    if len(student_list) == 0:
        print("No students to display.\n")
        return

    print("\n-- All Students --")
    for idx, s in enumerate(student_list, start=1):
        print(f"{idx}. Name: {s['Name']}, Roll No: {s['Roll']}, Course: {s['Course']}")
    print()

def remove_student():
    print("\n-- Delete Student --")
    r = input("Enter roll number to delete: ")

    for s in student_list:
        if s["Roll"] == r:
            student_list.remove(s)
            print("Student removed successfully!\n")
            return

    print("No student found with that roll number.\n")

def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        ch = input("Choose an option: ")

        if ch == '1':
            add_student()
        elif ch == '2':
            show_students()
        elif ch == '3':
            remove_student()
        elif ch == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option. Please try again.\n")

# Start the program
main()
