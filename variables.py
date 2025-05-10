import os
from dotenv import load_dotenv
import mysql
import psycopg2
from flask_pymongo import PyMongo,MongoClient
load_dotenv("c:/codes/Python/FlaskApi/.env")
mysqluser=os.getenv('mySQLuser')
mysqlpsw=os.getenv('mySQLpsw')
dbhost=os.getenv('dbhost')
postgrepsw=os.getenv('postgrePsw')
postgreuser=os.getenv('postgreuser')


class Variables():
     def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sqltable=""
        self.sqldata=[]
        self.databaseName=""
        self.MySqldbConnector= mysql.connector.connect(
       
        host=dbhost,
        user=mysqluser,
        password=mysqlpsw,
        database=''
)
        self.postgretable=''
        self.DBname=''
        self.statsNames=[]
        self.statsNums=[]
        self.allStats=[]
        self.client=MongoClient('localhost', 27017)
        self.datasizeRound=0
        self.collections=""
        self.objects=""
        self.tinydbName=""
      
        self.postgreConnector=psycopg2.connect(database='',host=dbhost,user=postgreuser,password=postgrepsw,port=5433)