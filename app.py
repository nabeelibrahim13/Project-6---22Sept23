import sys
from flask import Flask, request, jsonify, render_template
import pandas as pd
from src.Project622Sept23.logger import logging
from src.Project622Sept23.utils import read_sql_data


# app = Flask(__name__)
# @app.route("/")
# def home():    
#     df = read_sql_data()
#     print(df.head())
    #return render_template('users.html',all_users=df)

df = read_sql_data()

#print(df.head())

# if __name__ == "__main__":
#     logging.info("app.py is running")
    
#     app.run(debug=True)




