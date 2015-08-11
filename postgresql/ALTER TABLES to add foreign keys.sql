-- alter tables after csv load to keep relationships

ALTER TABLE changes_custom_attributes ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (Guid);
ALTER TABLE changes_lifecycle_history ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (Guid);
ALTER TABLE changes_decision_history ADD FOREIGN Key (change_guid) REFERENCES changes_summary (Guid);
ALTER TABLE changes_items ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (Guid);
ALTER TABLE changes_requests ADD FOREIGN KEY (change_guid) REFERENCES changes_summary (Guid);