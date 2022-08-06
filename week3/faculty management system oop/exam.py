class Exams:
    def __init__(self):
        self.lst = []

    def creating_exams(self):
        self.exam_info_helper()

    def exam_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        exam_id = input("enter id : ")
        exam_name = input("enter exam name : ")
        exam_department = input("enter department name : ")
        dic[exam_id] = {
            "exam name": exam_name,
            "exam department": exam_department
        }
        if not is_update_operation:
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def reading_all_exams_info(self):
        print("-" * 50)

        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(' id of exam = ', str(key), end=" ")
                    print(" ,name of exam = " + str(value["exam name"]), end=" ")
                    print(" ,department of exam = " + str(value["exam department"]))
        else:
            print("there is no exam until now")

        print("-" * 50)

    def reading_specific_exam_info(self):
        self.reading_all_exams_info()
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

    def update_specific_exam_info(self):
        self.reading_all_exams_info()
        search_filter = input("enter id or name of exam : ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value["exam name"] == search_filter:
                        self.exam_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
                idx += 1
            if not filter_in_list and isinstance(search_filter, int):
                print("exam id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("exam name entered not in list")
        else:
            print("you cant enter inter and string together ")

d = Exams()
d.creating_exams()
d.reading_all_exams_info()
d.reading_specific_exam_info()
d.update_specific_exam_info()
d.reading_all_exams_info()