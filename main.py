
import mysql.connector
from mysql.connector import Error

import create_data_base as cdb

import create_data_table_queries as cdtq

import read_data_table_queries as rdtq

import update_data_tables_queries as udtq

import populate_data_tables_queries as pdtq
def createServerConnection(host_name,user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database Connection Successful!")
    except Error as err:
        print(f"Error:{err}")
    return connection

def create_database(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        #cursor is created by the connection to mySQL. Think of the cursor as the blinking box ready to be used by the user. We are telling the cursor to
        #execute the query.
        print("Database created successfully!")
    except Error as err:
        print(f"Error: {err}")

def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful!")
    except Error as err:
        print(f"Error: {err}")

def read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

conntection = createServerConnection("localhost","root","student","cape_local_medical_center")

execute_query(conntection,udtq.update_patient)
print("Information for Patient Data Table:")
patientDataTable = read_query(conntection,rdtq.display_patient_information)
for patientInformation in patientDataTable:
    print(patientInformation)
print()

execute_query(conntection,udtq.update_procedures)
print("Information for Procedures Data Table:")
proceduresDataTable = read_query(conntection, rdtq.display_procedures_information)
for proceduresInformation in proceduresDataTable:
    print(proceduresInformation)
print()

execute_query(conntection,udtq.update_appointment)
appointmentDataTable = print("Information for Appointment Data Table")
appointmentDataTable = read_query(conntection,rdtq.display_appointment_information)
for appointmentInformation in appointmentDataTable:
    print(appointmentInformation)
print()