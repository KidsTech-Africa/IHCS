print("EXPERT SYSTEM FOR MEDICAL DOCTOR")
print("---------------------------------------------------")
firstname = input("Enter Your First Name")
lastname = input("Enter Your Last Name")
phone = input("Enter Your Phone Number")
address = input("Enter Your Home Address")
gender = input("Enter M for Male or F for Female")
if gender == "M" or gender == "m":
    print("Welcome " + lastname + " " + firstname + "  sir")
elif gender == "F"or gender == "f":
    print("Welcome " + lastname + " " + firstname + "  ma")
symptomlist = ("eye irritation","Runny nose", "Stuffy nose","puffy,watery eyes","sneezing","inflamed,itchy nose and throat","hives or skin rashes","Gastrointestinal distress (diarrhea, nausea, vomiting,excessing gas,indigestion)","tingling or swelling of the lips,face,or tongue","itchinesss","dificulty brething or wheezing","fainting or lighttheadedness","fever 100F","headache","pain and fatique","more severe, often dry cough")
print("Select any sign and symptoms you are feeling")
sn = 1
for symptom in symptomlist:
    strsn = str(sn)
    print(strsn + " for " + symptom)
    print("   ")
    sn = sn + 1
usersymptoms = input("Enter Your Symptom(s). E.g 1,2,3  ")
allergies = "123456"
coldflu ="13141516"

realsymptom = usersymptoms.split(",")
listsym=""
for sym in realsymptom:
    listsym = listsym + sym

if listsym == "123456":
    print("You may be suffering from ALLERGIES")
if listsym == "13141516":
    print("You may be suffering from COLD AND FLU")
    
    

