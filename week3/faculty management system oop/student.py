class Students:
    def __init__(self):
        self.lst = []

    def creating_students(self):
        self.student_info_helper()

    def student_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        student_id = input("enter id : ")
        student_name = input("enter student name : ")
        student_department = input("enter department name : ")
        dic[student_id] = {
            "student name": student_name,
            "student department": student_department
        }
        if not is_update_operation:
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def reading_all_students_info(self):
        print("-" * 50)

        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(' id of student = ', str(key), end=" ")
                    print(" ,name of student = " + str(value["student name"]), end=" ")
                    print(" ,department of student = " + str(value["student department"]))
        else:
            print("there is no student until now")

        print("-" * 50)

    def reading_specific_student_info(self):
        self.reading_all_students_info()
        idx = int(input("enter the index of record you want : "))
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

    def update_specific_student_info(self):
        self.reading_all_students_info()
        search_filter = input("enter id or name of student : ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value["student name"] == search_filter:
                        self.student_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
                idx += 1
            if not filter_in_list and isinstance(search_filter, int):
                print("student id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("student name entered not in list")
        else:
            print("you cant enter inter and string together ")

d = Students()
d.creating_students()
d.reading_all_students_info()
d.reading_specific_student_info()
d.update_specific_student_info()
d.reading_all_students_info()