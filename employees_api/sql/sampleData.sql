
--
-- Create model Department
--
CREATE TABLE IF NOT EXISTS 'employees_department' (
	'DepartmentId' integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	'Name' varchar(100) NOT NULL, 
	'CreatedOn' datetime NOT NULL
);
--
-- Create model Designation
--
CREATE TABLE IF NOT EXISTS  'employees_designation' (
	'DesignationId' integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	'Name' varchar(100) NOT NULL, 
	'CreatedOn' datetime NOT NULL
);
--
-- Create model Employee
--
CREATE TABLE IF NOT EXISTS 'employees_employee' (
	'EmployeeId' integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	'FirstName' varchar(100) NOT NULL, 
	'MiddleName' varchar(100) NOT NULL, 
	'LastName' varchar(100) NOT NULL, 
	'EmployeeCode' varchar(30) NOT NULL, 
	'CreatedOn' datetime NOT NULL, 
	'ModifiedOn' datetime NOT NULL, 
	'DepartmentId' integer NOT NULL REFERENCES 'employees_department' ('DepartmentId') DEFERRABLE INITIALLY DEFERRED, 
	'DesignationId' integer NOT NULL REFERENCES 'employees_designation' ('DesignationId') DEFERRABLE INITIALLY DEFERRED
);
--
-- Create model EmployeeSlots
--
CREATE TABLE IF NOT EXISTS 'employees_employeeslots' (
	'EmployeeSlotId' integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	'MeetingDate' date NULL, 
	'MeetingFromTime' time NULL, 
	'MeetingToTime' time NULL, 
	'message' text NULL, 
	'CreatedOn' datetime NOT NULL, 
	'EmployeeId1' integer NULL REFERENCES 'employees_employee' ('EmployeeId') DEFERRABLE INITIALLY DEFERRED, 
	'EmployeeId2' integer NULL REFERENCES 'employees_employee' ('EmployeeId') DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX IF NOT EXISTS 'employees_employee_DepartmentId_6045d2ce' ON 'employees_employee' ('DepartmentId');
CREATE INDEX IF NOT EXISTS 'employees_employee_DesignationId_b7324c9e' ON 'employees_employee' ('DesignationId');
CREATE INDEX IF NOT EXISTS 'employees_employeeslots_EmployeeId1_3f2564a5' ON 'employees_employeeslots' ('EmployeeId1');
CREATE INDEX IF NOT EXISTS 'employees_employeeslots_EmployeeId2_11297403' ON 'employees_employeeslots' ('EmployeeId2');


INSERT INTO 'employees_department' VALUES (
	NULL,
	'Research',
	'2014-05-09'
);
INSERT INTO 'employees_department'  VALUES (
	NULL,
	'Marketing',
	'2014-05-09'
);
INSERT INTO 'employees_department' VALUES (
	NULL,
	'Accounting',
	'2014-05-09'
);


INSERT INTO 'employees_designation'  VALUES (
	NULL,
	'Manager',
	'2014-05-09'
);

INSERT INTO 'employees_designation' VALUES (
	NULL,
	'Supervisor',
	'2014-05-09'
);


INSERT INTO 'employees_employee' VALUES(
		 NULL,
		 'Jon',
		 'A',
		 'Kramer',
		 '500',
		 '2014-05-09',
		 '2014-05-09',
		(SELECT DepartmentId from 'employees_department' WHERE Name='Research'),
		(SELECT DesignationId from 'employees_designation' WHERE Name='Manager')
);

INSERT INTO 'employees_employee' VALUES(
		 NULL,
		 'Taimoor',
		 'Khokhar',
		 'Khokhar',
		 '501',
		 '2014-05-09',
		 '2014-05-09',
		(SELECT DepartmentId from 'employees_department' WHERE Name='Marketing'),
		(SELECT DesignationId from 'employees_designation' WHERE Name='Supervisor')
);
