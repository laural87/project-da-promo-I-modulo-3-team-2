# %%
import pandas as pd
import sys
import os
from ast import literal_eval
import mysql.connector
from dotenv import load_dotenv


# %%

load_dotenv()
passwordsql = os.getenv('password')
usersql = os.getenv('user')
hostsql = os.getenv('host')



def dividimos_csv(datos):

       empleados = datos[['age', 'attrition', 'businesstravel', 'dailyrate', 'department',
       'distancefromhome', 'education', 'gender',
       'hourlyrate',  'joblevel', 'jobrole',
       'maritalstatus','monthlyrate',
       'numcompaniesworked', 'overtime', 'percentsalaryhike',
       'performancerating',  'stockoptionlevel',
       'totalworkingyears', 'trainingtimeslastyear', 'worklifebalance',
       'yearsatcompany', 'yearssincelastpromotion', 'yearswithcurrmanager',
       'datebirth', 'remotework','id_encuesta']]
       empleados.to_csv('Datos/empleados.csv')

       satisfaccion = datos[['environmentsatisfaction', 'jobinvolvement', 'jobsatisfaction', 'relationshipsatisfaction', 'id_encuesta']]
       satisfaccion.to_csv('Datos/satisfaccion.csv')


def create_bdd():
    cnx = mysql.connector.connect(user= usersql, password= passwordsql, host= hostsql)
    mycursor = cnx.cursor()

    try:
        mycursor.execute("CREATE DATABASE abc_brain_drain") # Here, the name of the DB is indicated after the CREATE DATABASE operator.
        print("Base de datos creada con nombre: abc_brain_drain 🆗")
        print('='*80)
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
    finally:
        cnx.commit()
        mycursor.close()
        cnx.close()


# %%

def create_tables():
    cnx = mysql.connector.connect(user= usersql, password= passwordsql, host= hostsql, database='abc_brain_drain')
    mycursor = cnx.cursor()

    # Query list where all tables are created
    queries = [
        """CREATE TABLE empleados (
    id_encuesta INT PRIMARY KEY,
    age INT,
    attrition VARCHAR(100),
    dailyrate FLOAT,
    businesstravel VARCHAR(100),
    department VARCHAR(100),
    distancefromhome INT,
    education INT,
    gender VARCHAR(10),
    hourlyrate FLOAT,
    joblevel INT,
    jobrole VARCHAR(100),
    maritalstatus VARCHAR(50),
    monthlyrate INT,
    numcompaniesworked INT,
    overtime VARCHAR(50),
    percentsalaryhike INT,
    performancerating FLOAT,
    stockoptionlevel INT,
    totalworkingyears FLOAT,
    trainingtimeslastyear INT,
    worklifebalance FLOAT,
    yearsatcompany INT,
    yearssincelastpromotion INT,
    yearswithcurrmanager INT,
    datebirth YEAR,
    remotework VARCHAR(10)
);""",
        """CREATE TABLE satisfaccion (
    id_encuesta INT PRIMARY KEY,
    environmentsatisfaction INT,
    jobinvolvement INT,
    jobsatisfaction INT,
    relationshipsatisfaction INT,
    FOREIGN KEY (id_encuesta) REFERENCES empleados(id_encuesta)
);"""
    ]

    # I have created this list of table names so that I can iterate over it and it will print their names appropriately as it makes them.
    table_names = [
        'empleados',
        'satisfaccion'
    ]

    # The zip is a function that groups lists that have multiple elements into tuples. 
    # This then allows you to iterate through the names in the print.
    for query, table_name in zip(queries, table_names):
        try:
            mycursor.execute(query) 
            print(f"Tabla creada con nombre: {table_name} 🆗")
            print('='*80)
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            print('='*80)

    cnx.commit()
    mycursor.close()
    cnx.close()

# %%

def insert_empleados():
    # Connection
    cnx = mysql.connector.connect(user= usersql, password= passwordsql, host= hostsql, database='abc_brain_drain')

    # Cursor creation
    mycursor = cnx.cursor()

    try: 
        # Read CSV file
        df = pd.read_csv('Datos/empleados.csv') 

        # SQL to insert data. You must indicate the name of the columns in the first parenthesis and in values enter the number of columns with %s
        sql_insert_query = """ INSERT INTO empleados (age, attrition, businesstravel, dailyrate, department,
       distancefromhome, education, gender, hourlyrate, joblevel,
       jobrole, maritalstatus, monthlyrate,
       numcompaniesworked, overtime, percentsalaryhike,
       performancerating, stockoptionlevel, totalworkingyears,
       trainingtimeslastyear, worklifebalance, yearsatcompany,
       yearssincelastpromotion, yearswithcurrmanager, datebirth,
       remotework, id_encuesta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        # Iterate over each row of the DataFrame and insert the data for each column.
        for _, row in df.iterrows():
            mycursor.execute(sql_insert_query, (row['age'], row['attrition'], row['businesstravel'], row['dailyrate'], row['department'],
                    row['distancefromhome'], row['education'], row['gender'], row['hourlyrate'], row['joblevel'],
                    row['jobrole'], row['maritalstatus'], row['monthlyrate'],
                    row['numcompaniesworked'], row['overtime'], row['percentsalaryhike'],
                    row['performancerating'], row['stockoptionlevel'], row['totalworkingyears'],
                    row['trainingtimeslastyear'], row['worklifebalance'], row['yearsatcompany'],
                    row['yearssincelastpromotion'], row['yearswithcurrmanager'], row['datebirth'],
                    row['remotework'], row['id_encuesta'] )) 

        # Confirm changes with commit
        cnx.commit() 
        print(f"{mycursor.rowcount} registro(s) insertado(s)📝")
        

    except mysql.connector.Error as err: 
        print(f"Error al insertar en la base de datos: {err} ❌")
        

    finally: 
        if cnx.is_connected(): 
            mycursor.close() 
            cnx.close() 
            print("Conexión a la base de datos cerrada🔚")
            print('='*80)

def insertsatisfaction():
    # Connection
    cnx = mysql.connector.connect(user= usersql, password= passwordsql, host= hostsql, database='abc_brain_drain')

    # Cursor creation
    mycursor = cnx.cursor()

    try: 
        # Read CSV file
        df = pd.read_csv('Datos/satisfaccion.csv')

        # SQL query to insert data
        sql_insert_query = """ 
        INSERT INTO satisfaccion (environmentsatisfaction, jobinvolvement, jobsatisfaction, relationshipsatisfaction, id_encuesta) 
        VALUES (%s, %s, %s, %s, %s)"""

        # Iterate over each row of the DataFrame and insert the data for each column.
        for index, row in df.iterrows():
            # Convert numpy.int64 to Python int if necessary
            data = (
                int(row['environmentsatisfaction']),
                int(row['jobinvolvement']),
                int(row['jobsatisfaction']),
                int(row['relationshipsatisfaction']),
                int(row['id_encuesta'])
            )
            mycursor.execute(sql_insert_query, data)

        # Confirm changes with commit
        cnx.commit()
        print(f"{mycursor.rowcount} registro(s) insertado(s)📝") 

    except mysql.connector.Error as err: 
        print(f"Error al insertar en la base de datos: {err} ❌") 

    finally: 
        if cnx.is_connected(): 
            mycursor.close() 
            cnx.close() 
            print("Conexión a la base de datos cerrada🔚")

