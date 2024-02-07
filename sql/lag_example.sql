Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

 

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+

######################

/^ using lag function^/

select *
from Weather 
where lag(temperature) over 
	(partition by recordDate order by recordDate) < temperature
	
/* if id sorted from late to current */	
select b.id 
from Weather a
left join Weather b
on a.id + 1 = b.id 
where a.temperature < b.temperature

/* better */
select b.id 
from Weather a
left join Weather b
on b.recordDate = DATE_ADD(a.recordDate INTERVAL 1 DAY)   
where a.temperature < b.temperature
	
	
	
	
	

