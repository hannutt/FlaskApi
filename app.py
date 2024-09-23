
from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template
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

import urllib
app = Flask(__name__)
app.register_blueprint(cruds,url_prefix='')
app.register_blueprint(apiCalls,url_prefix='')
app.register_blueprint(cloudConnection,url_prefix='')
app.register_blueprint(mysqlScripts,url_prefix='')
load_dotenv("c:/codes/Python/FlaskApi/.env")
showdata = False
connect=False

def showSQLDataBases():
    sqlDataBases = []

    mydb = mysql.connector.connect(
       
        host="localhost",
        user="root",
        password="Root512!",
)
    cursor = mydb.cursor()
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
     global statsNames
     statsNames=[]
     global statsNums
     statsNums=[]
     global allStats
     allStats=[]
    

     #tietokanta nimien listaus
     dbs=MongoClient().list_database_names()
     client = MongoClient('localhost', 27017)
   
     #mydatabase = client.quizDB
     #collections = mydatabase.list_collection_names()
     #print(collections)
     for i in dbs:
          dbsList.append(i)
        
          print(i)
     
          db=client[i]
          call = db.command("dbstats")
          datasize = call['dataSize'] / 1024
          collections = call['collections']
          print('Collections:', str(collections))
          print('Size:', str(datasize) + 'Mb')
          roundedSize = round(datasize,2)
        
          statsNames.append(i)
      
          statsNums.append(roundedSize)
          allStats.append(i)
          allStats.append(datasize)
          amountOfdb=len(dbsList)
        
    #listan alkioiden muunto int-tyyppiseksi
     for j in range(0, len(statsNums)):

    
        statsNums[j] = int(statsNums[j])    
          
     print(amountOfdb)
     return render_template('index.html',dbsList=dbsList,stats=statsNames,statsNums=statsNums,allStats=allStats,dbsAtlas=dbsAtlas,amountOfdb=amountOfdb,sqls=sqls,collections=collections)



@app.route("/statistic",methods=['POST'])
def DB_Statistics():
    print(statsNames)

    return render_template('index.html',stats=statsNames)

@app.route('/read-form', methods=['POST','GET']) 
def read_form():
   
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    #client = MongoClient('localhost', 27017)
    global selectedDB
    selectedDB = request.form.get('DBname')
    print(selectedDB)
   
    
    #db-statistiikka koodi, collectionien määrä, koko jne.
    dbname=client[selectedDB]
    call = dbname.command("dbstats")
    datasize = call['dataSize'] / 1024
    global datasizeRound
    datasizeRound=round(datasize,2)
    global collections
    collections = call['collections']
    global objects
    objects = call['objects']
   

    app.config['MONGO_URI']='mongodb://localhost:27017/'+selectedDB
    #global mongodb
    mongodb=PyMongo(app).db
    #global cols
    cols=mongodb.list_collection_names()
    # Get the form data as Python ImmutableDict datatype  
    data = request.form
    
    
    return render_template('selectCol.html',dbname=dbname,cols=cols,selectedDB=selectedDB,collections=collections,datasizeRound=datasizeRound,objects=objects)


    


#näyttää kaiken datan kokoelmasta
@app.route("/show-form",methods=['POST'])
def show_data():

    global showdata
    showdata=True
    l=[]
    dbKeys=[]
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    
    dataBaseName=request.form.get("selecDB")
    global dataBaseNameStr
    dataBaseNameStr = str(dataBaseName)
    collectionName = request.form.get("colname")
    global collectionNameStr
    collectionNameStr=str(collectionName)
    findLimit = request.form.get("DBlimit")
    print("collection name ",collectionNameStr)
   
        

    dbname=client[dataBaseNameStr]
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
        result=collection.find()
        count = collection.find().count()
    for i in result: 
        print(i)
        l.append(i)
        #tietokannan kenttien nimet muunnetaan listamuotoon.
        dbKeysList=list(i.keys())
        print(dbKeysList)

    
    #lasketaan kokoelman kenttien määrä
        global keysTotal
        keysTotal = len(i.keys())
    
        
    return render_template("selectCol.html",l=l,dbKeysList=dbKeysList,showdata=showdata,keysTotal=keysTotal,datasizeRound=datasizeRound,objects=objects,selectedDB=selectedDB,collectionNameStr=collectionNameStr,count=count)

@app.route("/mongo-query", methods=['POST','GET']) 
def runMongoQuery():
    dataMongo=[]
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dbname=client[dataBaseNameStr]
    col=dbname[collectionNameStr]
    text=request.form.get("mongodata")
    #katkaistaan teksti kaksoispisteen kohdalta 2 lista-alkioksi
    t=text.split(":")
    #kyselynä toimii t listan 0 ja 1 elementit eli esim word:susi
    query={t[0]:t[1]}
    result=col.find(query)
    
    for x in result:
        dataMongo.append(x)
    return render_template("selectCol.html",dataMongo=dataMongo)
    
if __name__ == '__main__':
    app.run(debug=True)






