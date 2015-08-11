-- alter tables after csv load to keep relationships

ALTER TABLE changes_custom_attributes ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_lifecycle_history ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_decision_history ADD FOREIGN Key (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_items ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);
ALTER TABLE changes_requests ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (guid);

ALTER TABLE items_custom_attributes ADD FOREIGN KEY (item_guid)REFERENCES items_summary (guid);
ALTER TABLE items_bom ADD FOREIGN KEY (parent_item_guid) REFERENCES items_summary (guid);
ALTER TABLE items_bom ADD FOREIGN KEY (child_item_guid) REFERENCES items_summary (guid);
ALTER TABLE items_sourcing ADD FOREIGN KEY (item_guid) REFERENCES items_summary (guid);

ALTER TABLE projects_schedule ADD FOREIGN KEY (project_guid) REFERENCES projects_summary (guid);
ALTER TABLE projects_referenced_items ADD FOREIGN KEY (project_guid) REFERENCES projects_summary (guid);
ALTER TABLE projects_referenced_items ADD FOREIGN KEY (project_phase_task_guid) REFERENCES projects_schedule (phase_guid);
