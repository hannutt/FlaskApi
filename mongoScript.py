from flask import Blueprint, render_template, request
import pymongo

mongoScript = Blueprint('mongoScript',__name__,static_folder='static',template_folder='templates')


#luodaan uusi kokoelman käyttäjän antamalla nimellä.
@mongoScript.route("/newcollection",methods=['POST','GET'])
def createNewCollection():
    dataBaseName = request.form.get('mongoDBname')
    colName = request.form.get('collectionName')
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dbname=client[dataBaseName]
    newcol = dbname[colName]
    insertQuery={'word':"Balloon"}
    newcol.insert_one(insertQuery)

    return render_template("selectCol.html")

@mongoScript.route("/dropcollection",methods=['POST','GET'])
def dropCollection():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dataBaseName=request.form.get('DB')
    colName=request.form.get('colToDelete')
    dbname=client[dataBaseName]
    delCol = dbname[colName]
    delCol.drop()

    return render_template("selectCol.html")



