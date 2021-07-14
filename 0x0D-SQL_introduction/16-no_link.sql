-- that lists all records of the table second_table of the database
SELECT score, name
from second_table
WHERE name RLIKE '^[A-Z]'
ORDER BY score DESC;