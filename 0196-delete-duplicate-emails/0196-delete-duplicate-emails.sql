# Write your MySQL query statement below
with dupli as (select id , row_number() over (partition by email order by id) as rnk from Person)

delete from person where id in (select id from dupli where rnk>1)