"connect to db"
import os
import logging
import pyodbc
import sqlalchemy


pyodbc.pooling = False

conn_string = os.environ["CONN_STRING"]
conn_url = sqlalchemy.engine.URL.create("mssql+pyodbc", query={"odbc_connect":conn_string})




try:
    # conn = pyodbc.connect(conn_string)
    engine  = sqlalchemy.create_engine(conn_url)
except KeyError as e:
    logging.error("Exception Occurred", exc_info=True)
except Exception as e:
    logging.error("An error has occurred while connecting to the database")
else:
    logging.info('Connected to database')
    # cursor = conn.cursor()
    conn = engine.connect()

