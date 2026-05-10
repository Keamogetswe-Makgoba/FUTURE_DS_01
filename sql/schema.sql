CREATE DATABASE future_interns_db;

-- After ETL using python , the data was loaded here for EDA

SELECT category, 
SUM(sales) as total_revenue, 
COUNT(*) as transaction_count
FROM sales_data_clean
GROUP BY category
ORDER BY total_revenue DESC
;

SELECT ROUND(AVG(sales), 2) as average_order_value 
FROM sales_data_clean
;

SELECT COUNT(*) 
FROM sales_data_clean
WHERE ship_date < order_date
;

-- now we are going to export for tableau

USE future_interns_db;
SELECT * FROM sales_data_clean
;