# exercises

## Create a new transaction


```sql
begin;
```

### Insert a new record into the Professor table

```sql
insert into professor (id,department_id,faculty_id,f_name,l_name,salary,age) values (1,1,1,'mohmmed','ahmed',2193,40);

```
### Insert a new record into the Student table

```sql
insert into student (id,f_name,l_name,f_phone,birth_date,age) values (1,'mohmmed','fathi',01111442600,'23-43-2123','23');

```

### Select all the Professors and students
```sql
select * from student;
select * from professor;
```

###  Open another session and select all the Professors and students
	What is the difference? 
```sql
1 - ctrl + shift + t 
2 -  to enter DB : sudo -u postgres psql
**" the insert is not added yet because the transaction not commited "**

```

### Return to the first session and delete the Professors with the salary greater than 20000
```sql
delete from professor where salary > 20000
```

### Open another session and select all the Professors and students. What is the difference?
```sql
**"the professor isn't deleted because the delete is not done yet because the transaction not commited"**
```


### Return to the first session and rollback the transaction
```sql
ROLLBACK;
```

### Open another session and select all the Professors and students. What is the difference?
```sql
**"the professor and students is same ,(no insert and delete is done) because we rollback the transaction.**
```
### Return to the first session Start a new transaction
```sql
begin;
```

### Insert a new record into the Professor table
```sql
insert into professor (id,department_id,faculty_id,f_name,l_name,salary,age) values (2,2,2,'youssed','ahmed',4000,50);
```

### Insert a new record into the Student table
```sql
insert into student (id,f_name,l_name,f_phone,birth_date,age) values (2,'ahmed','mohmmed',01111442600,'23-43-2123','23');
```

### Commit the transaction
```sql
commit
```

### Open another session and select all the Professors and students. What is the difference?
```sql
"the insert is  added  because the transaction is commited"
```

###  start a new transaction
```sql
 begin;
```
###  Insert a new record into the Professor table with a duplicated id. What happens?
```sql
 ERROR:  duplicate key value violates unique constraint "department_pkey"
```

### Try to insert a new record into the Student table with a duplicated id. What happens?
```sql
ERROR:  duplicate key value violates unique constraint "student_pkey"
```

### Try to commit the transaction. What happens?
```sql
ROLLBACK -- > reason : the insert is not done (because we Insert the record with a duplicated id.)
```

### Try to rollback the transaction. What happens?
```sql
there is no transaction is running and output :
WARNING:  there is no transaction in progress
ROLLBACK
```

### Try to insert a new record into the Student table with a duplicated id. What happens?
```sql
ERROR:  duplicate key value violates unique constraint "student_pkey"
```
