from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template,Blueprint
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo

cruds = Blueprint('cruds',__name__,static_folder='static',template_folder='templates')

@cruds.route('/edit-form',methods=['POST'])
def editRecords():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    collection = request.form.get('col')
    Dbase= request.form.get('DB')
    iid = request.form.get('objId2')
    word = request.form.get('1')
    db=client[Dbase]
    col=db[collection]
    #ehto, päivitetään id:n perusteella
    updateQuery={"_id":ObjectId(iid)}
    #uusi arvo lisätään word-kenttään
    newvalue= { "$set": { "word":word } }
    col.update_one(updateQuery,newvalue)
    
    return render_template('selectCol.html')

@cruds.route("/del-record",methods=['POST'])
def delRecord():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    collection = request.form.get('col')
    Dbase= request.form.get('DB')
    iid = request.form.get('objId')
    db=client[Dbase]
    col=db[collection]
    #poisto id:n perusteella saman kuin sql WHERE
    delquery={"_id":ObjectId(iid)}
    col.delete_one(delquery)
    
   
   
    print(iid,Dbase,collection)
    return render_template('index.html')