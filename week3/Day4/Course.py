
lst = list()
def creating_Course():
    print("Course is created")

def reading_Course():
            dic = dict()

            id = int(input(f"Enter id of Course " + " : "))
            name = input("Enter name of Course "+ " : ")
            year = int(input("enter year of this course : "))
            dic[id] = {name,year}
            lst.append(dic)

def retrieve_list():
    return lst

def read_specific_Course_Info(idx):
    while True:
        try:
            idx = int(input("enter idx : "))
            return lst[idx]
        except :
            
                if (idx>=len(lst) or idx < 0):
                    print("the index is out of range")
                elif (type(idx)!=int):
                    print("please enter integer value")
                idx = int(input("enter idx : "))

def update_Course():
    print ("the content of Course is : ")
    print(lst)
    print ("enter index and value to update item : ")
    idx = int(input("index : "))
    while True:
        if (idx>=len(lst) or idx <0):
            print("idx invalid.")
            idx = int(input("index : "))
        else:
            break
    key = input("enter name of this attribute : ")
    value = input("enter the value : ")
    lst[idx] = {key : value}




def retrieve_list():
    return lst

def link_professors_to_Course():
    Professors = dict()
    n = int(input("enter number of Professors : "))
    for i in range(n):
        id = int(input(f"Enter id of Professor " + str (i+1) + " : "))
        while (type(id) != int):
            print ("please enter integer value")
            id = input(f"Enter id of Professor " + str (i+1) + " : ")
        
        name = input("Enter names of Professor "+ str (i+1) + " : ")
        ssn = int(input ("enter  ssn : "))
        while (type(ssn) != int):
            print ("please enter integer value")
            ssn = input(f"Enter ssn of Professor " + str (i+1) + " : ")
        department = input ("enter department of Professor "+ str (i+1) + " : ")
        age = int(input ("enter age : "))
        while (type(age) != int):
            print ("please enter integer value")
            age = input(f"Enter age of Professor " + str (i+1) + " : ")
        nationality = input ("enter nationality of Professor "+ str (i+1) + " : ")
        city = input ("enter city : ")
        salary = float(input ("enter salary of Professor "+ str (i+1) + " : "))
        while (type(salary) != float):
            print ("please enter float value")
            salary = input(f"Enter salary of Professor " + str (i+1) + " : ")
        Professors[id]= {name,ssn,department,age,nationality,city,salary}
        lst.append(Professors)

def link_Exams_to_Course():
    Exams = dict()
    n = int(input("enter number of Exams : "))
    for i in range(n):
        id = int(input(f"Enter id of Exams " + str (i+1) + " : "))
        while (type(id) != int):
            print ("please enter integer value")
            id = input(f"Enter id of Exams " + str (i+1) + " : ")
        Examsinfo= []
        name = input("Enter names of Exams "+ str (i+1) + " : ")
        
        department = input ("enter department of Exams "+ str (i+1) + " : ")
        
        Examsinfo={id,name,department}
        lst.append(Examsinfo)
