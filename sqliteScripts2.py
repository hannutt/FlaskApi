
import os
from flask import Blueprint, redirect, render_template, request, url_for
import sqlite3


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
    tables=[]
   
    folder = request.form.get("srcFolder")
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".db"):
                dbvar=root+"\\"+file
                tables.append(dbvar)
                
    return render_template("index.html",sqliteDatabases=tables)


            
  
