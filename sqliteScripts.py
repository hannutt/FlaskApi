from flask import Blueprint, render_template, request
import sqlite3,os
sqliteTables=False
sqliteScripts = Blueprint('sqliteScripts',__name__,static_folder='static',template_folder='templates')


@sqliteScripts.route("/sqlite",methods=['POST','GET'])
def readDBname():
    global sqliteTables
    sqliteTables=True
    tables=[]
    dbname=request.form.get("path")
  
    
   
    conn = sqlite3.connect(dbname)
    sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
   
# Create a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute(sql_query)
    for x in cursor:
        tables.append(x)
    
    conn.close() 
    return render_template("index.html",tables=tables,sqliteTables=sqliteTables)

    
    