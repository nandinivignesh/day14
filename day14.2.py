import csv
FILENAME="students.cv"
def add_student():
    name=input("Enter student name:")
    age=input("Enter student age: ")
    grade=input("Enter student grade:")
    with open(FILENAME,"a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([name,age,grade])
        print("student record added sucessfully")
def view_students():
    try:
        with open(FILENAME,"r")as file:
            reader=csv.reader(file)
            students=list(reader)
            if not students:
                print("no student record found")
                return
            print("\nStudents Records:")
            print(f"{'Name':<15}{'Age':<5}{'Grade'}")

            for student in students:
                print(f"{student[0]:<15}{student[1]:<5}{student[2]}")
    except FileNotFoundError:
        print("No student records found")
def search_student():
    search_name=input("enter student name to search:").strip().lower()
    try:
        with open(FILENAME,"r")as file:
            reader=csv.reader(file)
            found=False
            for student in reader:
                if student[0].strip().lower()==search_name:
                    print("Found:Name:{student[0],Age:{student[1]}},Grade:{student[2]}")
                    found=True
                    break
                if not found:
                    print("Student not found")
    except FileNotFoundError:
        print("No students records found")

while True:
 print("\nStudent Record Manager")
 print("1. Add Student")
 print("2. View Students")
 print("3. Search Student")
 print("4. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
  add_student()
 elif choice == "2":
  view_students()
 elif choice == "3":
  search_student()
 elif choice == "4":
  print("Goodbye!")
 break
else:
  print("Invalid choice. Please try again.")

