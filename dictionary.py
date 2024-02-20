def is_valid_age(age):
    """Check if the age is valid."""
    return 10 < age <= 20

def is_valid_location(location, students):
    """Check if the location is valid."""
    for student in students:
        if student["Location"] == location:
            return True
    return False

def print_students(location, students):
    """Print the names of students in a particular location."""
    print(f"Student(s) enrolled in this training location:")
    for student in students:
        if student["Location"] == location:
            print(student["Name"])

def main():
    print("Enter the number of student details to be created:")
    num_students = int(input())
    if num_students <= 0:
        print("Invalid Input")
        return

    students = []
    for i in range(num_students):
        print(f"Enter details for student #{i + 1}.")
        name = input("Name: ")
        age = int(input("Age: "))
        if not is_valid_age(age):
            print("Invalid Input")
            return
        location = input("Location: ")
        student = {"Name": name, "Age": age, "Location": location}
        students.append(student)

    print("\nHere's the list of student details:")
    for student in students:
        print(student)

    print("\nEnter the desired training location:")
    location = input()
    if not is_valid_location(location, students):
        print("Invalid location")
        return

    print_students(location, students)

if __name__ == "__main__":
    main()