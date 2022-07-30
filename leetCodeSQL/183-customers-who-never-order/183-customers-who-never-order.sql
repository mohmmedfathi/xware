SELECT name as Customers
FROM Customers
LEFT join Orders
on 
Orders.customerId = Customers.id
where 
Orders.customerId IS NULL