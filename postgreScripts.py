import os
from dotenv import load_dotenv
import psycopg2
from flask import Blueprint, redirect, render_template, request
showtables=False
postgreScripts = Blueprint('postgreScripts',__name__,static_folder='static',template_folder='templates')
tableSelected=False
load_dotenv("c:/codes/Python/FlaskApi/.env")
postgrepsw=os.getenv('postgrePsw')
postgreuser=os.getenv('postgreuser')
dbhost=os.getenv('dbhost')
def connection():

    conn = psycopg2.connect(database="",
                            
                            host=dbhost,
                            user=postgreuser,
                            password=postgrepsw,
                            port=5433)
    return conn


@postgreScripts.route("/postgresql",methods=['POST','GET'])
def readPostgre():
    databases=[]
    conn=connection()
    cursor = conn.cursor()
    #haetaan kaikki tietokannat
    cursor.execute("SELECT datname FROM pg_database;")
    for i in cursor.fetchall():
    #i:n tietotyyppi on tuple, joten join metodin avulla muutetaan se merkkijonoksi
    #että voidaan käyttää replace metodia poistamaan ylim. merkit.
        result = "".join(i)
        finalres=result.replace("(","").replace(")","")
        databases.append(finalres)
   
    
    return render_template("postgresql.html",databases=databases)

@postgreScripts.route("/postgretables",methods=['POST','GET'])
def getTables():
    showtables=True
    tables=[]
    sizes=[]
    #talletetaan valitun tietokannan nimi 
    
    db=request.form.get('selectedPostgre')
    
    conn = psycopg2.connect(database=db,
                            
                            host="localhost",
                            user="postgres",
                            password=postgrepsw,
                            port=5433)
    cursor = conn.cursor()
    #haetaan kaikki taulut valitusta tietokannasta.
    cursor.execute(f"""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
""")
    for table in cursor.fetchall():
        result = "".join(table)
        finalres=result.replace("(","").replace(")","")
        tables.append(finalres)
        #valitun tietokannan koko
    cursor.execute(f"SELECT pg_size_pretty (pg_database_size ('{db}')) size;")
    for j in cursor:
        print(j)
        sizes.append(j)
    return render_template("postgresql.html",showtables=showtables,tables=tables,j=j,db=db)

@postgreScripts.route("/showpostgretable/<db>",methods=['POST','GET'])
def showPostgreTable(db):
    x=0
    global postgredb
    postgredb=db
    tableSelected=True
    tabledata=[]
    global columnname
    columnname=[]
 
    conn = psycopg2.connect(database=db,
                            host="localhost",
                            user="postgres",
                            password=postgrepsw,
                            port=5433)
    global tablename
    tablename=request.form.get("postgreTable")
    cursor=conn.cursor()
    
    cursor.execute(f"SELECT * FROM {tablename}")
    #sarakkeiden otsikot
    column_names = [desc[0] for desc in cursor.description] 
    for i in cursor.fetchall():
        tabledata.append(i)
    #sarakeiden nimet
    for j in column_names:
        columnname.append(j)
        x=x+1
    return render_template("postgresql.html",tabledata=tabledata,columnname=columnname,tableSelected=tableSelected,tablename=tablename,x=x)

@postgreScripts.route("/writepostgre",methods=['POST','GET'])
def writePostgreQuery():
     tabledata=[]
     conn = psycopg2.connect(database=postgredb,
                            host="localhost",
                            user="postgres",
                            password=postgrepsw,
                            port=5433)
     
     query=request.form.get("writePostgre")
     cursor=conn.cursor()
     
     #jos query alkaa sanalla insert toteutaan commit funktio, joka tallentaan datan kantaan
     if query.startswith("INSERT") or query.startswith("insert"):
        cursor.execute(query)
        conn.commit()
     elif query.startswith("UPDATE") or query.startswith("update"):
           cursor.execute(query)
           conn.commit()
     else:
        cursor.execute(query)
        for c in cursor.fetchall():
             tabledata.append(c)
    
    
     return render_template("postgresql.html",tabledata=tabledata)

@postgreScripts.route("/postgrecrud", methods=['POST','GET'])
def postgreCrud():
    data=[]
    fields=request.form.get("fieldsNum")
    fieldsInt=int(fields)
    #jos on painettu buttonia, jonka value on editBtn
    editBtn = request.form.get('editBtn')
    delBtn=request.form.get("delBtn")
  
    if editBtn:
         for i in range(0,fieldsInt):
             #kierrosmuuttuja täytyy muuntaa merkkijonoksi koska input kentän name attribuutti on myös merkkijono
             #tyyppinen.
             i=str(i)
             j=request.form.get(i)
             data.append(j)
         print(data)
         print(columnname)           
         
        
         conn = psycopg2.connect(database=postgredb,
                            host="localhost",
                            user="postgres",
                            password=postgrepsw,
                            port=5433)
         conn = cursor=conn.cursor()
         sql=f"UPDATE {tablename} set model={data[2]} WHERE id=1"
         cursor.execute(sql)
         conn.close()
         
    if delBtn:
        print("deleting")
    
    return render_template("postgresql.html")

@postgreScripts.route("/postgresqldelete", methods=['POST','GET'])
def deletePostgreRecord():
    id=request.form.get("id")
    idToInt=int(id)
 
    conn = psycopg2.connect(database=postgredb,
                            host="localhost",
                            user="postgres",
                            password=postgrepsw,
                            port=5433)
    sql=f"DELETE FROM {tablename} WHERE ID ={idToInt}"
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return render_template("postgresql.html")


    


