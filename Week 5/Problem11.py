def main():
    students = ["Asad", "Moon", "Talha", "Hamid", "Zaeem", "Sheer", "Sheri"]
    search_name = input("Enter the name of the student to search for: ").lower() 
    students_lower = [name.lower() for name in students]
    
    if search_name in students_lower:
        index = students_lower.index(search_name)
        print(f"{students[index]} found at index: {index}") 
    else:
        print(f"{search_name} is not present in the list of students.")

if __name__ == "__main__":
    main()
