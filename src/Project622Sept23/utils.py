from flask import Flask, request, jsonify, render_template
from flask import flask_mysqldb
import pandas as pd
import pymysql
import numpy as np
from src.Project622Sept23.logger import logging
from src.Project622Sept23.exception import CustomException


# Create the app object
# app = Flask(__name__)
# mysql = MySQL(app)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'mydb'

host = "localhost"
user = "root"
password = "root"
db = "mydb"

def read_sql_data():
    logging.info("Reading data from the database")
    try:
        mydb = pymysql.connect(
            host=host, 
            user=user, 
            password=password, 
            db=db)
        logging.info("Connected to the database", mydb)
        df=pd.read_sql('Select * from students',mydb)
        print(df.head())
        return df
    
    except Exception as ex:
        raise CustomException(ex)
