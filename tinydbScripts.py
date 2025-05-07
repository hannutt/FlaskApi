
import os
from flask import Blueprint, render_template, request
from tinydb import TinyDB, Query

tinyDB = Blueprint('tinyDB',__name__,static_folder='static',template_folder='templates')

@tinyDB.route("/openPage",methods=['POST','GET'])
def openTinyDBPage():
    return render_template("tinydb.html")

@tinyDB.route("/createfile",methods=['POST','GET'])
def createFile():
    fname=request.form.get('fileName')
    db=TinyDB(fname)
    return render_template("tinydb.html")

@tinyDB.route("/getjson",methods=['POST','GET'])
def getJsonFiles():
    currentdirectory = os.getcwd()
    ext=".json"
    for files in os.listdir(currentdirectory):
        if files.endswith(ext):
            print(files)
    return render_template("tinydb.html")  