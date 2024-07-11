from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template,Blueprint
from flask_pymongo import PyMongo,MongoClient
from string import Template
from bson.objectid import ObjectId
import pymongo


cloudConnection = Blueprint('cloudConnection',__name__,static_folder='static',template_folder='templates')