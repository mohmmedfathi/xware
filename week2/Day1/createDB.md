**#create faculty Database Postgresql**

create table if not exists Faculty(
id int primary key NOT NULL,
name varchar(20) NOT NULL
);

create table if not exists Department(
id int primary key NOT NULL,
name varchar(20) NOT NULL,
faculty_id int references faculty(id)
);

create table if not exists subject(
	id int ,
	name varchar(10) NOT NULL,
	code int primary key NOT NULL
);

create table if not exists professor(
	id int primary key NOT NULL,
	department_id int references Department(id),
	faculty_id int references faculty(id),
	f_name varchar(10) NOT NULL,
	l_name varchar(10) NOT NULL,
	image bytea ,
	salary REAL NOT NULL,
	Age int NOT NULL
);

create table if not exists student(
	id int primary key NOT NULL,
	f_name varchar(10) NOT NULL,
	l_name varchar(10) NOT NULL,
	image bytea ,
	f_phone int NOT NULL,
	l_phone int,
	birth_date varchar(20) NOT NULL
);

create table if not exists Address(
	id int primary key NOT NULL,
	government varchar(10) NOT NULL,
	city varchar(10) NOT NULL,
	line1 varchar(10) NOT NULL,
	line2 varchar(10)
);
create table if not exists student_Address(
	id int primary key NOT NULL,
	student_id int references student(id),
	Address_id int references Address(id)
);
	
	
create table if not exists course(
	id int primary key NOT NULL,
	professor_id int references professor(id),
	subject_code int references subject(code),
	duration varchar(20)
);
create table if not exists course_Enrollment(
	id int primary key NOT NULL,
	student_id int references student(id),
	course_id int references course(id)
);
create table if not exists Exams(
	id int primary key NOT NULL,
	course_id int references course(id),
	date varchar(20) NOT NULL,
	duration varchar(20)
);
	
