CREATE TABLE suppliers_summary
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	company_name varchar(200),
	supplier_ID varchar(50),
	account_number varchar(40),
	description varchar(255),
	website varchar(200),
	primary_contact varchar(201),
	contact_phone_number varchar(30),
	contact_email varchar(100),
	approval_status varchar(40),
	created_date timestamp with time zone,
	creator_full_name varchar(201),
	creator_ID varchar(100),
	PRIMARY KEY (guid)
);

CREATE TABLE suppliers_item_summary
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	supplier_item_number varchar(200),
	supplier_name varchar(200),
	supplier_guid varchar(25),
	item_type varchar(40),
	description varchar(255),
	procurement_type varchar(1),
	unit_of_measure varchar(100),
	created_date timestamp with time zone,
	creator_full_name varchar(201),
	creator_ID varchar(100),
	PRIMARY KEY (guid)
);

CREATE TABLE suppliers_custom_attributes
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	supplier_item_guid varchar(25),
	supplier_item_supplier_name varchar(200),
	supplier_item_number varchar(200),
	attribute_guid varchar(25),
	attribute_name varchar(100),
	attribute_value varchar(255),
	PRIMARY KEY (guid)
);