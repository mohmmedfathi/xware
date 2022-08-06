class Course:
    def __init__(self):
        self.lst = []
        self.professor_lst = []
        self.Exams_lst = []

    def creating_course(self):
        self.course_info_helper()

    def course_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        course_id = input("enter id : ")
        course_name = input("enter course name : ")
        course_department = input("enter department name : ")
        dic[course_id] = {
            "course name": course_name,
            "course department": course_department
        }
        if not is_update_operation:
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def reading_all_courses_info(self, course_only=False):
        print("-" * 50)

        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(' id of course = ', str(key), end=" ")
                    print(" ,name of course = " + str(value["course name"]), end=" ")
                    print(" ,department of course = " + str(value["course department"]))
        else:
            print("there is no course until now")
        print("-" * 50)

        if not course_only:
            # prof list
            print("professors : ")
            if self.professor_lst:
                for i in self.professor_lst:
                    for key, value in i.items():
                        print("id of professor : " + str(key),end = "\t")
                        print(", name is : " + str(value["professor name"]))
                        print("ssn is : " + str(value["ssn"]),end = "\t")
                        print(", department is : " + str(value["dep"]))
                        print("age is : " + str(value["age"]),end = "\t\t")
                        print(", nationality is : " + str(value["nationality"]))
                        print("city is : " + str(value["city"]),end = "\t")
                        print(", salary is : " + str(value["salary"]))
                        print()
            else:
                print("there is no professors until now")
            print("-" * 50)

            print("Exams : ")
            if self.Exams_lst:
                for i in self.Exams_lst:
                    for key, value in i.items():
                        print("id of Exam : " + str(key))
                        print("name of Exam is : " + str(value["exam name"]))
                        print("department of Exam  is : " + str(value["exam department"]))
                        print()
            else:
                print("there is no courses until now")
            print("-" * 50)

    def reading_specific_course_info(self):
        self.reading_all_subjects_info(course_only=True)
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

    def update_specific_course_info(self):
        self.reading_all_courses_info(course_only=True)
        search_filter = input("enter id or name of course : ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value["course name"] == search_filter:
                        self.course_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
                idx += 1
            if not filter_in_list and isinstance(search_filter, int):
                print("course id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("course name entered not in list")
        else:
            print("you cant enter inter and string together ")

    def link_professor_to_course(self):
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

    def link_exams_to_course(self):
        temp = dict()
        id = int(input(f"Enter id of exam : "))
        name = input("Enter names of exam : ")
        department = input("enter department of exam  : ")
        temp[id] = {
            "exam id": id,
            "exam name": name,
            "exam department": department
        }
        self.Exams_lst.append(temp)

