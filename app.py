
from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

from cruds import cruds
from apiCalls import apiCalls
from cloudConnection import cloudConnection
import urllib
app = Flask(__name__)
app.register_blueprint(cruds,url_prefix='')
app.register_blueprint(apiCalls,url_prefix='')
app.register_blueprint(cloudConnection,url_prefix='')
load_dotenv("c:/codes/Python/FlaskApi/.env")
showdata = False
def listDataBases():
    
    
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
    return dbList

@app.route("/",methods=['GET','POST'])

def showIndex():
     listDataBases()
     dbsAtlas=listDataBases()
     print("atlas db")
     
     dbsList = []
     global statsNames
     statsNames=[]
     global statsNums
     statsNums=[]
     global allStats
     allStats=[]
    

     
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
    #listan alkioiden muunto int-tyyppiseksi
     for j in range(0, len(statsNums)):

    
        statsNums[j] = int(statsNums[j])

     
     #dbcom=mydatabase.command("dbstats")
     #print(dbcom)
     #print(selection)
     
    
          
     
     return render_template('index.html',dbsList=dbsList,stats=statsNames,statsNums=statsNums,allStats=allStats,dbsAtlas=dbsAtlas)



@app.route("/statistic",methods=['POST'])
def DB_Statistics():
    print(statsNames)

    return render_template('index.html',stats=statsNames)

@app.route('/read-form', methods=['POST','GET']) 
def read_form():
    print('read func')
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
    
    print('show func')
    global showdata
    showdata=True
    l=[]
    dbKeys=[]
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dataBaseName=request.form.get("selecDB")
    dataBaseNameStr = str(dataBaseName)
    print("db name ",dataBaseNameStr)
    collectionName = request.form.get("colname")
    collectionNameStr=str(collectionName)
    print("collection name ",collectionNameStr)
    
    dbname=client[dataBaseNameStr]
    collection=dbname[collectionNameStr]
    result= collection.find()
    count = collection.find().count()
    for i in result: 
        print(i)
        l.append(i)
        #tietokannan kenttien nimet muunnetaan listamuotoon.
        dbKeysList=list(i.keys())

    
    #lasketaan kokoelman kenttien määrä
    global keysTotal
    keysTotal = len(i.keys())
    
        
    return render_template("selectCol.html",l=l,dbKeysList=dbKeysList,showdata=showdata,keysTotal=keysTotal,collections=collections,datasizeRound=datasizeRound,objects=objects,selectedDB=selectedDB,collectionNameStr=collectionNameStr,count=count)





#api-kutsu
@app.route("/api/all",methods=['GET'])
def read():
    try:
        app.config['MONGO_URI']='mongodb://localhost:27017/quizDB'
        #global mongodb
        mongodb=PyMongo(app).db

        item=[]
        results = mongodb.results.find({},)
        #keyLen=len(res.keys())
        #print("keylen: ",keyLen)
        for res in results:
         
            first_key = list(res.keys())[0]
            sec_key = list(res.keys())[1]
            third_key= list(res.keys())[2]

            items={

                "id":str(res[first_key]),
                "name":str(res[sec_key]),
                "points":res[third_key],
            }
            item.append(items)
           
        
        return jsonify(item)
    except:InvalidURL
    return "SELECT DATABASE!"
#tässä haetaan nimen perusteella mongokannasta <name> on parametri johon kirjoitetaan haetun käyttäjän nimi, esim.
#http://127.0.0.1:5000/findName/keijo



@app.route('/api/delete/<db>/<iid>',methods=['GET','DELETE'])
def delByname(db,iid):
     print("id ",iid)
     app.config['MONGO_URI']='mongodb://localhost:27017/quizDB'+db
     mongodb=PyMongo(app).db
     delete = mongodb.words.find_one({"_id":ObjectId(iid)})
     if delete:
          mongodb.words.delete_one({"_id":ObjectId(iid)})
          return 'DELETED'
        #global mongodb
     else:
         return "something went wrong"

     
    
   
     #if removeId:
     #delquery={"word":iid}
     #mongodb[col].delete_one({":_id":ObjectId(iid)})
     #return "deleted"


    
if __name__ == '__main__':
    app.run(debug=True)






