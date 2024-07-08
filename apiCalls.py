from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template,Blueprint
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)

apiCalls = Blueprint('apiCalls',__name__,static_folder='static',template_folder='templates')

#endpoint jossa käyttäjän antama tietokannan nimi parametrina.
@apiCalls.route("/api/db/<name>/<col>",methods=['GET'])
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
         
           #dbkeylistiin talletetaan kokoelman kentän eli _id jne
            dbFields=list(res.keys())
            keysTotal = len(res.keys())
            print("dbkeylist ",dbFields)

            items={
                #dictionaryn avain-arvo pari
                dbFields[0]:str(res),
                
              
               
            }
            
            item.append(items)
            
                    
        return jsonify(item)
    except:InvalidURL
    return "SELECT DATABASE!"

@apiCalls.route("/api/delete/<db>/<col>/<iid>")
def deleteRecord(db,col,iid):

    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db=client[db]
    collection=db[col]
    #poisto id:n perusteella saman kuin sql WHERE
    delquery={"_id":ObjectId(iid)}
    collection.delete_one(delquery)
    return "Record deleted"