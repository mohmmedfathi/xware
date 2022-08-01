
faculty_name= input ("Please Enter Faculty Name:")

number_of_department = int(input("How Many Department in The Faculty: "))
dep_info = []
for i in range (number_of_department):
    dep_name = input(f"enter department name of " + str(i + 1) + " : ")
    dep_info.append(dep_name)

Professors = dict()
n = int(input("Enter number of Professors :"))
for i in range(n):
        id = input(f"Enter id of Professor " + str (i+1) + " : ")
        while (type(id) != int):
            print ("please enter integer value")
            id = input(f"Enter id of Professor " + str (i+1) + " : ")
        pinfo= []
        name = input("Enter names of Professor "+ str (i+1) + " : ")
        ssn = input ("enter  ssn : ")
        while (type(ssn) != int):
            print ("please enter integer value")
            ssn = input(f"Enter ssn of Professor " + str (i+1) + " : ")
        department = input ("enter department of Professor "+ str (i+1) + " : ")
        age = input ("enter age : ")
        while (type(age) != int):
            print ("please enter integer value")
            age = input(f"Enter age of Professor " + str (i+1) + " : ")
        nationality = input ("enter nationality of Professor "+ str (i+1) + " : ")
        city = input ("enter city : ")
        salary = input ("enter salary of Professor "+ str (i+1) + " : ")
        while (type(salary) != float):
            print ("please enter float value")
            salary = input(f"Enter salary of Professor " + str (i+1) + " : ")
        pinfo.extend([name,ssn,department,age,nationality,city,salary])
        Professors[id] = pinfo
        

number_of_students = int(input("Please Enter Student Number : "))
students = dict()
for i in range (number_of_students):
        id = input("Enter id of student "+ str (i+1) + " : ")
        while (type(id) != int):
            print ("please enter integer value")
            id = input(f"Enter id of student " + str (i+1) + " : ")
        sinfo = []
        name = input("Enter names of student "+ str (i+1) + " : ")
        ssn = input ("enter  ssn : ")
        while (type(ssn) != int):
            print ("please enter integer value")
            ssn = input(f"Enter ssn of student " + str (i+1) + " : ")
        department = input ("enter department  of student "+ str (i+1) + " : ")
        age = int (input ("enter age : "))
        while (type(age) != int):
            print ("please enter integer value")
            age = input(f"Enter age of student " + str (i+1) + " : ")
        nationality = input ("enter nationality of student  "+ str (i+1) + " : ")
        city = input ("enter city : ")
        faculty = input ("enter faculty  of student "+ str (i+1) + " : ")
        sinfo.extend([name,ssn,department,age,nationality,city,faculty])
        students[id] = sinfo



number_of_subject = int(input("Please Enter Subjects Number : "))
subjects = dict()
for i in range (number_of_subject):
    code = input ("enter code of subject  "+ str (i+1) + " : ")
    subinfo = []
    name = input("Enter names of subject "+ str (i+1) + " : ")
    year = input ("enter year for this subject "+ str (i+1) + " : ")
    while (type(year) != int):
            print ("please enter integer value")
            age = input(f"Enter year of Subject " + str (i+1) + " : ")
    department = input ("enter department of subject "+ str (i+1) + " : ")   
    subinfo.extend([name,year,department])
    subjects[code] = subinfo


"""
i considered the key in course is id 
and 
subject is code and the informations same 
"""

number_of_courses = int(input("Please Enter Courses Number: : "))
courses = dict()
for i in range (number_of_courses):
    id = input ("enter id of course "+ str (i+1) + " : ")
    courseinfo = []
    name = input("Enter name of course "+ str (i+1) + " : ")
    year = input ("enter year for this course "+ str (i+1) + " : ")
    while (type(year) != int):
            print ("please enter integer value")
            age = input(f"Enter year of course " + str (i+1) + " : ")
    department = input ("enter department of course "+ str (i+1) + " : ")   
    courseinfo.extend([name,year,department])
    courses[code] = courseinfo



number_of_exams = int(input("Please Enter Exams Number: : "))
exams = dict()
for i in range (number_of_exams):
    id = input ("enter id of exam "+ str (i+1) + " : ")
    examinfo = []
    name = input("Enter name of exam "+ str (i+1) + " : ")
    year = input ("enter year for this exam "+ str (i+1) + " : ")
    while (type(year) != int):
            print ("please enter integer value")
            age = input(f"Enter year of exam " + str (i+1) + " : ")
    department = input ("enter department of exam  "+ str (i+1) + " : ")   
    examinfo.extend([name,year,department])
    courses[id] = courseinfo



print ("The Faculty name is " + faculty_name)
counter = 1
print ("Departments names : ") 
for i in dep_info :
    print(f"the department " + str(counter) + " = " + i)
    counter+=1

# [name,ssn,department,age,nationality,city,salary])

print("\n Professors info : ")
for i in Professors :
    print ("Professor with id " + str (i) + " : ")
    print ("name is : " + str(Professors[i][0]))
    print ("ssn is : " + str(Professors[i][1]))
    print ("department is : " + str(Professors[i][2]))
    print ("age is : " + str(Professors[i][3]))
    print ("nationality is : " + str(Professors[i][4]))
    print ("city is : " + str(Professors[i][5]))
    print ("salary is : " + str(Professors[i][6]))
    


print("\n students info : ")
for i in students :
    print (str(i)  + " = " + str(students[i]))
    
    print ("Professor with id " + str (i) + " : ")
    print ("name is : " + str(students[i][0]))
    print ("ssn is : " + str(students[i][1]))
    print ("department is : " + str(students[i][2]))
    print ("age is : " + str(students[i][3]))
    print ("nationality is : " + str(students[i][4]))
    print ("city is : " + str(students[i][5]))
    print ("faculty is : " + str(students[i][6]))

print("\n subjects info : ")
for i in subjects :
    
    print ("subject with code " + str (i) +  " : ")
    print ("name is : " + str(subjects[i][0]))
    print ("year is : " + str(subjects[i][1]))
    print ("department is : " + str(subjects[i][2]))

print("\n courses info : ")
for i in courses :
    print ("course with id " + str (i) + " : ")
    print ("name is : " + str(courses[i][0]))
    print ("year is : " + str(courses[i][1]))
    print ("department is : " + str(courses[i][2]))
print("\n exams info : ")
for i in exams :
    print ("exam with id " + str (i) + " : ")
    print ("name is : " + str(exams[i][0]))
    print ("year is : " + str(exams[i][1]))
    print ("department is : " + str(exams[i][2]))
    
print("Made With Love By ( XWARE BOOT CAMP )")
