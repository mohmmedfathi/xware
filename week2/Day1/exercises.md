# :muscle: exercises on the Faculty DB 
``` sql
sudo -u postgres psql
\l

create database Faculty_DB;
\c faculty_db
```
## :grey_exclamation: Insert Data Into These Tables

  **:one:&nbsp; Insert One Faculty** <br>
  **:two:&nbsp; Insert Three Departments Into This Faculty** <br>
  **:three:&nbsp; Insert nine Subjects** <br>
  **:four:&nbsp; Insert Courses With Defferent Durations** <br>
  **:five:&nbsp; Insert Atleast Five Students In Every Department** <br>
  **:six:&nbsp; Insert Exams For Every Course** <br>

### :hammer: **Insert One Faculty**

```sql
INSERT INTO faculty (id ,name) VALUES (1, 'mohmmed');
select * from faculty;
```
### :hammer: **Insert Three Departments Into This Faculty**

```sql
INSERT INTO department (id,name) VALUES(1,'math');

INSERT INTO department (id,name) VALUES(2,'science');

INSERT INTO department (id,name) VALUES(3,'cs');

select * from department;
```

### :hammer: **Insert nine Subjects**
```sql

INSERT INTO subject(id,name,code) VALUES(1,'s1',11);

INSERT INTO subject(id,name,code) VALUES(2,'s2',22);

INSERT INTO subject(id,name,code) VALUES(3,'s3',33);

INSERT INTO subject(id,name,code) VALUES(4,'s4',44);

INSERT INTO subject(id,name,code) VALUES(5,'s5',55);

INSERT INTO subject(id,name,code) VALUES(6,'s6',66);

INSERT INTO subject(id,name,code) VALUES(7,'s7',77);

INSERT INTO subject(id,name,code) VALUES(8,'s8',88);

INSERT INTO subject(id,name,code) VALUES(9,'s9',99);
```

### :hammer: **Insert Courses With Defferent Durations**
```sql 
INSERT INTO course(id,duration) VALUES(21,'3 week');

INSERT INTO course(id,duration) VALUES(483,'8 week');
```
### :hammer: **Insert Exams For Every Course**
```sql
INSERT INTO Exams (id,date,duration) VALUES(1,'11-11-2022','3 month');

INSERT INTO Exams (id,date,duration) VALUES(6,'5-12-2022','3 week');

INSERT INTO Exams (id,date,duration) VALUES(8,'10-1-2022','7 week');
```

# :up: QUERY EXERCISES
![Screenshot from 2022-07-30 14-57-34](https://user-images.githubusercontent.com/64088888/181915389-055ff6f4-b004-424e-8ba1-ae77da598691.png)

### :hammer: **Select all Students, Professor, Subjects, Courses, Exams, Departments**
```sql
select * from student;

select * from professor;

select * from subject;

select * from course;

select * from exams;

select * from department;
```
### :hammer: **Select all Professors with the Age is 40**
```sql
select * from professor where age = 40
```
### :hammer: **Select all Professors with the salary greater than 10000**
```sql
select * from professor where salary >10000;
```

### :hammer: **Order the Professors by the salary**

```sql
select * from professor order by salary;
```
### :hammer: **Order the students by the Birth_Date**

```sql
select * from student  order by birth_date;
```

### :hammer: **Get the average salary of the Professors**
```sql
SELECT AVG(salary) from professor;
```

### :hammer: **Update the salary of the Professors with the salary greater than 10000 to 20000**
```sql 
update professor set salary = 20000 where salary > 10000;
```
### :hammer: **Delete the Professors with the salary greater than 20000**
```sql
delete from professor where salary > 10000;
```

# :eyes: exercises on pgexercises.com

**:ballot_box_with_check: &nbsp; [Retrieve everything from a table](https://pgexercises.com/questions/basic/selectall.html)**
```sql
select *
from cd.facilities
```
**:ballot_box_with_check: &nbsp; [Retrieve specific columns from a table](https://pgexercises.com/questions/basic/selectspecific.html)**
```sql
select name,membercost
from cd.facilities
```
**:ballot_box_with_check: &nbsp; [Control which rows are retrieved](https://pgexercises.com/questions/basic/where.html)**
```sql
select *
from cd.facilities
where membercost >0
```
**:ballot_box_with_check: &nbsp; [ Control which rows are retrieved - part 2](https://pgexercises.com/questions/basic/where2.html)**
```sql
select facid, name, membercost, monthlymaintenance 
	from cd.facilities 
	where 
		membercost > 0 and (membercost < monthlymaintenance/50.0);   
```
