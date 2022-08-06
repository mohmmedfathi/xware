class Subject:
    def __init__(self):
        self.lst = []
        self.course_lst = []
        self.professor_lst = []

    def creating_subject(self):
        self.subject_info_helper()

    def reading_all_subjects_info(self, subject_only=False):
        print("-" * 50)

        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(' id of subject = ', str(key), end=" ")
                    print(" ,name of subject = " + str(value["subject name"]), end=" ")
                    print(" ,department of subject = " + str(value["subject department"]))
        else:
            print("there is no subject until now")
        print("-" * 50)

        if not subject_only:
            # prof list
            print("professors : ")
            if self.professor_lst:
                for i in self.professor_lst:
                    for key, value in i.items():
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
            print("courses : ")
            if self.course_lst:
                for i in self.course_lst:
                    for key, value in i.items():
                        print("id of course : " + str(key))
                        print("name of course is : " + str(value["course name"]))
                        print("department of course  is : " + str(value["course department"]))
            else:
                print("there is no courses until now")
            print("-" * 50)

    def subject_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        subject_id = input("enter id : ")
        subject_name = input("enter subject name : ")
        subject_department = input("enter department name : ")
        dic[subject_id] = {
            "subject name": subject_name,
            "subject department": subject_department
        }
        if not is_update_operation:
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def reading_specific_subject_info(self):
        self.reading_all_subjects_info(subject_only=True)
        idx = int(input("enter the index of record you want : "))

        # i cant access self.lst[idx].items() and print every value alone..

        c = 1
        for i in list(enumerate(self.lst[idx].items())):
            for j in i:

                if c % 2 == 1:
                    print("idx = ", end="")
                    print(j)
                    c += 1
                else:
                    print("content = ", end="")
                    print(j)
                    c += 1

    # print(' id of subject = ', str(d.key), end=" ")
    # print(" ,name of subject = " + str(d["subject name"]), end=" ")
    # print(" ,department of subject = " + str(d["subject department"]))
    #        print(self.lst[idx])

    def update_specific_subject_info(self):
        self.reading_all_subjects_info()
        search_filter = input("enter id or name of subject: ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value["subject name"] == search_filter:
                        self.subject_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
                idx += 1
            if not filter_in_list and isinstance(search_filter, int):
                print("subject id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("subject name entered not in list")
        else:
            print("you cant enter inter and string together ")

    def link_course_to_subject(self):
        temp = dict()
        id = int(input(f"Enter id of course : "))
        name = input("Enter names of course : ")
        department = input("enter department of course  : ")
        temp[id] = {
            "course id": id,
            "course name": name,
            "course department": department
        }
        self.course_lst.append(temp)

    def link_professor_to_subject(self):
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


s = Subject()
s.creating_subject()
s.reading_specific_subject_info()
