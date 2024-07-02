physician_data = """
insert into physician values
('EMP001', 'Dr. Smith', 'Cardiologist', 123456789),
('EMP002', 'Dr. Johnson', 'Pediatrician', 987654321),
('EMP003', 'Dr. Williams', 'Dermatologist', 654987321),
('EMP004', 'Dr. Brown', 'Orthopedic Surgeon', 789123456),
('EMP005', 'Dr. Garcia', 'Neurologist', 321654987),
('EMP006', 'Dr. Martinez', 'Ophthalmologist', 456789123),
('EMP007', 'Dr. Taylor', 'ENT Specialist', 987321654);
"""


department_data = """
insert into department values
('DEP001', 'Cardiology', '001'),
('DEP002', 'Pediatrics', '002'),
('DEP003', 'Dermatology', '003'),
('DEP004', 'Surgery', '004'),
('DEP005', 'Neurology', '005');
"""


patient_data = """
insert into patient values
(111111111, 'John Doe', '123 Main St', '555-1234', 987654, 'Dr. Smith'),
(222222222, 'Jane Smith', '456 Elm St', '555-5678', 876543, 'Dr. Johnson'),
(333333333, 'Michael Johnson', '789 Oak St', '555-9012', 765432, 'Dr. Brown'),
(444444444, 'Emily Davis', '321 Pine St', '555-3456', 654321, 'Dr. Williams'),
(555555555, 'David Wilson', '654 Birch St', '555-7890', 543210, 'Dr. Williams'),
(666666666, 'Sarah Thompson', '987 Cedar St', '555-2345', 432109, 'Dr. Brown'),
(777777777, 'Daniel Martinez', '210 Maple St', '555-6789', 321098, 'Dr. Brown'),
(888888888, 'Jessica Robinson', '543 Walnut St', '555-1234', 210987, 'Dr. Garcia'),
(999999999, 'Andrew Hill', '876 Pineapple St', '555-5678', 109876, 'Dr. Garcia'),
(1010101010, 'Michelle Lee', '109 Orange St', '555-9012', 198765, 'Dr. Garcia'),
(1111111111, 'Christopher King', '321 Cherry St', '555-3456', 987654, 'Dr. Martinez'),
(1212121212, 'Amanda Scott', '543 Peach St', '555-7890', 876543, 'Dr. Martinez'),
(1313131313, 'Kevin Phillips', '765 Plum St', '555-2345', 765432, 'Dr. Taylor'),
(1414141414, 'Elizabeth Baker', '987 Apple St', '555-6789', 654321, 'Dr. Taylor'),
(1515151515, 'Jacob Cooper', '210 Lemon St', '555-1234', 543210, 'Dr. Taylor'),
(1616161616, 'Hannah Reed', '432 Grape St', '555-5678', 432109, 'Dr. Smith'),
(1717171717, 'Matthew Morris', '654 Banana St', '555-9012', 321098, 'Dr. Smith'),
(1818181818, 'Olivia Bell', '876 Mango St', '555-3456', 210987, 'Dr. Johnson'),
(1919191919, 'Ryan Gray', '109 Pear St', '555-7890', 109876, 'Dr. Johnson'),
(2020202020, 'Sophia Foster', '321 Avocado St', '555-2345', 198765, 'Dr. Martinez');
"""


nurse_data = """
insert into nurse values
('EMP008', 'Nurse White', 'RN', True, 154321987),
('EMP009', 'Nurse Black', 'LPN', False, 289456123),
('EMP0010', 'Nurse Wilkinson', 'RN', True, 393849012),
('EMP0011', 'Nurse Terry', 'LPN', True, 438475932),
('EMP0012', 'Nurse Schultz','RN', True, 575839842),
('EMP0013', 'Nurse Acosta','RN', True, 627493854),
('EMP0014', 'Nurse Calhoun','RN',True, 738475648),
('EMP0015', 'Nurse Tanner', 'LPN', True, 834568743),
('EMP0016', 'Nurse Gardner', 'LPN',True, 967849302),
('EMP0017', 'Nurse Evans', 'RN', False, 285943485);
"""


appointment_data = """ 
insert into appointment values
('APP001', 111111111, 'EMP008', 'EMP001', '2024-07-02 09:00', 'Room A'),
('APP002', 222222222, 'EMP008', 'EMP001', '2024-07-03 10:30', 'Room B'),
('APP003', 333333333, 'EMP009', 'EMP001', '2024-07-04 13:45', 'Room C'),
('APP004', 444444444, 'EMP009', 'EMP002', '2024-08-01 10:00', 'Room A'),
('APP005', 555555555, 'EMP0010', 'EMP002', '2024-07-23 10:30', 'Room B'),
('APP006', 666666666, 'EMP0010', 'EMP002', '2024-07-06 14:45', 'Room C'),
('APP007', 777777777, 'EMP0011', 'EMP003', '2024-07-11 15:00', 'Room A'),
('APP008', 888888888, 'EMP0011', 'EMP003', '2024-07-21 11:30', 'Room B'),
('APP009', 999999999, 'EMP0012', 'EMP003', '2024-08-06 11:45', 'Room C'),
('APP0010', 1010101010, 'EMP0012', 'EMP004', '2024-08-01 14:00', 'Room A'),
('APP0011', 1111111111, 'EMP0013', 'EMP004', '2024-06-21 12:30', 'Room B'),
('APP0012', 1212121212, 'EMP0013', 'EMP004', '2024-07-06 09:45', 'Room C'),
('APP0013', 1313131313, 'EMP0014', 'EMP005', '2024-07-31 11:00', 'Room A'),
('APP0014', 1414141414, 'EMP0014','EMP005', '2024-07-11 08:30', 'Room B'),
('APP0015', 1515151515, 'EMP0015', 'EMP005', '2024-06-06 10:45', 'Room C'),
('APP0016', 1616161616, 'EMP0015', 'EMP006', '2025-01-01 11:00', 'Room A'),
('APP0017', 1717171717, 'EMP0016', 'EMP006', '2025-01-01 08:30', 'Room B'),
('APP0018', 1818181818, 'EMP0016', 'EMP006', '2025-01-01 10:45', 'Room C'),
('APP0019', 1919191919, 'EMP0017', 'EMP007', '2025-02-01 12:00', 'Room A'),
('APP0020', 2020202020, 'EMP0017', 'EMP007', '2025-01-02 11:40', 'Room C');
"""

procedures_data = """
insert into procedures values
(101, 'ECG', '100'),
(102, 'X-ray', '150'),
(103, 'Blood Test', '50'),
(104, 'ECG', '100'),
(105, 'X-ray', '150'),
(106, 'Blood Test', '50'),
(107, 'ECG', '100'),
(108, 'X-ray', '150'),
(109, 'Blood Test', '50'),
(1010, 'Blood Test', '50');
"""