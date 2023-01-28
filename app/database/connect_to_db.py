"connect to db"
import os
import logging
import pyodbc

conn_string = os.environ["CONN_STRING"]

try:
    conn = pyodbc.connect(conn_string)
except KeyError as e:
    logging.error("Exception Occurred", exc_info=True)
except Exception as e:
    logging.error("An error has occurred while connecting to the database")
else:
    logging.info('Connected to database')
    cursor = conn.cursor()
