lst = list()
def creating_Students():
    print("Exams is created")

def reading_Students():
        dic = dict()
        n = int(input("enter number of Students : "))
        for i in range (n):
            id = int(input(f"Enter id of Student " + " : "))
            name = input("Enter name of Student "+ " : ")

            dic[id] = {name}
            lst.append(dic)
    
def read_specific_Students_Info():
    idx = int(input("enter idx : "))
    return (lst[idx])

def update_specific_Students_Info():
    print ("the content of Students is : ")
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
             print('the id = ',str(key) + " " + " and student name = ",str(value))