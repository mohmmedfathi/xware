
import course
import department
import exam 
import faculty
import professor
import student
import subject

cours = course.Course()
dep = department.Department()
exm = exam.Exams()
faclty = faculty.faculty()
prof = professor.Professors()
studnt = student.Students()
sbjct = subject.Subject()

print("welcome ^_^")

def Application():
    while True:
        #faculty
        print(" 1 ---> Creating Faculty")
        print(" 2 ---> Reading Faculty Info")
        print(" 3 ---> Update Faculty Info")
        print(" 4 ---> Link Professors To Faculty")
        print(" 5 ---> Link Departments To Faculty")
        
        #department
        print('*' * 50)    
        print(" 6 ---> Creating Department")
        print(" 7 ---> Reading  All Departments Info")
        print(" 8 ---> Reading Specific Department Info")
        print(" 9 ---> Update Specific Department Info")
        
        print('*' * 50)   
        #subject 
        print(" 10 ---> Creating Subject")
        print(" 11 ---> Reading  All Subjects Info")
        print(" 12 ---> Reading Specific Subject Info")
        print(" 13 ---> Update Specific Subject Info")
        print(" 14---> Link Course To Subject")
        print(" 15 ---> Link Professors To Subject")
        
        print('*' * 50)  
        # Course
        print(" 16 ---> Creating Course")
        print(" 17 ---> Reading  All Courses Info")
        print(" 18 ---> Reading Specific Course Info")
        print(" 19 ---> Update Specific Course Info")
        print(" 20 ---> Link Professors To Course")
        print(" 21 ---> Link Exams To Course")
        
        print('*' * 50)  
        

        # Exams
        print(" 22 ---> Creating Exam")
        print(" 23 ---> Reading  All Exams Info")
        print(" 24 ---> Reading Specific Exam Info")
        print(" 25 ---> Update Specific Exam Info")
        
        print('*' * 50) 
        # Student
        print(" 26 ---> Creating Student")
        print(" 27 ---> Reading  All Students Info")
        print(" 28 ---> Reading Specific Student Info")
        print(" 29 ---> Update Specific Student Info")
        
        print('*' * 50) 
        # Professor
        print(" 30 ---> Creating Professor")
        print(" 31 ---> Reading  All Professors Info")
        print(" 32 ---> Reading Specific Professor Info")
        print(" 33 ---> Update Specific Professor Info")
        
        print(" 34 ---> exit the program")
        print('*' * 50) 
        
        

        x = int(input())
        
        
        #faculty
        if (x == 1):
            faclty.create_faculty()
        elif (x==2):
            faclty.reading_faculty_info()
        elif(x==3):
            faclty.update_faculty_info()
        elif(x==4):
            faclty.link_professors_to_faculty()
        elif (x == 5):
            faclty.link_departments_to_faculty()
            
            
        #department
        elif (x==6):
            dep.creating_department()
        elif(x==7):
            dep.reading_all_departments_info()
        elif(x==8):
            dep.reading_specific_departments_info()
        elif(x==9):
            dep.update_specific_department_info()
            
            
        #subject 
        elif (x == 10):
            sbjct.creating_subject()
        elif (x==11):
            sbjct.reading_all_subjects_info()
        elif(x==12):
            sbjct.reading_specific_subject_info()
        elif(x==13):
            sbjct.update_specific_subject_info()
        elif (x==14):
            sbjct.link_course_to_subject()
        elif (x == 15):
            sbjct.link_professor_to_subject() 
            

        # Course
        elif (x==16):
            cours.creating_course()
        elif(x==17):
            cours.reading_all_courses_info()
        elif(x==18):
            cours.reading_specific_course_info()
        elif (x == 19):
            cours.update_specific_course_info()
        elif (x==20):
            cours.link_professor_to_course()
        elif(x==21):
            cours.link_exams_to_course()
        
        
        # Exams
        elif(x==22):
            exm.creating_exams()
        elif (x == 23):
            exm.reading_all_exams_info()
        elif (x==24):
            exm.reading_specific_exam_info()
        elif (x == 25):
            exm.update_specific_exam_info()
            

        # student
        elif (x==26):
            studnt.creating_students()
        elif(x==27):
            studnt.reading_all_students_info()
        elif(x==28):
            studnt.reading_specific_student_info()
        elif(x==29):
            studnt.update_specific_student_info()
        
        # Professor
        elif (x==30):
            prof.creating_professors()
        elif(x==31):
            prof.reading_all_professors_info()
        elif(x==32):
             prof.reading_specific_professor_info()
        elif(x==33):
            prof.update_specific_professor_info()
        
        elif(x==34):
            break
        
        else :
            print("you entered invalid number.")

    print("Made With love on Xware")