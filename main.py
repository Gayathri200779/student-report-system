import json
def save_data(students):
    with open("students.json","w") as f:
        json.dump(students,f)
def load_data():
    try:
        with open("students.json","r") as f:
            return json.load(f)
    except:
        return[]
def get_marks():
    while True:
        try:
            marks=list(map(int,input("\nEnter your marks: ").split()))
            if not marks:
                print("error:marks cannot me empty")
                continue
            return marks
        except:
            print("invalid input.Enter numbers only")

def calculate_report(marks):
    total = sum(marks)
    avg = total / len(marks)
    max_val = max(marks)
    min_val = min(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    result = "Pass" if avg >= 50 else "Fail"

    return total, avg, grade, max_val, min_val, result


def display_student(name, marks):
    total, avg, grade, max_val, min_val, result = calculate_report(marks)

    print("\nName:", name)
    print("Total:", total)
    print(f"Average: {avg:.2f}")
    print("Grade:", grade)
    print("Maximum:", max_val)
    print("Minimum:", min_val)
    print("Result:\n", result)


students = load_data()

while True:
    print("\n"+"-"*40+"\n")
    print("\n1. Add Student")
    print("2. View All Reports")
    print("3. Search Student")
    print("4. Delete Student ")
    print("5. Exit\n")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("\nEnter name: ")
        found=False

        for student in students:
            existing_name=student[0]

            if existing_name.lower()==name.lower():
                print("Student already exists")
                found=True
                break
        if not found:
            marks = get_marks()
            students.append([name, marks])
            save_data(students)

    elif choice == "2":
        for student in students:
            name = student[0]
            marks = student[1]
            display_student(name, marks)

    elif choice == "3":
        search_name=input("\nEnter name to seacrh: ")
        found=False
        for student in students:
            name=student[0]
            marks=student[1]

            if name.lower()==search_name.lower():
                display_student(name,marks)
                found=True
                break
        if not found:
            print("Student not found")

    elif choice == "4":
        delete_name=input("\nEnter name to delete: ")
        found=False

        for student in students:
            name=student[0]

            if name.lower()==delete_name.lower():
                students.remove(student)
                found=True
                print("Student Deleted")
                break
        if not found:
            print("Student not found")

    elif choice == "5":
        save_data(students)
        print("Exiting....")
        break

    else:
        print("Invalid choice")
