from flask import Blueprint, render_template
import mysql.connector

mysqlScripts = Blueprint('mysqlScripts',__name__,static_folder='static',template_folder='templates')


#@mysqlScripts.route("/",methods=['POST','GET'])
def showSQLDataBases():
    sqlDataBases = []

    mydb = mysql.connector.connect(
       
        host="localhost",
        user="root",
        password="Root512!",
)
    cursor = mydb.cursor()
    databases = ("show databases")
    cursor.execute(databases)
    for (databases) in cursor:
         print (databases[0])
         sqlDataBases.append(databases[0])

    return render_template('index.html',sqlDataBases=sqlDataBases)
