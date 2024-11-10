
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

