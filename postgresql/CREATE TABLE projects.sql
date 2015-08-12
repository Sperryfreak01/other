CREATE TABLE projects_summary
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_number varchar(100),
	project_name varchar(200),
	program varchar(100),
	project_manager_full_name varchar(201),
	project_manager_id varchar(100),
	status varchar(40),
	current_phase varchar(200),
	description varchar(255),
	start_date timestamp with time zone,
	target_end_date timestamp with time zone,
	completion_date timestamp with time zone,
	creation_date timestamp with time zone,
	template varchar(100),
	comments varchar(255),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_schedule
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	phase_guid varchar(25),
	phase_name varchar(200),
	task_guid varchar(25),
	task_name varchar(200),
	assignment_type varchar(40),
	assignee_full_name varchar(201),
	assignee_id varchar(100),
	due_date timestamp with time zone,
	completed_date timestamp with time zone,
	status varchar(40),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_referenced_items
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	project_phase_task_guid varchar(25),
	project_phase_task_name varchar(200),
	reference_type varchar(40),
	item_guid varchar(25),
	item_number varchar(200),
	item_revision varchar(15),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_referenced_changes
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	project_phase_task_guid varchar(25),
	project_phase_task_name varchar(200),
	reference_type varchar(40),
	change_guid varchar(25),
	change_number varchar(20),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_referenced_requests
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	project_phase_task_guid varchar(25),
	project_phase_task_name varchar(200),
	reference_type varchar(40),
	request_guid varchar(25),
	request_number varchar(20),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_referenced_projects
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	project_phase_task_guid varchar(25),
	project_phase_task_name varchar(200),
	reference_type varchar(40),
	reference_project_guid varchar(25),
	reference_project_number varchar(100),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_referenced_quality
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	project_phase_task_guid varchar(25),
	project_phase_task_name varchar(200),
	reference_type varchar(40),
	quality_process_guid varchar(25),
	quality_process_number varchar(100),
	PRIMARY KEY (guid)
);

CREATE TABLE projects_referenced_url
(
	tran varchar(5),
	guid varchar(25) NOT NULL,
	project_guid varchar(25),
	project_number varchar(100),
	project_phase_task_guid varchar(25),
	project_phase_task_name varchar(200),
	reference_type varchar(40),
	url_guid varchar(25),
	url varchar(255),
	url_text varchar(100),
	url_description varchar(200),
	PRIMARY KEY (guid)
);