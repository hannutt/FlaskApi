
import os
from flask import Blueprint, redirect, render_template, request, url_for
import sqlite3
import pandas as pd


sqliteScripts2 = Blueprint('sqliteScripts2',__name__,static_folder='static',template_folder='templates')

@sqliteScripts2.route("/newcolumn/<dbname>/<table>",methods=['POST','GET'])
def createColumn(dbname,table):
    columnname=request.form.get("columnName")
    conn=sqlite3.connect(dbname)
    cursor=conn.cursor()
    cursor.execute(f"ALTER TABLE {table} ADD COLUMN {columnname}")

    return render_template("sqlite.html")

@sqliteScripts2.route("/tablecols/<dbname>/<table>",methods=['POST','GET'])
def createTableCols(dbname,table):
    conn=sqlite3.connect(dbname)
    cursor = conn.cursor()
    inputs=request.form.get("columns")
    return render_template("sqlite.html")

@sqliteScripts2.route("/searchFrom",methods=['POST','GET'])
def searchFromFolder():
    
    #saman nimistä listaa käytetään myös sqliteScripts readdbname funktiossa, jonka jälkeen
    #löydetyt tietodston käydään index.htmlssä for silmukalla läpi, kun myös käytetään
    #samaa listaa, saadaan myös tämän tulokset näkymään samassa table.elementissä
    restriction=request.form.get("numberofsearch")
    if restriction=="":
        restriction=1
    restrictInt=int(restriction)
    tables=[]
    dbSizes=[]
    folder = request.form.get("srcFolder")
    folder=folder.replace(" ","")
    
    i=0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".db"):
                dbvar=root+"\\"+file
                i+=1
                
                dbSize=os.stat(dbvar)
           
             #db-tiedostojen koon muunto megatavuiksi
                sizeInMb=dbSize.st_size/(1024*1024)
                dbSizes.append(sizeInMb)
             #pyöritys muotoon 0,00
                roundedSize=round(sizeInMb,2)
                sizeInMbStr = str(roundedSize)
                finalDBvar=dbvar+' | Size: '+sizeInMbStr + ' MB'
                tables.append(finalDBvar)
                if i == restrictInt:

                    return render_template("index.html",sqliteDatabases=tables)

@sqliteScripts2.route("/exportcsv",methods=['POST','GET'])
def exportCsv():
     database=request.form.get('dbname')
     table=request.form.get('tablename')
     conn=sqlite3.connect(database)
     df = pd.read_sql(f'SELECT * from {table}', conn)
     df.to_csv('data.csv', index = False)
     return render_template("sqlite.html")

  
