lst = list()
def creating_Exams():
    print("Professor is created")

def reading_Professors():
        dic = dict()
        n = int(input("enter number of Professors : "))
        for i in range (n):
            id = int(input(f"Enter id of Professor " + " : "))
            name = input("Enter name of Professor "+ " : ")

            dic[id] = {name}
            lst.append(dic)
    
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
        #print('the id = ',i[0]+ " " + " and dep name = ",i[0])
        for key, value in i.items():
             print('the id = ',str(key) + " " + " and professor name = ",str(value))