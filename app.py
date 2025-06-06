
from http.client import InvalidURL
from variables import Variables
from flask import Flask, flash, request, json, Response,jsonify,render_template
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import mysql.connector
from cruds import cruds
from apiCalls import apiCalls
from cloudConnection import cloudConnection
from mysqlScripts import mysqlScripts
from sqliteScripts import sqliteScripts
from mongoScript import mongoScript
from sqliteScripts2 import sqliteScripts2
from postgreScripts import postgreScripts
from azureScripts import azureScripts
from tinydbScripts import tinyDB

import urllib
app = Flask(__name__)
app.register_blueprint(cruds,url_prefix='')
app.register_blueprint(apiCalls,url_prefix='')
app.register_blueprint(cloudConnection,url_prefix='')
app.register_blueprint(mysqlScripts,url_prefix='')
app.register_blueprint(sqliteScripts,url_prefix='')
app.register_blueprint(mongoScript,url_prefix='')
app.register_blueprint(sqliteScripts2,url_prefix='')
app.register_blueprint(postgreScripts,url_prefix='')
app.register_blueprint(azureScripts,url_prefix='')
app.register_blueprint(tinyDB,url_prefix='')

showdata = False
connect=False
var = Variables()
var.client
def showSQLDataBases():
    sqlDataBases = []

    cursor = var.MySqldbConnector.cursor()
    databases = ("show databases")
    cursor.execute(databases)
    for (databases) in cursor:
         print (databases[0])
         sqlDataBases.append(databases[0])

    return sqlDataBases


def listAtlasDataBases():
    
    
    #salasana ja käyttäjätunnus on tallenettu .env ympäristömuuttujatiedostoon.
    #tässä ne haetaan avain-arvopareina, eli my_psw on avain ja env tiedostossa sen jälkeinen merkkijono
    #on arvo eli salasana
    my_psw=os.getenv('my_psw')
    my_user=os.getenv('my_user')
    username = urllib.parse.quote(str(my_user))
    password = urllib.parse.quote(str(my_psw))
    uri = "mongodb+srv://{}:{}@cluster0.gfnzlpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)
    client = MongoClient(uri,server_api=ServerApi('1'))
    dbList=client.list_database_names()
    #palautetaan dbslist, että sitä voidaan käyttää seuraavassa funktiossa
    return dbList


@app.route("/",methods=['GET','POST'])

def showIndex():
     #toisen moduulin funktiota voi käyttää näin, kunhan se tuodaan import lauseella ja route on kunnossa.
     sqls=showSQLDataBases()
     listAtlasDataBases()
     dbsAtlas=[]
     dbsAtlas=listAtlasDataBases()
   
    
     
     dbsList = []
     #tietokanta nimien listaus
     dbs=MongoClient().list_database_names()
     #client = MongoClient('localhost', 27017)
     #haetaan vain pääkansiot ilman alikansioita c-asemalta
     dirs=next(os.walk('c:\\'))[1]
     #lisätään merkki c:\\ jokaisen lista-alkion eteen. kenoviivoja on 4, että ne voidaan
     #korvata myöhemmin koodissa yhdellä kenoviivalla replace-metodin avulla. (readInput funktio
     # sqliteScript.py:ssä)
     dirsFinal=["C:\\"+  d for d in dirs]
    
     #mydatabase = client.quizDB
     #collections = mydatabase.list_collection_names()
     #print(collections)
     for i in dbs:
          dbsList.append(i)
          db=var.client[i]
          call = db.command("dbstats")
          datasize = call['dataSize'] / 1024
          var.collections = call['collections']
          roundedSize = round(datasize,2)
        
          var.statsNames.append(i)
      
          var.statsNums.append(roundedSize)
          var.allStats.append(i)
          var.allStats.append(datasize)
          amountOfdb=len(dbsList)
        
    #listan alkioiden muunto int-tyyppiseksi
     for j in range(0, len(var.statsNums)):
        var.statsNums[j] = int(var.statsNums[j])
   
     return render_template('index.html',dbsList=dbsList,stats=var.statsNames,statsNums=var.statsNums,allStats=var.allStats,dbsAtlas=dbsAtlas,amountOfdb=amountOfdb,sqls=sqls,collections=var.collections,dirsFinal=dirsFinal)



