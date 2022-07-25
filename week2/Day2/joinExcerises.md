



# This is Join Exercise
## Using College Management System Database With Joins
### Select Subject id, Subject Name, Subject Code, Course Duration in One Query
![carbon](https://user-images.githubusercontent.com/64088888/180866726-9392b962-d00c-4364-9850-c69eabe550a7.svg)
<details><summary><b>code</b></summary>
  
```bash
select subject.id,subject.name,subject.code,course.duration 
from subject
inner join course 
on subject.code = course.subject_code;
```
 </details>
 
### Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query
![carbon (1)](https://user-images.githubusercontent.com/64088888/180867145-66fedd25-22e3-49c1-8555-bcac7b0a022b.svg)
<details><summary><b>code</b></summary>
  
```bash
select subject.id,subject.name,subject.code,course.duration,professor.name
from course 
inner join subject 
on course.sub_code = subject.sub_code
inner join professor
on course.p_id = professor.p_id;
```
 </details>
 
### Select All Students With Thier Address In one Query
![carbon (2)](https://user-images.githubusercontent.com/64088888/180867150-dddad977-2805-4b87-bb78-9e9714ce921e.svg)

<details><summary><b>code</b></summary>
  
```bash
select student.id,student.f_name,student.l_name,student.f_phone,student.birth_date,student.age,Address.line1
from student_Address
inner join student 
on student_Address.student_id = student.id
inner join Address 
on student_Address.address_id= address.id;
```
  </details>
  
### Select All Student Name In Every Couse.
![carbon (3)](https://user-images.githubusercontent.com/64088888/180867157-70839323-e714-44c8-814d-c5f351211336.svg)

<details><summary><b>code</b></summary>
  
```bash
select student.name
from student 
inner join course_Enrollment
on student.id = course_Enrollment.student_id;
```
  </details>
