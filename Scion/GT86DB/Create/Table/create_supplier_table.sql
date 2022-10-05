/*
--
--	This script creates a new table for suppliers
--
*/

CREATE TABLE supplier (
	supplier_id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
	supplier_name VARCHAR(255) NOT NULL,
	country_id INT NOT NULL,
	dta000 DATETIME NOT NULL,
	dtb000 DATETIME NULL,
	dtc000 DATETIME NULL
);