CREATE TABLE quality_summary
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_number varchar(100),
	quality_process_name varchar(200),
	process_description varchar(255),
	owner_full_name varchar(201),
	owner_ID varchar(100),
	started_date timestamp with time zone,
	current_step_completion_date timestamp with time zone,
	target_date timestamp with time zone,
	completion_date timestamp with time zone, 
	current_step_due_date timestamp with time zone,
	template varchar(200),
	type varchar(100),
	status varchar(100),
	creator_full_name varchar(201),
	creator_ID varchar(100),
	creation_date timestamp with time zone,
	current_phase varchar(200),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_custom_attributes
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	attribute_guid varchar(25),
	attribute_name varchar(100),
	attribute_value varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_details
(
	trans varchar(5),
	quality_process_guid varchar(25),
	guid varchar(25) NOT NULL,
	quality_process_number varchar(100),
	step_name varchar(200),
	assignee_full_name varchar(201),
	assignee_ID varchar(100),
	decision_user_full_name varchar(201),
	decision_user_ID varchar(100),
	due_date timestamp with time zone,
	decision_comment varchar(255),
	step_complete varchar(1),
	completed_date timestamp with time zone,
	PRIMARY KEY (guid)
);

CREATE TABLE quality_affected_items
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	item_guid varchar(25),
	item_number varchar(200),
	item_revision varchar(15),
	notes varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_affected_changes
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	change_guid varchar(25),
	change_number varchar(200),
	notes varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_affected_requests
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	request_guid varchar(25),
	request_number varchar(200),
	notes varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_affected_projects
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	project_guid varchar(25),
	project_number varchar(200),
	notes varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_affected_quality
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	referenced_quality_process_guid varchar(25),
	referenced_quality_process_number varchar(200),
	notes varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_affected_url
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	step_guid varchar(25),
	step_name varchar(200),
	url_guid varchar(25),
	url varchar(255),
	url_text varchar(100),
	url_description varchar(200),
	notes varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE quality_history
(
	trans varchar(5),
	guid varchar(25) NOT NULL,
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	action varchar(255),
	property varchar(255),
	user_full_name varchar(201),
	user_id varchar(100),
	original_value varchar(255),
	new_value varchar(255),
	history_date timestamp with time zone,
	PRIMARY KEY (guid)
);