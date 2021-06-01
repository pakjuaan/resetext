a=[]

name = input("Enter patient's name: ")
doctor = input("Enter doctor: ")
date = input("Enter date: ")
hospital = input("Enter hospital: ")
medicine = input("Enter medicine: ")
field = input("Enter doctor's field of expertise: ")
illness = input("Enter patient's diagnosis: ")
notes = input("Enter notes: ")

a.append({"name": name, "doctor": doctor, "date": date, "hospital": hospital, "medicine": medicine, "field": field, "illness": illness, "notes": notes})
        
with open('data.txt', 'a') as data:
    for i in a:
        data.write(str(i) + '\n')

print("\nInformation saved!")
input("Press Enter to continue...")
        