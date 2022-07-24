#first (exercises on the Faculty DB)

# - Insert Data Into These Tables.
#Insert One Faculty
#Insert Three Departments Into This Faculty
#Insert Three Subjects In Every Department
#Insert Courses With Defferent Durations
#Insert Atleast Five Students In Every Department
#Insert Exams For Every Course

*************************************************************
sudo -u postgres psql

\l


create database Faculty_DB;

\c faculty_db

---------------------------------

INSERT INTO faculty (id ,name) VALUES (1, 'mohmmed');

select * from faculty;

---------------------------------

INSERT INTO department (id,name) VALUES(1,'math');

INSERT INTO department (id,name) VALUES(2,'science');

INSERT INTO department (id,name) VALUES(3,'cs');

---------------------------------

select * from department;

---------------------------------

INSERT INTO subject(id,name,code) VALUES(1,'s1',11);

INSERT INTO subject(id,name,code) VALUES(2,'s2',22);

INSERT INTO subject(id,name,code) VALUES(3,'s3',33);

INSERT INTO subject(id,name,code) VALUES(4,'s4',44);

INSERT INTO subject(id,name,code) VALUES(5,'s5',55);

INSERT INTO subject(id,name,code) VALUES(6,'s6',66);

INSERT INTO subject(id,name,code) VALUES(7,'s7',77);

INSERT INTO subject(id,name,code) VALUES(8,'s8',88);

INSERT INTO subject(id,name,code) VALUES(9,'s9',99);

---------------------------------

INSERT INTO course(id,duration) VALUES(21,'3 week');

INSERT INTO course(id,duration) VALUES(483,'8 week');

---------------------------------

INSERT INTO Exams (id,date,duration) VALUES(1,'11-11-2022','3 month');

INSERT INTO Exams (id,date,duration) VALUES(6,'5-12-2022','3 week');

INSERT INTO Exams (id,date,duration) VALUES(8,'10-1-2022','7 week');

*************************************************************

# - Select Data From Thse Tables.
#Select all Students, Professor, Subjects, Courses, Exams, Departments
#Select all Professors with the Age is 40
#Select all Professors with the salary greater than 10000
#Order the Professors by the salary
#Order the students by the Birth_Date
#Get the average salary of the Professors
#Update the salary of the Professors with the salary greater than 10000 to 20000
#Delete the Professors with the salary greater than 20000
#Update These Tables
#Set Students Line 2
#Add Age Column in Student Table
#Set Students Age
#Check All Exams Have Different Date And Time And If So Change These So Every Exam Have Different Date And Time

select * from student;

select * from professor;

select * from subject;

select * from course;

select * from exams;

select * from department;

---------------------------------

select * from professor where age = 40

select * from professor where salary >10000;

---------------------------------

select * from professor order by salary;

---------------------------------

select * from student  order by birth_date;

---------------------------------

SELECT AVG(salary) from professor;

---------------------------------

update Address set line2 = random()::int where line2 = NULL;

update professor set salary = 20000 where salary > 10000;

delete from professor where salary > 10000;

update Address set line2 = random()::int where line2 = NULL;

ALTER TABLE Student
ADD Age int;

update Student set age = 6 where age = NULL;

*************************************************************

exercises on pgexercises.com

1 - Retrieve everything from a table --> https://pgexercises.com/questions/basic/selectall.html

sol : 
select *
from cd.facilities

2- Retrieve specific columns from a table -->https://pgexercises.com/questions/basic/selectspecific.html
sol : 

select name,membercost
from cd.facilities

3 - Control which rows are retrieved --> https://pgexercises.com/questions/basic/where.html
sol : 
select *
from cd.facilities
where membercost >0

4 - Control which rows are retrieved - part 2 --> https://pgexercises.com/questions/basic/where2.html

sol:
select facid, name, membercost, monthlymaintenance 
	from cd.facilities 
	where 
		membercost > 0 and (membercost < monthlymaintenance/50.0);   
