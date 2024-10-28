from flask import Blueprint, render_template, request
import sqlite3,os
from pathlib import Path, PureWindowsPath

sqliteTables=False
runsql=False
sqliteScripts = Blueprint('sqliteScripts',__name__,static_folder='static',template_folder='templates')


@sqliteScripts.route("/sqlite",methods=['POST','GET'])
def readDBname():
    runsql=True
    i=0
    #kun sqliteTables on true, näytetään filepath input index.htmlssä
    sqliteTables=True
    #käyttäjän syöttämä määrä, montako db tiedostoa etsitään
    restriction = request.form.get('restriction')
    #muunto int-tietotyyppiin eli luvuksi.
    restrictionInt = int(restriction)
    sqliteDatabases=[]
    #etsitään db-päätteisiä tiedostoja kaikkialta c-levyltä.
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if file.endswith(".db"):
             i=i+1
             print(os.path.join(root, file))
             dbvar=root+"\\"+file
             #db-tiedostojen koot megatavuina
             dbSize=os.stat(dbvar)
           
             #db-tiedostojen koon muunto megatavuiksi
             sizeInMb=dbSize.st_size/(1024*1024)
             #pyöritys muotoon 0,00
             roundedSize=round(sizeInMb,2)
             sizeInMbStr = str(roundedSize)
             finalDBvar=dbvar+' | Size: '+sizeInMbStr + ' MB'
             sqliteDatabases.append(finalDBvar)
             #sqliteDatabases.append(sizeInMb)
             #rajoitetaan db päätteiset tiedostot käyttäjän syöttämään määrään
             #i pitää kirjaa siitä, montako db päätteistä tiedostoa on löydetty.
             if i == restrictionInt:
                return render_template("index.html",sqliteDatabases=sqliteDatabases,sqliteTables=sqliteTables,runsql=runsql)

@sqliteScripts.route("/getsqlite",methods=['POST','GET'])
def showSqliteTables():
    sqliteTables=True
    
    sqlTables=[]
    global dbname
    dbname=request.form.get('sqliteFile')
     #määritetään tietokantatiedosto, johon yhdistetään
    conn = sqlite3.connect(dbname)
    #sql kysely, joka hakee kaikki taulut valitusta tietokannasta
    sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
   
# Create a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    for x in cursor:
       print(x)
       sqlTables.append(x)
    conn.close()
    return render_template("index.html",sqlTables=sqlTables,sqliteTables=sqliteTables)

@sqliteScripts.route("/opentable",methods=['POST','GET'])
def runsqlite():
   
   data=[]
   global dbname
   table=request.form.get("selectedTable")
   conn = sqlite3.connect(dbname)
   #f-stringin avulla voidaan antaan taulun nimi parametrina.
   cursor = conn.execute(f"SELECT * FROM {table}")
   for row in cursor:
      data.append(row)
   return render_template("sqlite.html",data=data)


   
    
    

    
    