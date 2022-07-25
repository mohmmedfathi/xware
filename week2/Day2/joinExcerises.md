



# This is Join Exercise
## Using College Management System Database With Joins
### Select Subject id, Subject Name, Subject Code, Course Duration in One Query
![carbon](https://user-images.githubusercontent.com/64088888/180866726-9392b962-d00c-4364-9850-c69eabe550a7.svg)

```bash
select subject.id,subject.name,subject.code,course.duration 
from subject
inner join course 
on subject.code = course.subject_code;
```
### Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query

```bash
select subject.id,subject.name,subject.code,course.duration,professor.name
from course 
inner join subject 
on course.sub_code = subject.sub_code
inner join professor
on course.p_id = professor.p_id;
```

### Select All Students With Thier Address In one Query
```bash
select student.id,student.f_name,student.l_name,student.f_phone,student.birth_date,student.age,Address.line1
from student_Address
inner join student 
on student_Address.student_id = student.id
inner join Address 
on student_Address.address_id= address.id;
```
### Select All Student Name In Every Couse.
```bash
select student.name
from student 
inner join course_Enrollment
on student.id = course_Enrollment.student_id;
```
