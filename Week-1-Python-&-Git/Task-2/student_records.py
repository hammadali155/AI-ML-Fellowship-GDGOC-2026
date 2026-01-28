students = []


def add_student(roll_no, name, age, grades):
    for student in students:
        if student['roll_no'] == roll_no:
            print(f"Student with roll number {roll_no} already exists!")
            return
    
    student = {
        'roll_no': roll_no,
        'name': name,
        'age': age,
        'grades': grades,
        'average': sum(grades.values()) / len(grades) if grades else 0
    }
    
    students.append(student)
    print(f"Student '{name}' added successfully!")


def update_student(roll_no, **kwargs):
    for student in students:
        if student['roll_no'] == roll_no:
            if 'name' in kwargs:
                student['name'] = kwargs['name']
            if 'age' in kwargs:
                student['age'] = kwargs['age']
            if 'grades' in kwargs:
                student['grades'] = kwargs['grades']
                student['average'] = sum(kwargs['grades'].values()) / len(kwargs['grades'])
            
            print(f"Student record updated successfully!")
            return
    
    print(f"Student with roll number {roll_no} not found!")


def delete_student(roll_no):
    for i, student in enumerate(students):
        if student['roll_no'] == roll_no:
            deleted = students.pop(i)
            print(f"Student '{deleted['name']}' deleted successfully!")
            return
    
    print(f"Student with roll number {roll_no} not found!")


def display_all_students():
    if not students:
        print("No student records found!")
        return
    
    print("\n" + "="*80)
    print(f"{'Roll No':<10} {'Name':<20} {'Age':<5} {'Average':<10} {'Grades'}")
    print("="*80)
    
    for student in students:
        grades_str = ", ".join([f"{subj}: {grade}" for subj, grade in student['grades'].items()])
        print(f"{student['roll_no']:<10} {student['name']:<20} {student['age']:<5} "
              f"{student['average']:<10.2f} {grades_str}")
    
    print("="*80)
    print(f"Total students: {len(students)}\n")


def search_student(roll_no):
    for student in students:
        if student['roll_no'] == roll_no:
            print(f"\nStudent Record Found:")
            print(f"Roll No: {student['roll_no']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {student['grades']}")
            print(f"Average: {student['average']:.2f}\n")
            return
    
    print(f"Student with roll number {roll_no} not found!")


def get_top_students(n=3):
    if not students:
        print("No student records found!")
        return
    
    sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)
    
    print(f"\nTop {min(n, len(students))} Students:")
    print("="*60)
    
    for i, student in enumerate(sorted_students[:n], 1):
        print(f"{i}. {student['name']} (Roll No: {student['roll_no']}) - Average: {student['average']:.2f}")
    
    print("="*60 + "\n")


def get_statistics():
    if not students:
        print("No student records found!")
        return
    
    all_averages = [student['average'] for student in students]
    
    print("\nStudent Statistics:")
    print("="*50)
    print(f"Total Students: {len(students)}")
    print(f"Highest Average: {max(all_averages):.2f}")
    print(f"Lowest Average: {min(all_averages):.2f}")
    print(f"Class Average: {sum(all_averages) / len(all_averages):.2f}")
    print("="*50 + "\n")


def filter_students_by_average(min_average):
    filtered = [s for s in students if s['average'] >= min_average]
    
    if not filtered:
        print(f"No students found with average >= {min_average}")
        return
    
    print(f"\nStudents with average >= {min_average}:")
    print("="*60)
    for student in filtered:
        print(f"{student['name']} (Roll No: {student['roll_no']}) - Average: {student['average']:.2f}")
    print("="*60 + "\n")


def main():
    add_student(101, "Hammad Ali", 20, {"Math": 95, "Physics": 90, "Chemistry": 88})
    add_student(102, "Haris Khan", 19, {"Math": 92, "Physics": 94, "Chemistry": 91})
    add_student(103, "Shahid Zahoor", 21, {"Math": 78, "Physics": 82, "Chemistry": 80})
    
    while True:
        print("\n" + "="*50)
        print("STUDENT RECORD SYSTEM")
        print("="*50)
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Search Student")
        print("6. Top Students")
        print("7. Statistics")
        print("8. Filter by Average")
        print("9. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-9): ").strip()
        
        try:
            if choice == "1":
                roll_no = int(input("Enter roll number: "))
                name = input("Enter name: ").strip()
                age = int(input("Enter age: "))
                
                print("Enter grades (press Enter when done):")
                grades = {}
                while True:
                    subject = input("Subject (or press Enter to finish): ").strip()
                    if not subject:
                        break
                    grade = float(input(f"Grade for {subject}: "))
                    grades[subject] = grade
                
                add_student(roll_no, name, age, grades)
            
            elif choice == "2":
                roll_no = int(input("Enter roll number to update: "))
                print("Leave fields blank to skip updating them.")
                name = input("New name: ").strip()
                age_input = input("New age: ").strip()
                
                update_data = {}
                if name:
                    update_data['name'] = name
                if age_input:
                    update_data['age'] = int(age_input)
                
                update_student(roll_no, **update_data)
            
            elif choice == "3":
                roll_no = int(input("Enter roll number to delete: "))
                confirm = input(f"Are you sure? (y/n): ").strip().lower()
                if confirm == 'y':
                    delete_student(roll_no)
            
            elif choice == "4":
                display_all_students()
            
            elif choice == "5":
                roll_no = int(input("Enter roll number to search: "))
                search_student(roll_no)
            
            elif choice == "6":
                n = int(input("How many top students to display? "))
                get_top_students(n)
            
            elif choice == "7":
                get_statistics()
            
            elif choice == "8":
                min_avg = float(input("Enter minimum average: "))
                filter_students_by_average(min_avg)
            
            elif choice == "9":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice! Please try again.")
        
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
