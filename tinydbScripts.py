
import os
from flask import Blueprint, redirect, render_template, request, url_for
from tinydb import TinyDB, Query
from tinydb.table import Document
from variables import Variables


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
        data=request.form.get('txtmultiple')
        #splittaus : merkin kohdalta eli luodaan data muuttujan sisällöstä lista, jokainen sana : merkkien molemmin
        #puolin on oma lista-alkionsa
        datalist=data.split(":")
        #Luo sanakirjan listasta yhdistämällä elementtejä käyttämällä joka toista elementtiä arvona ja toista avaimena
        listToDict = {datalist[i]: datalist[i + 1] for i in range(0, len(datalist), 2)}    
        var.tinydbName=request.form.get("selectedfile")
        db=TinyDB(var.tinydbName)
      
        db.insert(listToDict)
        return render_template("tinydb.html")
    
    if request.form['action']=="Show data":
        var.tinydbName=request.form.get("selectedfile")
        return redirect(url_for('tinyDB.readData'))
    if request.form['action']=="Update data":
        var.tinydbName=request.form.get("selectedfile")
        var.recordid=request.form.get("recordId")
        var.data=request.form.get('txtmultiple')
        return redirect(url_for('tinyDB.updateData'))

    

@tinyDB.route("/showdata",methods=['POST','GET'])
def readData():
    datalist=[]
    db=TinyDB(var.tinydbName)
    data=db.all()
    for i in data:
        #doc_id tietueen id-numero käydään ne läpi i-silmukkamuuttujassa
        #datalist.append(i.doc_id)
        datalist.append(i)
    return render_template("tinydb.html",datalist=datalist)

@tinyDB.route("/update",methods=['POST','GET'])
def updateData():

    
    db=TinyDB(var.tinydbName)
    content=Query()
    
    datalist=var.data.split(":")
    print(datalist)
    listToDict = {datalist[i]: datalist[i + 1] for i in range(0, len(datalist), 2)} 
    #db.update(listToDict,content.pid=='14')
    
    return render_template("tinydb.html")
    