@app.route("/statistic",methods=['POST'])
def DB_Statistics():

    return render_template('index.html',stats=var.statsNames)

@app.route('/mongodb/', methods=['POST','GET']) 
def read_form():
   
   
    #client = MongoClient('localhost', 27017)
    #global selectedDB
    selectedDB = request.form.get('DBname')
    #db-statistiikka koodi, collectionien määrä, koko jne.
    dbname=var.client[selectedDB]
    call = dbname.command("dbstats")
    datasize = call['dataSize'] / 1024
   
    var.datasizeRound=round(datasize,2)
    var.collections = call['collections']
    var.objects = call['objects']
   
    
    app.config['MONGO_URI']='mongodb://localhost:27017/'+selectedDB
    
    mongodb=PyMongo(app).db
    cols=mongodb.list_collection_names()
    # Get the form data as Python ImmutableDict datatype  
    data = request.form
    
    
    return render_template('selectCol.html',dbname=dbname,cols=cols,selectedDB=selectedDB,collections=var.collections,datasizeRound=var.datasizeRound,objects=var.objects)


#näyttää kaiken datan kokoelmasta
@app.route("/readcollection/<selectedDB>",methods=['POST'])
def show_data(selectedDB):

    showdata=True
    data=[]
    ids=[]
    dbKeys=[]
    dataBaseNameStr = str(selectedDB)
    collectionName = request.form.get("colname")
    collectionNameStr=str(collectionName)
    findLimit = request.form.get("DBlimit")
   
    dbname=var.client[dataBaseNameStr]
    collection=dbname[collectionNameStr]
    #jos dblimit syötekntän arvo on muu kuin tyhjä, ja sisältö on mumeroita,käytetään haussa limit metodia.
    if findLimit !="" and findLimit.isdigit():
        findLimitInt=int(findLimit)
        result= collection.find().limit(findLimitInt)
        #löydettyjen tietuiden määrän lasku
        count = collection.find().count()
        #jos ei ole tyhjä, voi sisältää numeroita ja kirjaimia
    elif findLimit !="":
        fieldName= request.form.get("fieldNames")
        #db.content.find({$text:{$search:"love"}})  
        collection.create_index([(fieldName, 'text')])
        result = collection.find({"$text": {"$search":findLimit}})
        count = collection.find().count()
    else:
        #haetaan vain id numerot
        resultid=collection.find({}, {"_id": 1})
        for j in resultid:
            ids.append(j)

        #data ilman id kenttää
        result=collection.find()
        count = collection.find().count()
        for i in result: 
            data.append(i)
        #tietokannan kenttien nimet muunnetaan listamuotoon.
        dbKeysList=list(i.keys())
    #lasketaan kokoelman kenttien määrä
        keysTotal = len(i.keys())
        
    return render_template("selectCol.html",data=data,dbKeysList=dbKeysList,showdata=showdata,keysTotal=keysTotal,datasizeRound=var.datasizeRound,objects=var.objects,selectedDB=selectedDB,collectionNameStr=collectionNameStr,count=count,ids=ids)

@app.route("/mongo-query/<selectedDB>/<collection>", methods=['POST','GET']) 
def runMongoQuery(selectedDB,collection):
    dataMongo=[]
    dbname=var.client[selectedDB]
    col=dbname[collection]
    text=request.form.get("mongodata")
    #katkaistaan teksti kaksoispisteen kohdalta 2 lista-alkioksi
    t=text.split(":")
    #kyselynä toimii t listan 0 ja 1 elementit eli esim word:susi
    query={t[0]:t[1]}
    result=col.find(query)
    
    #näytetään käyttäjän kirjoittaman kyselyn tulos
    for x in result:
        dataMongo.append(x)
    
    return render_template("selectCol.html",dataMongo=dataMongo)
    
if __name__ == '__main__':
    app.run(debug=True)






