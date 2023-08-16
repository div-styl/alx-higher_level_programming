-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, state.name FROM cities LEFT JOIN state ON state.id = cities.state_id ORDER BY cities.id;