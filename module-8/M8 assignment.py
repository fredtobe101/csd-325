# Fred Costello
# CSD-325 M8 Assignment
# 5/10/2026
# Resources: Oxylabs2024, Microsoft Word, Copilot, Google




# ---Explanation of code/ assignment instructions by line---
# JSON Load function used to load file (line 29)
# loops through JSON list and prints value (Line 43 - 84)
# Notification output that the list is original (Line 65)
# first, last and fictional ID added (line 68)
# Output to user that the list is updated (71)
# Use the JSON dump() function to append the new data to the file (57)



import json
from win11toast import toast

class Student:
    def __init__(self, first, last, student_id, email):
        self.first = first
        self.last = last
        self.student_id = student_id
        self.email = email

def load_students(filename):
    with open(filename, "r") as file: #open function
        data = json.load(file) #load function, Assignment instruction 6,a
        students = []
        for entry in data:
            student = Student(
                entry["F_Name"],
                entry["L_Name"],
                entry["Student_ID"],
                entry["Email"]
            )
            students.append(student)
        return students

def print_students(student_list):
    for s in student_list:
        print(f"{s.last}, {s.first} : ID = {s.student_id} , Email = {s.email}")

def save_students(filename, student_list):
    data = []
    for s in student_list:
        data.append({
            "F_Name": s.first,
            "L_Name": s.last,
            "Student_ID": s.student_id,
            "Email": s.email
        })
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":

    filename = r"C:\Users\fredc\OneDrive\Desktop\Bellevue Classes\CSD325 - Advanced Python\Week 8\Student.json"

    students = load_students(filename)

    print("Original Student List:\n")
    print_students(students)

    new_student = Student("Fred", "Costello", 511515, "fredcostello@coldmail.com")
    students.append(new_student)

    print("\nUpdated Student List:\n")
    print_students(students)

    toast("Student.json Updated", "The student list has changed. Choose Y or N in the console to save.")

    choice = input("\nWould you like to save the updated list to Student.json? (Y/N): ").strip().upper()

    if choice == "Y":
        save_students(filename, students)
        toast("File Saved", "Student.json has been updated successfully.")
        print("\nThe Student.json file has been updated.")
    else:
        toast("Changes Not Saved", "The JSON file was not modified.")
        print("\nChanges were NOT saved to the JSON file.")
