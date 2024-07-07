
from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo


app = Flask(__name__)

showdata = False

@app.route("/")

def showIndex():
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
     
    
          
    
     return render_template('index.html',dbsList=dbsList,stats=statsNames,statsNums=statsNums,allStats=allStats)



@app.route("/statistic",methods=['POST'])
def DB_Statistics():
    print(statsNames)

    return render_template('index.html',stats=statsNames)

@app.route('/read-form', methods=['POST']) 
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
   
    #print(dbname)
    #DbNameOnly = request.form.get('DBname')
    #mydatabase = client.DbNameOnly
    #collections = mydatabase.list_collection_names()
    #print(collections)
    #collections=mydatabase.list_collection_names()
    #collections = mydatabase.list_collection_names()
    #print(collections)
   
    
    #print(selectedDB)

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
    for i in result: 
        print(i)
        l.append(i)
        #tietokannan kenttien nimet muunnetaan listamuotoon.
        dbKeysList=list(i.keys())

    
    #lasketaan kokoelman kenttien määrä
    keysTotal = len(i.keys())
        
    return render_template("selectCol.html",l=l,dbKeysList=dbKeysList,showdata=showdata,keysTotal=keysTotal,collections=collections,datasizeRound=datasizeRound,objects=objects,selectedDB=selectedDB)


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

#endpoint jossa käyttäjän antama tietokannan nimi parametrina.
@app.route("/api/db/<name>/<col>",methods=['GET'])
def readDB(name,col):
    print(name)
    try:
        app.config['MONGO_URI']='mongodb://localhost:27017/'+name
        #global mongodb
        mongodb=PyMongo(app).db
        item=[]
        
        
        #asetetaan collection nimi, eli parametrina tuleva col ja haetaan collectionista
        #data
        results = mongodb[col].find({},)
        dbKeys=[]

    
    #lasketaan kokoelman kenttien määrä
    #keysTotal = len(i.keys())
        for res in results:
         
           #lasketaan ja tietokannan kokoelman kenttien määrä ja lisätään se listaan
            dbKeysList=list(res.keys())
            keysTotal = len(res.keys())
            print(dbKeysList)

            items={
                #käytetään kenttiä tiedon näyttämisessä.
                dbKeysList[0]:str(res),
               
            }
            
            item.append(items)
            print(item)
                    
        return jsonify(item)
    except:InvalidURL
    return "SELECT DATABASE!"

@app.route('/api/delete/<db>/<col>/<iid>',methods=['GET','DELETE'])
def delByname(db,col,iid):
     print("id ",iid)
     app.config['MONGO_URI']='mongodb://localhost:27017/quizDB'+db
        #global mongodb
     mongodb=PyMongo(app).db
     #removeId = mongodb[col].find_one({"_id":iid})
     #if removeId:
     delquery={"word":iid}
     mongodb[col].delete_one(delquery)
     return "deleted"


    
if __name__ == '__main__':
    app.run(debug=True)






