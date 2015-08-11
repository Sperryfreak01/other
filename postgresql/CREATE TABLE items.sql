CREATE TABLE items_summary
(
 trans varchar(5),
 guid varchar(25) NOT NULL,
 category_name varchar(80),
 category_path varchar(255),
 item_number varchar(200),
 revision varchar(15),
 item_name varchar(100),
 lifecycle_phase varchar(20),
 description varchar(255),
 owner_full_name varchar(201),
 prototype_cost money,
 production_cost money,
 procurement_type varchar(1),
 unit_of_measure varchar(100),
 created_date timestamp with time zone,
 creator_full_name varchar(201),
 creator_id varchar(100),
 revision_status varchar(40),
 effective_date timestamp with time zone,
 superseded_date timestamp with time zone,
 specs_modified varchar(1),
 bom_modified varchar(1),
 sourcing_modified varchar(1),
 files_modified varchar(1),
 PRIMARY KEY (guid)
 );

 CREATE TABLE items_custom_attributes
 (
  trans varchar(5),
  guid varchar(25) NOT NULL,
  item_guid varchar(25),
  item_number varchar(200),
  attribute_guid varchar(25),
  attribute_name varchar(100),
  attribute_value varchar(255)
);

CREATE TABLE items_bom
(
 trans varchar(5),
 guid varchar(25) NOT NULL,
 parent_item_guid varchar(25),
 parent_item_number varchar(200),
 parent_item_revision varchar(15),
 child_item_guid varchar(25),
 child_item_number varchar(200),
 child_item_revision varchar(15),
 quantity smallint,
 bom_notes varchar(255),
 reference_designators varchar(255),
 PRIMARY KEY (guid)
);

CREATE TABLE items_bom_substitues
(
 trans varchar(5),
 guid varchar(25) NOT NULL,
 bom_guid varchar(25),
 parent_item_guid varchar(25),
 parent_item_number varchar(200),
 parent_item_revision varchar(15),
 primary_child_item_guid varchar(25),
 primary_child_item_number varchar(200),
 primary_child_item_revision varchar(15),
 substitue_child_item_guid varchar(25),
 substitue_child_item_number varchar(200),
 substitue_child_item_revision varchar(15),
 rank smallint,
 quantit smallint,
 notes varchar(255),
 PRIMARY KEY (guid)
);

CREATE TABLE items_sourcing
(
 trans varchar(5),
 guid varchar(25) NOT NULL,
 item_guid varchar(25),
 item_number varchar(200),
 item_revision varchar(15),
 active_production varchar(1),
 active_prototype varchar(1),
 rank smallint,
 split_percent varchar(10),
 approved varchar(40),
 make_item varchar(1),
 manufacturer_item_guid varchar(25),
 manufacturer_item_supplier_name varchar(200),
 manufacturer_item_number varchar(200),
 supplier_item_guid varchar(25),
 supplier_item_supplier_name varchar(200),
 supplier_item_number varchar(200),
 notes varchar(255),
 vendor_item_conversion_factor smallint
);
 
 