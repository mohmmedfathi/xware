class faculty:
    def __init__(self):
        self.lst = []
        self.professor_lst = []
        self.department_lst = []

    def create_faculty(self):
        self.faculty_info_helper()

    def reading_faculty_info(self):
        # print(self.lst)
        #self.lst
        print("-"*50)
        print("faculties : ")
        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(f"id = {key}")
                    print(f"faculty name = {value['faculty name']}", end="\t")
                    print(f"number of department = {value['num of department']}", end="\t")
                    print(f"number of employee = {value['num of employee']}")
        else:
            print("there is no faculty until now")
        print("-" * 50)

        # prof list
        print("professors : ")
        if  self.professor_lst:
            for i in self.professor_lst:
                for key,value in i.items():
                    print("id of professor : " + str(key))
                    print("name is : " + str(value["professor name"]))
                    print("ssn is : " + str(value["ssn"]))
                    print("department is : " + str(value["dep"]))
                    print("age is : " + str(value["age"]))
                    print("nationality is : " + str(value["nationality"]))
                    print("city is : " + str(value["city"]))
                    print("salary is : " + str(value["salary"]))
        else:
            print("there is no professors until now")
        print("-" * 50)
        print("departments : ")
        # dep list
        if  self.department_lst:
            for i in self.department_lst:
                for key, value in i.items():
                    print(' id of department = ', str(key),end= " ")
                    print(" ,name of department= " + str(value))
        else:
            print("there is no departments until now")

        print("-" * 50)

    def faculty_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        faculty_id = input("enter id : ")
        faculty_name = input("enter faculty name : ")
        num_of_department = input("enter number of department : ")
        num_of_employee = input("enter number of employee : ")
        dic[faculty_id] = {
            "faculty name": faculty_name,
            "num of department": num_of_department,
            "num of employee": num_of_employee
        }
        if (not is_update_operation):
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def update_faculty_info(self):
        self.reading_faculty_info()
        search_filter = input("enter id or name of faculty : ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value['faculty name'] == search_filter:
                        self.faculty_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
            if not filter_in_list and isinstance(search_filter, int):
                print("faculty id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("faculty name entered not in list")
            idx += 1
        else:
            print("you cant enter inter and string together ")

    def link_professors_to_faculty(self):
        temp = dict()
        id = int(input(f"Enter id of Professor : "))
        while type(id) != int:
            print("please enter integer value")
            id = input(f"Enter id of Professor : ")

        name = input("Enter names of Professor : ")
        ssn = int(input("enter  ssn : "))
        while type(ssn) != int:
            print("please enter integer value")
            ssn = int(input(f"Enter ssn of Professor : "))

        department = input("enter department of Professor  : ")
        age = int(input("enter age : "))
        while (type(age) != int):
            print("please enter integer value")
            age = input(f"Enter age of Professor : ")

        nationality = input("enter nationality of Professor : ")
        city = input("enter city : ")
        salary = float(input("enter salary of Professor : "))
        while type(salary) != float:
            print("please enter float value")
            salary = float(input(f"Enter salary of Professor : "))

        temp[id] = {"professor name": name,
                    "ssn": ssn,
                    "dep": department,
                    "age": age,
                    "nationality": nationality,
                    "city": city,
                    "salary": salary}

        self.professor_lst.append(temp)

    def link_departments_to_faculty(self):
            temp = {}

            dep_id = input(f"enter department id : ")
            dep_name = input(f"enter department name : ")
            temp[dep_id] = dep_name

            self.department_lst.append(temp)
