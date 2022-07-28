 
## **Apply Normalization Concept with Postgresql**
# make database Without Normalization
## professor table

```sql
create table if not exists professor(
    id int primary key NOT NULL,
    f_name varchar(10) NOT NULL,
    l_name varchar(10) NOT NULL,
	name varchar(30) NOT NULL,
    salary REAL NOT NULL,
    Age int NOT NULL ,
	birth_date varchar(10) NOT NULL,
	image varchar(5) ,
	email varchar(40) NOT NULL
);
```

## student table

```sql
create table if not exists student(
    id int primary key NOT NULL,
    f_name varchar(10) NOT NULL,
    l_name varchar(10) NOT NULL,
    f_phone int NOT NULL,
    l_phone int,
    birth_date varchar(20) NOT NULL ,
	image varchar(5) ,
	email varchar(40) NOT NULL
);
```

> :warning: **the email is small so inrease him with alter**
```
-- ALTER TABLE student ALTER COLUMN email TYPE varchar(40);
```
## insert records
``` sql
insert into student (id,f_name,l_name,f_phone,birth_date,email)
values (1,'mohmmed','fathi',01111442600,'27-11-2001','mohmmedfathi.123@gmail.com');
insert into student (id,f_name,l_name,f_phone,birth_date,email)
values (2,'ahmed','fathi',01117642600,'27-76-2001','fhgff.123@gmail.com');
insert into professor (id,f_name,l_name,name,salary,Age,birth_date,email)
values (1,'ahmed','mohammed','ahmed mohammed ahmed',2000,40,'1-1-2001','grfger@gmail.com');
insert into professor (id,f_name,l_name,name,salary,Age,birth_date,email)
values (2,'ahmed','mohammed','ahmed mohammed ahmed',2000,40,'1-1-2001','grfger@gmail.com');
```

## to show current data
``` sql
select * from student;
select *from professor;
```

******************************************


# drop coulmns and make normalization
```sql
ALTER TABLE professor
DROP f_name;
ALTER TABLE professor
DROP l_name;
ALTER TABLE professor
DROP name;
ALTER TABLE professor
DROP email;

ALTER TABLE student
DROP f_name;
ALTER TABLE student
DROP l_name;
ALTER TABLE student
DROP f_phone;
ALTER TABLE student
DROP l_phone;
ALTER TABLE student
DROP email;

```
```sql
create table if not exists professor( 
       id  primary key NOT NULL, 
	image varchar(5),
	salary REAL NOT NULL, 
	 Age int NOT NULL ,
	 birth_date varchar(10) NOT NULL,
);

create table if not exists professor_name(
	 id serial  primary key, 
	 f_name varchar(10) NOT NULL, 
   	 l_name varchar(10) NOT NULL, 
	 name varchar(30) NOT NULL,
     professor_id int references professor(id)
);

create table if not exists professor_links(
	 id serial int primary key NOT NULL, 
	 email varchar(40) NOT NULL,
	 linkedin_email varchar(40) NOT NULL,
	 professor_id int references professor(id)
	);
create table if not exists professor_phone(
	 id serial  primary key NOT NULL, 
   	 phone int NOT NULL, 
	 professor_id int references professor(id)
);




create table if not exists student( 
    id int primary key NOT NULL, 
	 birth_date varchar(10) NOT NULL,
	image varchar(5) 
	
);
create table if not exists student_name(
	 id serial int primary key NOT NULL, 
	 f_name varchar(10) NOT NULL, 
   	 l_name varchar(10) NOT NULL, 
	 name varchar(30) NOT NULL,
     student_id int references student(id)
);


create table if not exists student_connect(
	 id serial  primary key NOT NULL, 
	 email varchar(40) NOT NULL,
   	 phone int NOT NULL, 
	 student_id int references student(id)
	
);
```
## try to insert on normalized table
``` sql
DELETE FROM professor
WHERE id = 1;

insert into professor(id,salary,Age,birth_date) values (1,1000,20,'kodijfao');
insert into professor_name(professor_id,f_name,l_name,name) values (1,'mohmmed','ahmed','mohmmed ahmed sayed');

insert into professor_links(professor_id,email,linkedin_email) values (1,'mohmmedfathi.123','ahgfddfdmed');

```

