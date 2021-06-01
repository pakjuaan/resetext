import ast

arr=[]
f = open('data.txt', 'r')
for x in f:
    arr.append(ast.literal_eval(x))

if len(arr) == 0:
    print("Empty!")
    input("\nPress Enter to continue...")
    
else:
    for i in arr:
        print("Patient's Name:\t\t\t", i["name"])
        print("Doctor:\t\t\t\t", i["doctor"])
        print("Consultation Date:\t\t", i["date"])
        print("Hospital/Clinic:\t\t", i["hospital"])
        print("Prescribed Medicine:\t\t", i["medicine"])
        print("Doctor's Field of Expertise:\t", i["field"])
        print("Patient's Diagnosis:\t\t", i["illness"])
        print("Notes:\t\t\t\t", i["notes"])
        print()