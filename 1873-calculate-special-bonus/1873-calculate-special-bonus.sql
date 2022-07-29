SELECT employee_id ,

CASE 
 WHEN ((employee_id % 2) =1  AND name NOT LIKE 'M%') THEN salary
 ELSE  0
 END AS bonus 
 FROM Employees
 ORDER BY employee_id
 
 -- another sol by if 
 SELECT employee_id,
if(employee_id % 2 AND name NOT LIKE 'M%', salary, 0) AS bonus
from Employees 
ORDER BY employee_id;
