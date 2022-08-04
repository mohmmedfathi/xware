
import Department
import Course
import Fuculity
import Professor
import Student
import Exams

#exit
while True:
    print(" 1 ---> reading Department info")
    print(" 2 ---> update specific Department ")
    print(" 3 ---> retrieve list ")
    print(" 4 ---> read specific Department ")
    
    print("--------------------------------")
    
    print(" 5 ---> Reading Faculty Info")
    print(" 6 ---> Update Faculty Info ")
    print(" 7 ---> Link Professors To Faculty ")
    print(" 8 ---> Link Departments To Faculty ")
    print(" 9 ---> retreive the content")
    
    print("--------------------------------")
    
    print(" 10 ---> Link Professor To Course")
    print(" 11 ---> Link Exams To Course")
    print(" 12 ---> Update Specific Course Info")
    print(" 13 ---> retreive the content")
    print(" 14 ---> Reading Course Info")
    
    print("--------------------------------")
    
    print(" 15 ---> Reading All Exams Info")
    print(" 16 ---> update Specific Exam Info")
    print(" 17 ---> read Specific Exam Info")
    print(" 18 ---> retrieve all exam info ")
    
    print("--------------------------------")

    print(" 19 ---> Reading All Student Info")
    print(" 20 ---> update Specific Student Info")
    print(" 21 ---> read Specific Student Info")
    print(" 22 ---> retrieve all Student info ")
    
    print("--------------------------------")
    
    print(" 23 ---> Reading All Professors Info")
    print(" 24 ---> update Specific Professor Info")
    print(" 25 ---> read Specific Professor Info")
    print(" 26 ---> retrieve all Professor info ")
    
    print("--------------------------------")
    
    print(" 27 ---> exit from program")
    
    x = int(input())
    if (x == 1):
        Department.reading_Department()
    elif (x==2):
        Department.update_Department()
    elif(x==3):
        print(Department.retrieve_list())
    elif(x==4):
        print(Department.read_specific_Department_Info())
    elif (x == 5):
        Fuculity.reading_faculty()
    elif (x==6):
        Fuculity.update_faculty()
    elif(x==7):
        Fuculity.link_professors_to_Fuculity()
    elif(x==8):
        Fuculity.link_Departments_to_Fuculity()
    elif(x==9):
        Fuculity.retrieve_list()
    elif (x == 10):
        Course.link_professors_to_Course()
    elif (x==11):
        Course.link_Exams_to_Course()
    elif(x==12):
        Course.update_Course()
    elif(x==13):
        print(Course.retrieve_list())
    elif (x==14):
        Course.reading_Course()
    elif (x == 15):
        Exams.reading_Exams()
    elif (x==16):
        Exams.update_specific_Exams_Info()
    elif(x==17):
       print(Exams.read_specific_Exams_Info())
    elif(x==18):
       print(Exams.retrieve_list())
    elif (x == 19):
        Student.reading_Students()
    elif (x==20):
        Student.update_specific_Students_Info()
    elif(x==21):
       print(Student.read_specific_Students_Info)
    elif(x==22):
       print(Student.retrieve_list())
    elif (x == 23):
        Professor.reading_Professors()
    elif (x==24):
        Professor.update_specific_Professors_Info()
    elif(x==25):
       print(Professor.read_specific_Professor_Info())
    elif(x==26):
       print(Professor.retrieve_list())
    elif(x==27):
        break
    else :
        print("you entered invalid number.")










  

   
   

    
   
    