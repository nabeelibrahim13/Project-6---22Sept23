import sys
from flask import Flask, request, jsonify, render_template

from src.Project622Sept23.logger import logging


@app.route('/')
def form():
    return render_template('user.html')

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
    
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         email = request.form['email']
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO users VALUES(%s,%s,%s)''',(name,age,email))
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
#     return render_template("form.html")

@app.route("/users")
def getusers():
    cur = mysql.connection.cursor()
    users= cur.execute("SELECT * from users")
    if users > 0:
        userDetails = cur.fetchall()
    return render_template('users.html',all_users=userDetails)






if __name__ == "__main__":
    logging.info("The execution has started")
    logging.warning("warnig")
    logging.error("error")
    logging.critical("critical")
    logging.debug("debug")




