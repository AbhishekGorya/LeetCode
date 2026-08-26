/* Write your MySQL query statement below */
SELECT 
    visited_on, 
    SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    ROUND(SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) / 7.0, 2) AS average_amount
FROM Customer 
GROUP BY visited_on 
ORDER BY visited_on 
LIMIT 18446744073709551615 OFFSET 6;
