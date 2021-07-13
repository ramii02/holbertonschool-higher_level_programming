-- lists all cities contained in the database hbtn_0d_usa
-- each record should display cities id name and states name
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states on cities.state_id=states.id;
