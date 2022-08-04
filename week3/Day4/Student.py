studentList = list()
CourseLst = list()
ProfessorLst = list()
def creating_Subject():
    print("Exams is created")

def Reading_All_Subjects_Info():
        
        n = int(input("enter number of Students : "))
        for i in range (n):
            dic = dict()
            id = int(input(f"Enter id of Student " + " : "))
            name = input("Enter name of Student "+ " : ")

            dic[id] = {"name" :name}
            studentList.append(dic)
    
def read_specific_Students_Info():
    idx = int(input("enter idx : "))
    return (studentList[idx])

def update_specific_Students_Info():
    print ("the content of Students is : ")
    print(studentList)
    print ("enter index and value to update item : ")
    idx = int(input("index : "))
    while True:
        if (idx>=len(studentList) or idx <0):
            print("idx invalid.")
            idx = int(input("index : "))
        else:
            break
    key = input("enter name of this attribute : ")
    value = input("enter the value : ")
    studentList[idx] = {key : value}
    
    
def retrieve_list():
    for i in studentList:
        for key, value in i.items():
                print("id of Student : " + str(key))
                print("name of Student is : " + str(value["name"]))
                print()
    for i in CourseLst:
        for key, value in i.items():
                print("id of Course : " + str(key))
                print("name of Course is : " + str(value["name"]))
                print("department of Course is : " + str(value["department"]))

    for i in ProfessorLst:
        for key, value in i.items():
                print("id of professor : " + str(key))
                print("name is : " + str(value["name"]))
                print("ssn is : " + str(value["ssn"]))
                print("department is : " + str(value["department"]))
                print("age is : " + str(value["age"]))
                print("nationality is : " + str(value["nationality"]))
                print("city is : " + str(value["city"]))
                print("salary is : " + str(value["salary"]))
                print()
                print()
                


def Link_Course_To_Subject() :
    dic = dict()
    id = int(input(f"Enter id of Course " + " : "))
    name = input("Enter name of Course "+  " : ")
    department = input ("enter department of Course "+ " : ")
    dic[id] = {"name" : name,"department" : department}
    CourseLst.append(dic)
    
def Link_Professor_To_Subject():
    n = int(input("enter number of professors : "))
    for i in range(n):
        
        temp = dict()
        id = int(input(f"Enter id of Professor " + str (i+1) + " : "))
        while (type(id) != int):
            print ("please enter integer value")
            id = input(f"Enter id of Professor " + str (i+1) + " : ")
        pinfo= []
        name = input("Enter names of Professor "+ str (i+1) + " : ")
        ssn = int(input ("enter  ssn : "))
        while (type(ssn) != int):
            print ("please enter integer value")
            ssn = int(input(f"Enter ssn of Professor " + str (i+1) + " : "))
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
            salary = float(input(f"Enter salary of Professor " + str (i+1) + " : "))
        temp[id] = {
                    "name" : name,
                    "ssn" : ssn,
                    "department" : department,
                    "age" : age,
                    "nationality" : nationality,
                    "city" : city,
                    "salary" : salary}
        ProfessorLst.append(temp)
    
