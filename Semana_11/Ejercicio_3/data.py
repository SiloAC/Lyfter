import csv
from student import Student, create_student_from_dict

def export_to_csv(students):
    if not students:
        print("No data to export.")
        return
    with open("students.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "section", "spanish", "english", "social", "science"])
        writer.writeheader()
        for student in students:
            writer.writerow(student.to_dict())
    print("Data exported successfully to 'students.csv'.")

def import_from_csv():
    students = []
    try:
        with open("students.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    student = create_student_from_dict(row)
                    students.append(student)
                except Exception as e:
                    print(f"Error importing a row: {e}")
        print(f"{len(students)} students imported from 'students.csv'.")
    except FileNotFoundError:
        print("No 'students.csv' file found to import.")
    return students