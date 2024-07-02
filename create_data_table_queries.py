physician = """
create table physician(
employee_id varchar(100) unique,
physician_name varchar(100) not null,
position varchar(100) not null,
ssn int not null
);
"""

department = """
create table department(
department_id varchar(100) unique,
name varchar(100) not null,
head int not null
);
"""

patient = """
create table patient(
ssn int unique,
name varchar(100) not null,
address varchar(100) not null,
phone varchar(100) not null,
insurance_id int not null,
pcp varchar(100) not null
);
"""

nurse = """
create table nurse(
employee_id varchar(100) unique,
name varchar(100) not null,
position varchar(100) not null,
registered boolean,
ssn int not null
);
"""

appointment = """
create table appointment(
appointment_id varchar(100) unique,
patient int not null,
prep_nurse varchar(100) not null,
physician varchar(100) not null,
start_dt_time varchar(100) not null,
examination_room varchar(100) not null
);
"""

procedures = """
create table procedures(
code int unique,
name varchar(100) not null,
cost varchar(100) not null
);
"""