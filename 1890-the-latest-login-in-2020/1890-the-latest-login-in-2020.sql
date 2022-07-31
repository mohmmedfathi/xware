# Write your MySQL query statement below
select user_id,MAX(time_stamp) AS last_stamp 
FROM Logins
where time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
group by user_id