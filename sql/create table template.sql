CREATE TABLE changes_custom_attributes
  (
  "Trans Type" character varying (5),
  "Guid" character varying (25) NOT NULL,
  "Change_Guid" character varying (25) NOT NULL,
  "Change_Number" character varying (25) NOT NULL,
  "Attribute_GUID" character varying (25) NOT NULL,
  "Attribute_Name" character varying (100) NOT NULL,
  "Attribute_Value" character varying (25) NOT NULL,
  CONSTRAINT changes_custom_attributes_pkey PRIMARY KEY ("Guid")
)
WITH (
  OIDS = FALSE
);

CREATE TABLE changes_decision_history
(
  "Trans Type" character varying (5),
  "Change Guid" character varying (25) NOT NULL,
  "Guid" character varying (25) NOT NULL, 
  "Change_Number" character varying (25) NOT NULL,
  "Stage" character varying (25) NOT NULL,
  "Approval_Role" character varying (25),
  "Approval_Rqmt" character varying (25),
  "User_Full_Name" character varying (25) NOT NULL,
  "User_ID" character varying (25) NOT NULL,
  "Proxy_User_Full_Name" character varying (25),
  "Proxy_User_ID" character varying (25),
  "Decision" character varying (25) NOT NULL,
  "Decision_Date" timestamp with time zone,
  "Comments" character varying (250),
  "Stage_Change" character varying (25),
  "Stage_Change_User_Full_Name" character varying (25),
  "Stage_Change_User_ID" character varying (25),
  "Stage_Change_Data" character varying (25),
  "Additional_Reviewer" character varying (5) NOT NULL,
  "Historical" character varying (5) NOT NULL,
  CONSTRAINT changes_decision_history_pkey PRIMARY KEY ("Guid")
)
WITH (
  OIDS=FALSE
);

CREATE TABLE change_items
(
  "Trans Type" character varying(5),
  "Guid" character varying(25) NOT NULL,
  "change_guid" character varying(25),
  "ECO" character varying(25),
  "Item_Guid" character varying(25),
  "End_Item_Guid" character varying(25),
  "Item_Number" character varying(200),
  "Item_Start_Revision" character varying(25),
  "Item_End_Revision" character varying(25),
  CONSTRAINT change_items_pkey PRIMARY KEY ("Guid")
)
WITH (
  OIDS=FALSE
);

CREATE TABLE changes_lifecycle_history
(
  "Trans Type" character varying(5),
  "Change_Guid" character varying(25) NOT NULL,
  "Guid" character varying(25) NOT NULL,
  "Change_Number" character varying(25) NOT NULL,
  "Status" character varying(25) NOT NULL,
  "Status_Date" timestamp with time zone,
  "User_Name" character varying(25) NOT NULL,
  "User_ID" character varying(25) NOT NULL,
  "Comments" character varying(250),
  CONSTRAINT changes_lifecycle_history_pkey PRIMARY KEY ("Guid")
)
WITH (
 OIDS=FALSE
);

CREATE TABLE changes_requests
(
  "Trans Type" character varying(5),
  "Guid" character varying(25),
  "Change_Guid" character varying(25),
  "Change_Number" character varying(25),
  "Request_Guid" character varying(25),
  "Request_Number" character varying(25)
)
WITH (
 OIDS=FALSE
);

CREATE TABLE change_summary
(
  "Trans Type" character varying(5),
  "Guid" character varying(25) NOT NULL,
  "Category_Name" character varying(80),
  "Category_Path" character varying(255),
  "Change_Number" character varying(25) NOT NULL,
  "Title" character varying(200),
  "Description" character varying(255),
  "Routings" character varying(255),
  "Approval_Deadline_Date" timestamp with time zone,
  "Effectivity_Date" timestamp with time zone,
  "Expiration_Date" timestamp with time zone,
  "Lifecycle_Status" character varying(50),
  "Lifecycle_Status_Date" timestamp with time zone,
  "Creator" character varying(201),
  "Creator_Email" character varying(254),
  "Create_Date" timestamp with time zone,
  "Submitter" character varying(201),
  "Submitter_Email" character varying(254),
  "Submitted_Date" timestamp with time zone,
  CONSTRAINT change_summary_pkey PRIMARY KEY ("Guid"),
  CONSTRAINT "change_summary_Change_Number_key" UNIQUE ("Change_Number")
)
WITH (
  OIDS=FALSE
);
