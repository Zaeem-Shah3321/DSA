def display_students(students):
    if not students:
        print("No students in the class.")
    else:
        print("Current students in the class:")
        for student in students:
            print(f"- {student}")

def add_student(students):
    name = input("Enter the name of the student to add: ")
    students.append(name)
    print(f"{name} has been added.")

def remove_student(students):
    name = input("Enter the name of the student to remove: ")
    if name in students:
        students.remove(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found in the list.")

def main():
    students = [] 
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            remove_student(students)
        elif choice == '3':
            display_students(students)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
