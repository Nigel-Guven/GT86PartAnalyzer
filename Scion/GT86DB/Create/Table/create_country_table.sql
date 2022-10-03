/*
--
--	This script creates a new table for countries
--
*/

CREATE TABLE countries (
	country_id		INT IDENTITY(1,1) PRIMARY KEY PRIMARY KEY,
	country_name	CHAR(100) NOT NULL UNIQUE,
	country_iso		CHAR(2) NOT NULL
);