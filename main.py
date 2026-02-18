import os
import csv

FILENAME = "students.csv"

# Create file if not exists:
def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode = "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course"])

# Add student:
def add_student():
    id = input("Enter your ID: ")
    name = input("Enter your Name: ")
    age = input("Enter your Age: ")
    course = input("Enter your Course: ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, course])


print(" ✅ Student Added Succesfully\n")


# View students:
def view_students():
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

# Search student:
def search_student():
    id = input("Enter student ID to search: ")
    found = False
    with open(FILENAME, mode="r", newline="") as file:
        reader  = csv.reader(file)
        for row in reader:
            if row and row[0] == id:
                print("🎯 Student found: ",row)
                found = True

    if not found:
        print("❌ Student not found")
    print()

# Update student:
def update_student():
    sid = input("Enter Student ID to update: ")
    rows = []
    updated = False

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == sid:
                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")
                rows.append([sid, name, age, course])
                updated = True
            else:
                rows.append(row)

    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("✅ Student Updated Successfully")
    else:
        print("❌ Student Not Found")
    print()


    # Delete student:

def delete_student():
    sid = input("Enter Student ID to delete: ")
    rows = []
    deleted = False

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == sid:
                deleted = True
            else:
                rows.append(row)

    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if deleted:
        print("✅ Student Deleted Successfully")
    else:
        print("❌ Student Not Found")
    print()
    
# Main menu:
def main():
    create_file()

    while True:
        print("====STUDENT MANAGEMENT SYSTEM====")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your Choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print(" 👋 Exiting Program")
            break
        else:
            print(" ❌ Invalid Choice\n")

# Run Program:
main()