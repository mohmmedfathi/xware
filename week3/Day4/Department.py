
def creating_Department():
    print("Department is created")
dep_info = []
def reading_Department():
 number_of_department = int(input("enter number of department : "))
 for i in range (number_of_department):
             dic = {}
             dep_name = input(f"enter department name of " + str(i + 1) + " : ")
             dep_id = input("enter the id " + str(i + 1) + ": " )
             dic[dep_id]=dep_name
             dep_info.append([dep_name,dep_id])
            
            

def update_Department():
    print ("the content of Department is : ")
    print(dep_info)
    print ("enter index to update item : ")
    idx = int(input("index : "))
    del dep_info[idx]
    value = input("enter name of this Department : ")
    key = input("enter id of this Department : ")
    dep_info.append([value , key])
    
def retrieve_list():
    print ("Departments names : ") 
    print(dep_info)
    
    for i in range (len(dep_info)):
        print("the Department " + str(i+1) + " name : " +str(dep_info[i][0]))
        print("the Department "+ str(i+1) + " id : " + str(dep_info[i][1]))
        

def read_specific_Department_Info():
    #make try and except
            idx = int(input("enter idx : "))
            return dep_info[idx]