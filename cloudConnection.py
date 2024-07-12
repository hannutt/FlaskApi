from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template,Blueprint
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse


cloudConnection = Blueprint('cloudConnection',__name__,static_folder='static',template_folder='templates')

@cloudConnection.route('/cloud',methods=['POST','GET'])
def connectAtlas():
    l=[]
    psw=request.form.get('psw')
    user=request.form.get('user')
    username = urllib.parse.quote(str(user))
    password = urllib.parse.quote(str(psw))

    
    uri = "mongodb+srv://{}:{}@cluster0.gfnzlpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)

    DBname=request.form.get('dbname')
    colName=request.form.get('colname')
# Create a new client and connect to the server
    client = MongoClient(uri,server_api=ServerApi('1'))
    dbName=client[DBname]
    collection=dbName[colName]

# Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        res=collection.find()
        for i in res:
            print(i)
            l.append(i)
    
    except Exception as e:
        print(e)
    
    print(username,password)
    return render_template('cloud.html',l=l)