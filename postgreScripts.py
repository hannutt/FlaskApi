import psycopg2
from flask import Blueprint, render_template, request
showtables=False
postgreScripts = Blueprint('postgreScripts',__name__,static_folder='static',template_folder='templates')
tableSelected=False
def connection():

    conn = psycopg2.connect(database="",
                            
                            host="localhost",
                            user="postgres",
                            password="SkaneBorg12!",
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
        print(i)
        databases.append(i)
   

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
                            password="SkaneBorg12!",
                            port=5433)
    cursor = conn.cursor()
    #haetaan kaikki taulut valitusta tietokannasta.
    cursor.execute(f"""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
""")
    for table in cursor.fetchall():
        print(table)
        tables.append(table)
        #valitun tietokannan koko
    cursor.execute(f"SELECT pg_size_pretty (pg_database_size ('{db}')) size;")
    for j in cursor:
        print(j)
        sizes.append(j)
    return render_template("postgresql.html",showtables=showtables,tables=tables,j=j,db=db)

@postgreScripts.route("/showpostgretable/<db>",methods=['POST','GET'])
def showPostgreTable(db):
    global postgredb
    postgredb=db
    tableSelected=True
    tabledata=[]
    columnname=[]
 
    conn = psycopg2.connect(database=db,
                            host="localhost",
                            user="postgres",
                            password="SkaneBorg12!",
                            port=5433)
    global tablename
    tablename=request.form.get("postgreTable")
    cursor=conn.cursor()
    
    cursor.execute(f"SELECT * FROM {tablename}")
    #sarakkeiden otsikot
    column_names = [desc[0] for desc in cursor.description] 
    for i in cursor.fetchall():
        tabledata.append(i)
    for j in column_names:
        columnname.append(j)
    return render_template("postgresql.html",tabledata=tabledata,columnname=columnname,tableSelected=tableSelected)

@postgreScripts.route("/writepostgre",methods=['POST','GET'])
def writePostgreQuery():
     tabledata=[]
     conn = psycopg2.connect(database=postgredb,
                            host="localhost",
                            user="postgres",
                            password="SkaneBorg12!",
                            port=5433)
     
     query=request.form.get("writePostgre")
     cursor=conn.cursor()
     cursor.execute(query)
     for c in cursor.fetchall():
         tabledata.append(c)
     return render_template("postgresql.html",tabledata=tabledata)

    


