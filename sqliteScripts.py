from flask import Blueprint, render_template, request
import sqlite3,os
from pathlib import Path, PureWindowsPath

sqliteTables=False
sqliteScripts = Blueprint('sqliteScripts',__name__,static_folder='static',template_folder='templates')


@sqliteScripts.route("/sqlite",methods=['POST','GET'])
def readDBname():
    sqliteDatabases=[]
    for root, dirs, files in os.walk("C:\emptyfol"):
        for file in files:
            if file.endswith(".db"):
             print(os.path.join(root, file))
             dbvar=root+"\\"+file
             sqliteDatabases.append(dbvar)
    return render_template("index.html",sqliteDatabases=sqliteDatabases)

@sqliteScripts.route("/getsqlite",methods=['POST','GET'])
def showSqliteTables():
    dbname=request.form.get('sqliteFile')
     #määritetään tietokantatiedosto, johon yhdistetään
    conn = sqlite3.connect(dbname)
    #sql kysely, joka hakee kaikki taulut valitusta tietokannasta
    sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
    
    '''
    global sqliteTables
    sqliteTables=True
    tables=[]
    replacedTable=[]
    '''
   
# Create a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    for x in cursor:
       print(x)
     
        
    
    conn.close()
    return render_template("index.html")
   
    
    

    
    