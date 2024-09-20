import csv

id_student = []
name = []
age = []
major = []
department = []
units = []
uni_loan = []


def menu():
    while True:
        print("Application Title")
        print("1. Load records")
        print("2. Display")
        print("3. Add record")
        print("4. Delete record")
        print("5. Save records")
        print("6. Exit")

        choice = int(input("Please enter your choice between 1 and 6: "))
        if choice == 1:
            load_records()
        elif choice == 2:
            display_records()
        elif choice == 3:
            add_record()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            save_records()
        elif choice == 6:
            print("Exit menu")
            break
        else:
            print("Invalid choice.Please enter your choice between 1 and 6: ")

def load_records():
    with open("students.csv", mode="r") as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for entry in csv_file:
            id_student.append(int(entry[0]))
            name.append(entry[1])
            age.append(int(entry[2]))
            major.append(entry[3])
            department.append(entry[4])
            units.append(int(entry[5]))
            uni_loan.append(entry[6])
        print("Records loaded successfully")
        # return csv_file


def display_records():
    # load_records()
    print("{0:10s}".format("ID"),
          "{0:15s}".format("Name"),
          "{0:10s}".format("Age"),
          "{0:25s}".format("Major"),
          "{0:20s}".format("Department"),
          "{0:10s}".format("Units"),
          "{0:10s}".format("Uni_Loan"),
          )

    for i in range(len(id_student)):
        print("{0:10d}".format(id_student[i]), end=" ")
        print("{0:15s}".format(name[i]), end=" ")
        print("{0:10d}".format(age[i]), end=" ")
        print("{0:25s}".format(major[i]), end=" ")
        print("{0:20s}".format(department[i]), end=" ")
        print("{0:10d}".format(units[i]), end=" ")
        print("{0:10s}".format(uni_loan[i]))


def add_record():
    # load_records()
    next_id = len(id_student) + 1
    next_name = input("Name: ")
    next_age = int(input("Age: "))
    next_major = input("Major ")
    next_department = input("Department: ")
    next_units = int(input("Units: "))
    next_uni_loan = input("Uni Loan: ")
    id_student.append(next_id)
    name.append(next_name)
    age.append(next_age)
    major.append(next_major)
    department.append(next_department)
    units.append(next_units)
    uni_loan.append(next_uni_loan)

def delete_record():
    # load_records()
    delete_id = int(input("Enter the ID to be deleted: ")) - 1
    id_student.pop(delete_id)
    name.pop(delete_id)
    age.pop(delete_id)
    major.pop(delete_id)
    department.pop(delete_id)
    units.pop(delete_id)
    uni_loan.pop(delete_id)

def save_records():
    # load_records()
    with open("students.csv", "w") as file:
        writer = csv.writer(file)
        for i in range(len(id_student)):
            writer.writerow([id_student[i], name[i], age[i], major[i], department[i], units[i], uni_loan[i]])
        print("Records saved successfully")

menu()