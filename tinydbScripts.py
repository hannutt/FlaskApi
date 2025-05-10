
import os
from flask import Blueprint, redirect, render_template, request, url_for
from tinydb import TinyDB, Query
from variables import Variables
from localStoragePy import localStoragePy

var=Variables()

tinyDB = Blueprint('tinyDB',__name__,static_folder='static',template_folder='templates')


def returnPath():
    path=request.form.get("selectedfile")
    return path
    

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

@tinyDB.route("/showdata",methods=['POST','GET'])
def readData():
   
    #dbase=request.form.get("selectedfile2")
    db=TinyDB(var.tinydbName)
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



