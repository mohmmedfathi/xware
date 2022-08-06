class Department:
    def __init__(self):
        self.lst = []

    def creating_department(self):
        self.department_info_helper()

    def department_info_helper(self, is_update_operation=False, indx=0):
        dic = dict()
        department_id = input("enter id : ")
        department_name = input("enter department name : ")
        dic[department_id] = department_name
        if (not is_update_operation):
            self.lst.append(dic)
        else:
            self.lst[indx] = dic

    def reading_all_departments_info(self):
        print("-" * 50)
        if self.lst:
            for i in self.lst:
                for key, value in i.items():
                    print(' id of department = ', str(key), end=" ")
                    print(" ,name of department= " + str(value))
        else:
            print("there is no departments until now")

        print("-" * 50)

    def reading_specific_departments_info(self):
        self.reading_all_departments_info()
        idx = int(input("enter the index of record you want : "))
        print(self.lst[idx])

    def update_specific_department_info(self):
        self.reading_all_departments_info()
        search_filter = input("enter id or name of department : ")
        if type(search_filter) == int or type(search_filter) == str:
            idx = 0
            filter_in_list = False
            for i in self.lst:
                for key, value in i.items():
                    if key == search_filter or value == search_filter:
                        self.department_info_helper(is_update_operation=True, indx=idx)
                        filter_in_list = True
                idx += 1
            if not filter_in_list and isinstance(search_filter, int):
                print("department id entered not in list")
            elif not filter_in_list and type(search_filter) == str:
                print("department name entered not in list")

        else:
            print("you cant enter inter and string together ")


