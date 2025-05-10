
import os
from flask import Blueprint, render_template, request
from tinydb import TinyDB, Query
from variables import Variables
from localStoragePy import localStoragePy

var=Variables()
storage_backend = "text"
localStorage = localStoragePy("flaskapi", storage_backend)
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
    tinydbName=request.form.get("selectedfile")
    datafield=request.form.get("datafield")
    data=request.form.get("data")
    db=TinyDB(tinydbName)
    db.insert({datafield:data})
    return render_template("tinydb.html")

@tinyDB.route("/showdata",methods=['POST','GET'])
def readData():

    dbase=request.form.get("selectedfile2")
    db=TinyDB(dbase)
    data=db.all()
    
    return render_template("tinydb.html",data=data)

@tinyDB.route("/update",methods=['POST','GET'])
def updateData():
    pass

@tinyDB.route("/multiple",methods=['POST','GET'])
def addMultipleItems():
    multipleData=[]
    data=request.form.get('txtmultiple')
    dbase=request.form.get("selectedfile3")
    multipleData.append(data)
    print(multipleData)
    
    db=TinyDB(dbase)
    db.insert_multiple(multipleData)

    return render_template("tinydb.html")



