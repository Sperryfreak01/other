-- alter tables after csv load to keep relationships

ALTER TABLE changes_custom_attributes ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_lifecycle_history ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_decision_history ADD FOREIGN Key (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_items ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_items ADD FOREIGN KEY (Item_Guid) REFERENCES items_summary (guid);
ALTER TABLE changes_items ADD FOREIGN KEY (End_Item_Guid) REFERENCES items_summary (guid);
ALTER TABLE changes_requests ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_requests ADD FOREIGN KEY (request_guid) REFERENCES requests_summary (guid);

ALTER TABLE items_custom_attributes ADD FOREIGN KEY (item_guid) REFERENCES items_summary (guid);
ALTER TABLE items_bom ADD FOREIGN KEY (parent_item_guid) REFERENCES items_summary (guid);
ALTER TABLE items_bom ADD FOREIGN KEY (child_item_guid) REFERENCES items_summary (guid);
ALTER TABLE items_sourcing ADD FOREIGN KEY (item_guid) REFERENCES items_summary (guid);

-- ALTER TABLE projects_schedule ADD FOREIGN KEY (project_guid) REFERENCES projects_summary (guid);(
-- -- missing two references here in table "projects_schedule" that reference its own fields, not sure how to handle them
-- ALTER TABLE projects_referenced_items ADD FOREIGN KEY (project_guid) REFERENCES projects_summary (guid);
-- ALTER TABLE projects_referenced_items ADD FOREIGN KEY (project_phase_task_guid) REFERENCES projects_schedule (phase_guid);
-- ALTER TABLE projects_referenced_changes ADD FOREIGN KEY (project_guid) REFERENCES projects_summary (guid);
-- ALTER TABLE projects_referenced_changes ADD FOREIGN KEY (project_phase_task_guid) REFERENCES projects_schedule (phase_guid);

ALTER TABLE quality_custom_attributes ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_details ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_items ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_items ADD FOREIGN KEY (step_guid) REFERENCES quality_details (guid);
ALTER TABLE quality_affected_changes ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_changes ADD FOREIGN KEY (step_guid) REFERENCES quality_details (guid);
ALTER TABLE quality_affected_changes ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE quality_affected_requests ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_requests ADD FOREIGN KEY (step_guid) REFERENCES quality_details (guid);
ALTER TABLE quality_affected_requests ADD FOREIGN KEY (request_guid) REFERENCES requests_summary (guid);
ALTER TABLE quality_affected_projects ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_projects ADD FOREIGN KEY (step_guid) REFERENCES quality_details (guid);
ALTER TABLE quality_affected_projects ADD FOREIGN KEY (project_guid) REFERENCES projects_schedule (guid);
ALTER TABLE quality_affected_quality ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_quality ADD FOREIGN KEY (step_guid) REFERENCES quality_details (guid);
ALTER TABLE quality_affected_quality ADD FOREIGN KEY (referenced_quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_url ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);
ALTER TABLE quality_affected_url ADD FOREIGN KEY (step_guid) REFERENCES quality_details (guid);
ALTER TABLE quality_history ADD FOREIGN KEY (quality_process_guid) REFERENCES quality_summary (guid);

ALTER TABLE requests_custom_attributes ADD FOREIGN KEY (request_guid) REFERENCES requests_summary (guid);
ALTER TABLE requests_lifecycle_history ADD FOREIGN KEY (request_guid) REFERENCES requests_summary (guid);
ALTER TABLE requests_items ADD FOREIGN KEY (request_guid) REFERENCES requests_summary (guid);
ALTER TABLE requests_items ADD FOREIGN KEY (item_guid) REFERENCES items_summary (guid);

ALTER TABLE suppliers_item_summary ADD FOREIGN KEY (supplier_guid) REFERENCES suppliers_summary (guid);
ALTER TABLE suppliers_custom_attributes ADD FOREIGN KEY (supplier_item_guid) REFERENCES suppliers_item_summary (guid);