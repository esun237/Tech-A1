import csv
# this is branch1
lists=[]
def loadR():
    global lists
    id=[]
    name=[]
    age=[]
    major=[]
    department=[]
    units_to_complete=[]
    has_student_loan=[]

    lists=[id,name,age,major,department,units_to_complete,has_student_loan]

    with open ("students.csv", mode='r') as file:
        csvFile = csv.reader(file)
        next(csvFile,None)

        for row in csvFile:
            for i in range(len(lists)):
                lists[i].append(row[i])


def displayT():
    header = "{:22s}  {:22s}  {:22s}  {:22s}  {:22s}  {:22s}  {:22s}".format("ID", "Name", "Age", "Major", "Department",
                                                                             "Units to Complete", "Has Student Loan")
    table = ""
    for u in range(len(lists[0])): #row
        for unit in lists:
            if unit[u].isdigit():
                table = table + "{:>22s}  ".format(unit[u])
            else:
                table = table + "{:<22s}  ".format(unit[u])
        table = table + "\n"
    print(header)
    print(table)

def add_record():
    global lists
    id = str(int(len(lists[0])) + 1)
    name = input("Enter name: ")
    age = input("Enter age: ")
    major = input("Enter major: ")
    department = input("Enter department: ")
    units_to_complete = input("Please enter how many units need to complete: ")
    has_student_loan = input("Any loan(please enter true or false): ")
#    lists[0].append(id)
#    lists[1].append(name)
#    lists[2].append(age)
#    lists[3].append(major)
#    lists[4].append(department)
#    lists[5].append(units_to_complete)
#    lists[6].append(has_student_loan)

    list = [id,name,age,major,department,units_to_complete,has_student_loan]
    for unit in range(len(list)): #loop 7 times [0] - [6]
        lists[unit].append(list[unit])

def delete_record():
    global lists
    id = input("Please enter the id you want to delete: ")
    if id in lists[0]: #if id in IDs
        unit_id=lists[0].index(id) #find the index number of id, and store index number to unit_id
        for unit in lists:
            del unit[unit_id]
    else:
        print("No such ID!")

def save_record():
    global lists
    f = open("students.csv", "w", newline="")
    writer = csv.writer(f)

    list = [] #rows
    for u in range(len(lists[0])):  # u demonstrate how many rows
        list.append([]) #append empty array to list
        for unit in lists: # for each u, loop 7 times
            list[u].append(unit[u]) #add id[0],name[0],age[0]... to row[0]
            #print(list)
    writer.writerow(["ID", "Name", "Age", "Major", "Department", "Units to Complete", "Has Student Loan"])
    for i in list:
        writer.writerow(i)
    f.close()


def menu():
    print("Application Title")
    print("1. Load records")
    print("2. Display")
    print("3. Add record")
    print("4. Delete record")
    print("5. Save record")
    print("6. Exit")
#variable to control the while loop
bolMyLoopControl = True

#create while loop
while bolMyLoopControl:
    menu()
    numChosen = int(input("Please choose: "))
    if numChosen == 1:
        print("Load records")
        loadR()
    elif numChosen == 2:
        print("Display")
        if lists:
            displayT()
        else:
            print("No records found!")
    elif numChosen == 3:
        add_record()
        print("Add record")
    elif numChosen == 4:
        delete_record()
        print("Delete record")
    elif numChosen == 5:
        save_record()
        print("Save record")
    else:
        bolMyLoopControl=False
        print("Exiting the menu")