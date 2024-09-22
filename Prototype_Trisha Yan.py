import csv
# this is branch1


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
#print(lists)


header = "{:22s}  {:22s}  {:22s}  {:22s}  {:22s}  {:22s}  {:22s}".format("ID","Name","Age","Major","Department","Units to Complete","Has Student Loan")
table=""
for u in range(len(lists[0])):
    for unit in lists:
        if unit[u].isdigit():
            table=table + "{:>22s}  ".format(unit[u])
        else:
            table =table + "{:<22s}  ".format(unit[u])
    table =table + "\n"
print(header)
print(table)
# for unit in lists:
#     for u in range(len(unit)):
#         table = table + unit[u]
#print(table)
'''
for u in range(len(lists[0])):
    for unit in lists:
        # for u in range(len(lists)):
        #     table = table + unit[u]
        table += unit[u]
    table += "\n"
print(table)

'''