students = {}
courses = {}
marks = {}


def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for i in range(num_students):
        students_id = input("Enter the student ID: ")
        students_name = input("Enter the student name: ")
        students_dob = input("Enter the student date of birth: ")
        students[students_id] = {'name': students_name, 'dob': students_dob}


def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        courses_id = input("Enter the course ID: ")
        courses_name = input("Enter the course name: ")
        courses[courses_id] = {'name': courses_name}


def input_marks():
    courses_id = input("Enter the course ID: ")
    if courses_id not in courses:
        print("Invalid course ID.")
        return
    for students_id in students:
        mark = float(input(f"Enter the mark for {students[students_id]['name']}: "))
        if students_id not in marks:
            marks[students_id] = {}
        marks[students_id][courses_id] = mark


def list_courses():
    for courses_id in courses:
        print(f"{courses_id}: {courses[courses_id]['name']}")


def list_students():
    for students_id in students:
        print(f"{students_id}: {students[students_id]['name']}")


def show_marks():
    courses_id = input("Enter the course ID: ")
    if courses_id not in courses:
        print("Invalid course ID.")
        return
    for students_id in students:
        if students_id in marks and courses_id in marks[students_id]:
            print(f"{students[students_id]['name']}: {marks[students_id[courses_id]]}")
        else:
            print(f"{students[students_id]['name']}: N/A")


input_students()
input_courses()

while True:
    print("Select an option:")
    print("1. Input marks for a course.")
    print("2. List courses.")
    print("3. List students.")
    print("4. Show student marks for a given course.")
    print("5. Quit.")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
