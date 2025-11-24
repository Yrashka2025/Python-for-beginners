student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Accessing values
student_name = student["name"]
student_age = student["age"]

print("Student name:", student_name)
print("Student age:", student_age)

# Adding new key-value pairs
student["email"] = "alice@university.edu"
print("After adding email:", student)


student["gpa"] = 3.9
print("After updating GPA:", student)


del student["major"]
print("After removing major:", student)


print("Student details:")
for key in student:
    print(f"{key}: {student[key]}")
