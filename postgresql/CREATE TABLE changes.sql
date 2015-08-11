CREATE TABLE changes_summary
(
  Trans varchar(5),
  Guid varchar(25) NOT NULL,
  Category_Name varchar(80),
  Category_Path varchar(255),
  Change_Number varchar(25) NOT NULL,
  Title varchar(200),
  Description varchar(255),
  Routings varchar(255),
  Approval_Deadline_Date timestamp with time zone,
  Effectivity_Date timestamp with time zone,
  Expiration_Date timestamp with time zone,
  Lifecycle_Status varchar(50),
  Lifecycle_Status_Date timestamp with time zone,
  Creator varchar(201),
  Creator_Email varchar(254),
  Create_Date timestamp with time zone,
  Submitter varchar(201),
  Submitter_Email varchar(254),
  Submitted_Date timestamp with time zone,
  PRIMARY KEY (Guid),
  UNIQUE (Change_Number)
);

CREATE TABLE changes_custom_attributes
  (
  Trans varchar (5),
  Guid varchar (25) NOT NULL,
  Change_Guid varchar (25) NOT NULL,
  Change_Number varchar (25) NOT NULL,
  Attribute_GUID varchar (25) NOT NULL,
  Attribute_Name varchar (100) NOT NULL,
  Attribute_Value varchar (255) NOT NULL,
  PRIMARY KEY (Guid)
);

CREATE TABLE changes_lifecycle_history
(
  Trans varchar(5),
  Change_Guid varchar(25) NOT NULL,
  Guid varchar(25) NOT NULL,
  Change_Number varchar(25) NOT NULL,
  Status varchar(50) NOT NULL,
  Status_Date timestamp with time zone,
  User_Name varchar(201) NOT NULL,
  User_ID varchar(100) NOT NULL,
  Comments varchar(255),
  PRIMARY KEY (Guid)
);

CREATE TABLE changes_decision_history
(
  Trans varchar (5),
  Change_Guid varchar (25) NOT NULL,
  Guid varchar (25) NOT NULL, 
  Change_Number varchar (25) NOT NULL,
  Stage smallint NOT NULL,
  Stage_Status varchar(40) NOT NULL,
  Approval_Role varchar (50),
  Approval_Rqmt varchar (40),
  User_Full_Name varchar (201) NOT NULL,
  User_ID varchar (100) NOT NULL,
  Proxy_User_Full_Name varchar (201),
  Proxy_User_ID varchar (100),
  Decision varchar (40) NOT NULL,
  Decision_Date timestamp with time zone,
  Comments varchar (255),
  Stage_Change varchar (50),
  Stage_Change_User_Full_Name varchar (201),
  Stage_Change_User_ID varchar (100),
  Stage_Change_Date timestamp with time zone,
  Additional_Reviewer varchar (1) NOT NULL,
  Historical varchar (1) NOT NULL
);

CREATE TABLE changes_items
(
  Trans varchar(5),
  Guid varchar(25) NOT NULL,
  Change_Guid varchar(25),
  ECO varchar(25),
  Item_Guid varchar(25),
  End_Item_Guid varchar(25),
  Item_Number varchar(200),
  Item_Start_Revision varchar(25),
  Item_End_Revision varchar(25),
  PRIMARY KEY (Guid)
);

CREATE TABLE changes_requests
(
  Trans varchar(5),
  Guid varchar(25),
  Change_Guid varchar(25),
  Change_Number varchar(25),
  Request_Guid varchar(25),
  Request_Number varchar(25),
  PRIMARY KEY (Guid)
);
