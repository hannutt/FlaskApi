
from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template
from flask_pymongo import PyMongo,MongoClient
from string import Template

import pymongo


app = Flask(__name__)


@app.route("/")


def showIndex():
     dbsList = []
     dbs=MongoClient().list_database_names()
     client = MongoClient('localhost', 27017)
     mydatabase = client.quizDB
     collections = mydatabase.list_collection_names()
     print(collections)
     for i in dbs:
          dbsList.append(i)
    
     return render_template('index.html',dbsList=dbsList)

@app.route("/show-form",methods=['POST'])
def show_data():
    l=[]
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dataBaseName=request.form.get("selecDB")
    dataBaseNameStr = str(dataBaseName)
    print("db name ",dataBaseNameStr)
    collectionName = request.form.get("colname")
    collectionNameStr=str(collectionName)
    print("collection name ",collectionNameStr)
    
    dbname=client[dataBaseNameStr]
    collection=dbname[collectionNameStr]
    result= collection.find({},{ "_id": 1, "name": 1,"points":1})
    for i in result: 
        print(i)    
   
    
    '''
    l=[]
    path = request.form.get('DBpath')
    app.config['MONGO_URI']=path
    global mongodb
    col="results"
    mongodb=PyMongo(app).db
    
    results=mongodb.results.find({},)
    for res in results:
        l.append(res) 
        print(res)
    '''
    return render_template("selectCol.html",result=result)

@app.route('/read-form', methods=['POST']) 
def read_form():
 
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    #client = MongoClient('localhost', 27017)
    selectedDB = request.form.get('DBname')
    print(selectedDB)
    dbname=client[selectedDB]
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
    
    
    return render_template('selectCol.html',dbname=dbname,cols=cols,selectedDB=selectedDB)




@app.route("/api/all",methods=['GET'])
def read():
    try:

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
@app.route("/findName/<name>")
def searchByname(name):
    user = mongodb.results.find_one({"name": name})
    #jos nimi löytyy, items sanakirja-olioon talletetaan user eli löydetyn nimen id,nimi ja pisteet
    if user:
            userinfo={

            "id":str(user['_id']),
            "name":str(user['name']),
            "points":user['points'],
        }
     
    return jsonify({'userinfo':userinfo})

@app.route('/deleteName/<name>')
def delByname(name):
     user = mongodb.results.find_one({"name": name})
     if user:
          mongodb.results.delete_one({"name":name})
          return 'DELETED'
     
    
if __name__ == '__main__':
    app.run(debug=True)






