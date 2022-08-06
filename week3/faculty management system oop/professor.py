class Professors:
    def __init__(self):
        self.lst = []

    def creating_professors(self):
        self.professor_info_helper()

    def professor_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        professor_id = input("enter id : ")
        professor_name = input("enter professor name : ")
        professor_department = input("enter department name : ")
        dic[professor_id] = {
            "professor name": professor_name,
            "professor department": professor_department
        }
        if not is_update_operation:
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def reading_all_professors_info(self):
        print("-" * 50)

        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(' id of professor = ', str(key), end=" ")
                    print(" ,name of professor = " + str(value["professor name"]), end=" ")
                    print(" ,department of professor = " + str(value["professor department"]))
        else:
            print("there is no professor until now")

        print("-" * 50)

    def reading_specific_professor_info(self):
        self.reading_all_professors_info()
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

    def update_specific_professor_info(self):
        self.reading_all_professors_info()
        search_filter = input("enter id or name of professor : ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value["professor name"] == search_filter:
                        self.professor_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
                idx += 1
            if not filter_in_list and isinstance(search_filter, int):
                print("professor id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("professor name entered not in list")
        else:
            print("you cant enter inter and string together ")

