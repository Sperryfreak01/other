CREATE TABLE supplier_data.motor_3Xmotion_data
(
	id serial NOT NULL,
	motor_serial_number varchar(50) NOT NULL,
	gear_serial_number varchar(50) NOT NULL,
	cw_0nm_current double precision,
	cw_0nm_rpm double precision,
	ccw_0nm_current double precision,
	ccw_0nm_rpm double precision,
	cw_120nm_current double precision,
	cw_120nm_rpm double precision,
	ccw_120nm_current double precision,
	ccw_120nm_rpm double precision,
	shaft_diameter double precision,
	boss_diameter double precision,
	boss_height double precision,
	PRIMARY KEY (id)
);

CREATE TABLE supplier_data.toenergy_data
(
	id serial NOT NULL,
	name varchar(50) NOT NULL,
	voltage_open_circuit double precision,
	current_short_circuit double precision,
	power_module double precision,
	voltage_module double precision,
	current_module double precision,
	ff double precision,
	n double precision,
	r_sh double precision,
	r_s double precision,
	PRIMARY KEY (id)
)