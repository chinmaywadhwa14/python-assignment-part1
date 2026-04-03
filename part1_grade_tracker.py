# ==================================================
# TASK 1: Data Parsing & Profile Cleaning
# ==================================================
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72"},
    {"name": "Priya Nair", "roll": "103", "marks_str": "91, 85, 88, 94"},
    {"name": "Karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62"},
    {"name": "Sneha pillai", "roll": "105", "marks_str": "75, 80, 70, 68"}
]

for student in raw_students:
    # Clean name
    name = student["name"].strip().title()

    # Validate name
    if not all(word.isalpha() for word in name.split()):
        continue

    # Convert roll
    roll = int(student["roll"])

    # Convert marks
    marks = [int(m.strip()) for m in student["marks_str"].split(",")]

    # Print output
    print(f"Student: {name}")
    print(f"Roll No: {roll}")
    print(f"Marks: {marks}")
    print("----------------------")


# ==================================================
# TASK 2: Marks Analysis Using Loops & Conditionals
# ==================================================

student_name = "Ayesha Sharma"

subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nStudent: {student_name}\n")

# 1. Print each subject with marks and grade
for i in range(len(subjects)):
    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], "-", mark, "-", grade)

# 2. Total and Average
total = sum(marks)
print("\nTotal Marks:", total)

average = total / len(marks)
print("Average:", round(average, 2))

# 3. Highest Scoring Subject
max_mark = max(marks)
max_index = marks.index(max_mark)
print("Highest:", subjects[max_index], "-", max_mark)

# 4. Lowest Scoring Subject
min_mark = min(marks)
min_index = marks.index(min_mark)
print("Lowest:", subjects[min_index], "-", min_mark)

# 5. Add new subjects using while loop
while True:
    choice = input("\nDo you want to add a subject? (yes/no): ")

    if choice.lower() == "no":
        break

    subject = input("Enter subject name: ")

    try:
        mark = int(input("Enter marks: "))
    except:
        print("Invalid input. Please enter numbers only.")
        continue

    if mark < 0 or mark > 100:
        print("Invalid marks (must be 0–100)")
        continue

    subjects.append(subject)
    marks.append(mark)

# 6. Print updated list
print("\nUpdated List:")
for i in range(len(subjects)):
    print(subjects[i], "-", marks[i])


# ============================================================
# TASK 3: Class Performance Summary
# ============================================================

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

pass_count = 0
fail_count = 0
total_class_average = 0

print("\nName | Average | Status")
print("-" * 35)

for student in class_data:
    name = student[0]
    marks = student[1]

    avg = sum(marks) / len(marks)
    avg = round(avg, 2)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    print(name, "|", avg, "|", status)

    total_class_average += avg

class_average = total_class_average / len(class_data)
class_average = round(class_average, 2)

print("\nSummary:")
print("Passed:", pass_count)
print("Failed:", fail_count)
print("Class Average:", class_average)


# ============================================================
# TASK 4: String Manipulation Utility
# ============================================================

essay = "   python is a versatile language. it supports object oriented programming. Python is widely used in data science.   "

# 1. Clean spaces
clean_essay = essay.strip()
print("Cleaned Essay:", clean_essay)

# 2. Title Case
title_essay = clean_essay.title()
print("\nTitle Case:", title_essay)

# 3. Count 'python' (case-insensitive)
count_python = clean_essay.lower().count("python")
print("\nCount of 'python':", count_python)

# 4. Replace all forms of 'python' → 'Python 3'
replaced_essay = clean_essay.lower().replace("python", "Python 3")
print("\nReplaced Essay:", replaced_essay)

# 5. Split sentences
sentences = clean_essay.split(". ")

# 6. Print numbered sentences properly
print("\nSentences:")
for i in range(len(sentences)):
    sentence = sentences[i].strip()

    if sentence != "":
        if not sentence.endswith("."):
            sentence += "."

        print(f"{i+1}. {sentence}")
