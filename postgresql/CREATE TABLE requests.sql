CREATE TABLE requests_summary
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	problem varchar(500),
	requested_action varchar(500),
	category varchar(80),
	request_number varchar(20),
	request_title varchar(100),
	request_code varchar(25),
	deferral_code varchar(25),
	resolution_code varchar(25),
	lifecycle_status varchar(50),
	lifecycle_status_date timestamp with time zone,
	supplier varchar(200),
	creator_full_name varchar(201),
	creator_ID varchar(100),
	creation_date timestamp with time zone,
	submitter_full_name varchar(201),
	submitter_ID varchar(100),
	submit_date timestamp with time zone,
	PRIMARY KEY (guid)
);

CREATE TABLE requests_custom_attributes
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	request_guid varchar(25),
	request_number varchar(20),
	attribute_guid varchar(25),
	attribute_name varchar(100),
	attribute_value varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE requests_lifecycle_history
(
	trans varchar(5),
	request_guid varchar(25) NOT NULL,
	guid varchar(25),
	request_number varchar(20),
	status varchar(50),
	status_date timestamp with time zone,
	user_full_name varchar(201),
	user_ID varchar(100),
	comments varchar(255)
);

CREATE TABLE requests_items
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	request_guid varchar(25),
	request_number varchar(20),
	item_guid varchar(25),
	item_number varchar(200),
	item_revision varchar(15),
	notes varchar(255),
	PRIMARY KEY (guid)
);