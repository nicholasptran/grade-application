"connect to db"
import os
import logging
import pyodbc

conn_string = os.environ["CONN_STRING"]

try:
    conn = pyodbc.connect(conn_string)
except KeyError as e:
    logging.error("Exception Occurred", exc_info = True)
else:
    logging.info('Connected to database')
    cursor = conn.cursor()
