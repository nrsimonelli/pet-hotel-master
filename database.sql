CREATE TABLE pet (
	id SERIAL PRIMARY KEY,
	owner_id INT REFERENCES owner,
	pet VARCHAR(50),
	breed VARCHAR(50),
	color VARCHAR(50),
	check_in BOOLEAN DEFAULT false
);

CREATE TABLE owner (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

SELECT * FROM owner;

SELECT * FROM pet;

SELECT * FROM owner 
JOIN pet ON owner.id = pet.owner_id
ORDER BY pet.id;

INSERT INTO owner (name) VALUES
	('bob'),
	('doug');

INSERT INTO pet (owner_id, pet, breed, color) VALUES 
	(1, 'birdo', 'parakeet', 'blue'),
	(1, 'snake', 'cobra', 'green'),
	(2, 'doug', 'eel', 'grey');