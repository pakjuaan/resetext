import ast

arr=[]
found = False
f = open('data.txt', 'r')
for x in f:
    arr.append(ast.literal_eval(x))

if len(arr) == 0:
    print("Already empty!")
    input("\nPress Enter to continue...")

else:
    print("DELETE\n\n[1]Select\n[2]Delete All")
    delsel = input("\nOption: ")

    if delsel == '1':
        search = input("Enter patient's name whose information you wish to delete: ")

        for i in range(len(arr)):
            if arr[i]['name'] == search:
                found = True
                break
        
        if found == True:   
            print("Patient's Name:\t\t\t", arr[i]["name"])
            print("Doctor:\t\t\t\t", arr[i]["doctor"])
            print("Consultation Date:\t\t", arr[i]["date"])
            print("Hospital/Clinic:\t\t", arr[i]["hospital"])
            print("Prescribed Medicine:\t\t", arr[i]["medicine"])
            print("Doctor's Field of Expertise:\t", arr[i]["field"])
            print("Patient's Diagnosis:\t\t", arr[i]["illness"])
            print("Notes:\t\t\t\t", arr[i]["notes"])

            arr.pop(i)
            with open('data.txt', 'w') as data:
                for j in arr:
                    data.write(str(j) + '\n')     

            print('Information deleted.')
            input("\nPress Enter to continue...")

        else:
            print("Not found!")
            input("\nPress Enter to continue...")

    else:
        arr.clear()
        with open('data.txt', 'w') as data:
            for j in arr:
                data.write(str(j) + '\n')        

        print('All information deleted.')
        input("\nPress Enter to continue...")

            
