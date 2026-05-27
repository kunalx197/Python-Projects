import csv
import os
from datetime import datetime

FILE_NAME = "attendance.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])


def mark_attendance():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty!\n")
        return

    status = input("Enter status (Present/Absent): ").strip().capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid status! Use Present or Absent.\n")
        return

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time, status])

    print(f"Attendance marked for {name}!\n")


def view_attendance():
    print("\n--- Attendance Records ---")

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(f"{row[0]:<15} {row[1]:<12} {row[2]:<10} {row[3]}")

    print()


def search_student():
    student_name = input("Enter student name to search: ").strip().lower()
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        print("\n--- Search Results ---")

        for row in reader:
            if row[0].lower() == student_name:
                print(f"Name: {row[0]} | Date: {row[1]} | Time: {row[2]} | Status: {row[3]}")
                found = True

    if not found:
        print("No record found.")

    print()


def attendance_summary():
    present_count = 0
    absent_count = 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[3] == "Present":
                present_count += 1
            elif row[3] == "Absent":
                absent_count += 1

    print("\n--- Attendance Summary ---")
    print(f"Total Present: {present_count}")
    print(f"Total Absent : {absent_count}\n")


while True:
    print("===== Attendance Management System =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Search Student Record")
    print("4. Attendance Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        mark_attendance()

    elif choice == '2':
        view_attendance()

    elif choice == '3':
        search_student()

    elif choice == '4':
        attendance_summary()

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")
