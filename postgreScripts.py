import psycopg2
from flask import Blueprint, render_template, request

postgreScripts = Blueprint('postgreScripts',__name__,static_folder='static',template_folder='templates')

def connection():

    conn = psycopg2.connect(database="stuffdb",
                            
                            host="localhost",
                            user="postgres",
                            password="SkaneBorg12!",
                            port=5433)
    return conn

@postgreScripts.route("/postgresql",methods=['POST','GET'])
def readPostgre():
    databases=[]
    conn=connection()
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database;")
    for i in cursor.fetchall():
        print(i)
        databases.append(i)
   

    return render_template("postgresql.html",databases=databases)

