-- Product App - DB Queries


--CREATE DATABASE product_db_v2b;

--SHOW CREATE TABLE product_details;
--SELECT generate_create_table_statement('product_details');


SELECT *
FROM information_schema.columns
WHERE table_schema = 'YOURSCHEMA' AND table_name = 'countries'
ORDER BY ordinal_position;



-- Select from Table with Limit 20
SELECT * FROM product_details ORDER BY id LIMIT 20;




























































































