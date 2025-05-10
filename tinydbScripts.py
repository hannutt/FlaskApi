
import os

from flask import Blueprint, redirect, render_template, request, url_for
from tinydb import TinyDB, Query
from tinydb.table import Document
from variables import Variables
from localStoragePy import localStoragePy

var=Variables()

tinyDB = Blueprint('tinyDB',__name__,static_folder='static',template_folder='templates')

@tinyDB.route("/openPage",methods=['POST','GET'])
def openTinyDBPage():
     
     jsonfiles=[]
     currentdirectory = os.getcwd()
     ext=".json"
     for files in os.listdir(currentdirectory):
        if files.endswith(ext):
            jsonfiles.append(currentdirectory+"\\"+files)
     return render_template("tinydb.html",jsonfiles=jsonfiles)  

@tinyDB.route("/createfile",methods=['POST','GET'])
def createFile():
    fname=request.form.get('fileName')
    db=TinyDB(fname)
    return render_template("tinydb.html")


@tinyDB.route("/savetodb",methods=['POST','GET'])
def saveToDb():
    #jos painettu painiketta jonka value on save
    if request.form['action']=="Save":
        var.tinydbName=request.form.get("selectedfile")
        datafield=request.form.get("datafield")
        var.data=request.form.get("data")
        db=TinyDB(var.tinydbName)
        db.insert({datafield:var.data})
        return render_template("tinydb.html")
    if request.form['action']=="Show data":
        var.tinydbName=request.form.get("selectedfile")
        return redirect(url_for('tinyDB.readData'))
    if request.form['action']=="Save multiple":
        var.tinydbName=request.form.get("selectedfile")
        return redirect(url_for('tinyDB.addMultipleItems'))

    

@tinyDB.route("/showdata",methods=['POST','GET'])
def readData():
    datalist=[]
    db=TinyDB(var.tinydbName)
    data=db.all()
    for i in data:
        #doc_id tietueen id-numero käydään ne läpi i-silmukkamuuttujassa
        datalist.append(i.doc_id)
        datalist.append(i)
    return render_template("tinydb.html",datalist=datalist)

@tinyDB.route("/update",methods=['POST','GET'])
def updateData():
    docid=request.form.get('docid')
    db=TinyDB(var.tinydbName)
    db.update({var.datafield:var.data})
    return render_template("tinydb.html")
    

@tinyDB.route("/multiple",methods=['POST','GET'])
def addMultipleItems():
    multipleData=[]
    data=request.form.get("txtmultiple")
    #multipleData.append(data)
    print(data)
    
    #db=TinyDB(var.tinydbName)
    #db.insert_multiple(multipleData)

    return render_template("tinydb.html")



