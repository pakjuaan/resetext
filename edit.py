import ast

arr=[]
found = False
f = open('data.txt', 'r')
for x in f:
    arr.append(ast.literal_eval(x))

if len(arr) == 0:
    print("Empty!")
    input("\nPress Enter to continue...")

else:
    search = input("Enter patient's name whose information you wish to edit: ")

    for i in range(len(arr)):
        if arr[i]['name'] == search:
            print("Patient's Name:\t\t\t", arr[i]["name"])
            print("Doctor:\t\t\t\t", arr[i]["doctor"])
            print("Consultation Date:\t\t", arr[i]["date"])
            print("Hospital/Clinic:\t\t", arr[i]["hospital"])
            print("Prescribed Medicine:\t\t", arr[i]["medicine"])
            print("Doctor's Field of Expertise:\t", arr[i]["field"])
            print("Patient's Diagnosis:\t\t", arr[i]["illness"])
            print("Notes:\t\t\t\t", arr[i]["notes"])
            print()

            name = input("Enter patient's name: ")
            doctor = input("Enter doctor: ")
            date = input("Enter date: ")
            hospital = input("Enter hospital: ")
            medicine = input("Enter medicine: ")
            field = input("Enter doctor's field of expertise: ")
            illness = input("Enter patient's diagnosis: ")
            notes = input("Enter notes: ")

            arr[i] = {"name": name, "doctor": doctor, "date": date, "hospital": hospital, "medicine": medicine, "field": field, "illness": illness, "notes": notes}
            found = True
            break

    if found == True:   
        with open('data.txt', 'w') as data:
            for j in arr:
                data.write(str(j) + '\n')        

        print("Changes saved!")
        input("\nPress Enter to continue...")

    else:
        print("Not found!")
        input("\nPress Enter to continue...")