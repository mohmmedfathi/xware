lst = list()
def creating_Exams():
    print("Professor is created")

def reading_Professors():
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
        lst.append(temp)
    
def read_specific_Professor_Info():
    idx = int(input("enter idx : "))
    return (lst[idx])

def update_specific_Professors_Info():
    print ("the content of Professors is : ")
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
    for i in lst:
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
                