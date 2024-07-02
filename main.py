
import mysql.connector
from mysql.connector import Error

import create_data_base as cdb

import create_data_table_queries as cdtq

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


conntection = createServerConnection("localhost","root","student","cape_local_medical_center")
