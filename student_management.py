def menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

students = []

def add_student():
    student_name = input("Enter the name of the student: ")
    students.append(student_name)
    print(f"Student {student_name} added successfully!")

def view_students():
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")

def search_student():
    student_name = input("Enter the name of the student to search: ")
    if student_name in students:
        print(f"Student {student_name} found.")
    else:
        print(f"Student {student_name} not found.")

def remove_student():
    student_name = input("Enter the name of the student to remove: ")
    if student_name in students:
        students.remove(student_name)
        print(f"Student {student_name} removed successfully!")
    else:
        print(f"Student {student_name} not found.")

def main():
    while True:
        menu()
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main function
main()
