from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template,Blueprint
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv("c:/codes/Python/FlaskApi/.env")


cloudConnection = Blueprint('cloudConnection',__name__,static_folder='static',template_folder='templates')

@cloudConnection.route("/readAtlasDB",methods=['POST','GET'])
def readAtlasDB():
    
    my_psw=os.getenv('my_psw')
    my_user=os.getenv('my_user')
    username = urllib.parse.quote(str(my_user))
    password = urllib.parse.quote(str(my_psw))
    uri = "mongodb+srv://{}:{}@cluster0.gfnzlpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)
    client = MongoClient(uri,server_api=ServerApi('1'))
    name=request.form.get('nameOfDb')
    dbName=client[name]
    collections=dbName.list_collection_names()
    print(name)
    print(collections)
    return render_template('cloudSelect.html',name=name,collections=collections)

@cloudConnection.route('/cloud',methods=['POST','GET'])

def getDataFromAtlas():
    l=[]
    my_psw=os.getenv('my_psw')
    my_user=os.getenv('my_user')
    username = urllib.parse.quote(str(my_user))
    password = urllib.parse.quote(str(my_psw))
    
    uri = "mongodb+srv://{}:{}@cluster0.gfnzlpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)

    DBname=request.form.get('atlasDBName')
    colName=request.form.get('atlasCollection')
# Create a new client and connect to the server
    
    client = MongoClient(uri,server_api=ServerApi('1'))
   # dbList=client.list_database_names()
    dbName=client[DBname]
    collection=dbName[colName]

# Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        res=collection.find()
        for i in res:
            l.append(i)
    
    except Exception as e:
        print(e)
    
    return render_template('cloudSelect.html',l=l)

