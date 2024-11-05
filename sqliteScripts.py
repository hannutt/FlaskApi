import io
from flask import Blueprint, render_template, request
import sqlite3,os
from pathlib import Path, PureWindowsPath

sqliteTables=False
runsql=False
sqliteScripts = Blueprint('sqliteScripts',__name__,static_folder='static',template_folder='templates')


@sqliteScripts.route("/sqlite",methods=['POST','GET'])
def readDBname():
    dbNames=[]
    dbSizes=[]
    runsql=True
    i=0
    #kun sqliteTables on true, näytetään filepath input index.htmlssä
    sqliteTables=True
    #käyttäjän syöttämä määrä, montako db tiedostoa etsitään
    restriction = request.form.get('restriction')
    
    #muunto int-tietotyyppiin eli luvuksi.
    restrictionInt = int(restriction)
    sqliteDatabases=[]
    #etsitään db-päätteisiä tiedostoja kaikkialta c-levyltä.
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if file.endswith(".db"):
             i=i+1
             print(os.path.join(root, file))
             dbvar=root+"\\"+file
             dbNames.append(file)
             #db-tiedostojen koot megatavuina
             dbSize=os.stat(dbvar)
           
             #db-tiedostojen koon muunto megatavuiksi
             sizeInMb=dbSize.st_size/(1024*1024)
             dbSizes.append(sizeInMb)
             #pyöritys muotoon 0,00
             roundedSize=round(sizeInMb,2)
             sizeInMbStr = str(roundedSize)
             finalDBvar=dbvar+' | Size: '+sizeInMbStr + ' MB'
             sqliteDatabases.append(finalDBvar)
             #sqliteDatabases.append(sizeInMb)
             #rajoitetaan db päätteiset tiedostot käyttäjän syöttämään määrään
             #i pitää kirjaa siitä, montako db päätteistä tiedostoa on löydetty.
             if i == restrictionInt:
                return render_template("index.html",sqliteDatabases=sqliteDatabases,sqliteTables=sqliteTables,runsql=runsql)

@sqliteScripts.route("/getsqlite",methods=['POST','GET'])
def showSqliteTables():
    sqliteTables=True 
    sqlTables=[]
    global dbname
    dbname=request.form.get('sqliteFile')
    
    conn = sqlite3.connect(dbname)
    
  
     #määritetään tietokantatiedosto, johon yhdistetään
    
    #sql kysely, joka hakee kaikki taulut valitusta tietokannasta
    sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
   
# Create a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    for x in cursor:
       print(x)
       sqlTables.append(x)
    conn.close()

    return render_template("index.html",sqlTables=sqlTables,sqliteTables=sqliteTables)

@sqliteScripts.route("/opentable",methods=['POST','GET'])
def runsqlite():
   selectedTable=request.form.get('selectedTable')
   ids=[]
   data=[]
   
   table=request.form.get("selectedTable")
   conn = sqlite3.connect(dbname)
   #f-stringin avulla voidaan antaan taulun nimi parametrina.
   cursor = conn.execute(f"SELECT * FROM {table}")
   #sarakkeiden nimet, columanames[0] = id kenttä ja se välitetään html-sivulle
   columnnames = list(map(lambda x: x[0], cursor.description))
   finalNames = " ".join(columnnames)
  
   #columnnames listan pituus
   lng = len(columnnames)
   columnInt = int(lng)
   print("columns ",lng)
   
   
   for row in cursor:
      ids.append(row)
      #row on tuple datatyyppi, joten muutetaan se merkkijonoksi että voidaan käyttää replace metodia
      #poistamaan ylim. merkit
      datastr = str(row).replace("(","").replace(")","").replace("'","")
      
      data.append(datastr)
   getDbName(dbname)
   return render_template("sqlite.html",ids=ids,data=data,lng=lng,finalNames=finalNames,dbname=dbname,selectedTable=selectedTable,columnnames=columnnames[0],columnInt=columnInt,columnamesAll=columnnames,table=table)

def getDbName(returnedDB):
   return returnedDB


@sqliteScripts.route("/readInput",methods=['POST','GET'])
def readInput():
   tables=[]
   dbpath=request.form.get("dbPath")
   conn = sqlite3.connect(dbpath)
  
     #määritetään tietokantatiedosto, johon yhdistetään
    
    #sql kysely, joka hakee kaikki taulut valitusta tietokannasta
   sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
   
# Create a cursor object using the cursor() method
   cursor = conn.cursor()
   cursor.execute(sql_query)
   for x in cursor:
       print(x)
       tables.append(x)
   conn.close()
   return render_template("index.html",tables=tables)


#sqliten itse kirjoitettavat kyselyt.
@sqliteScripts.route("/selfwrite",methods=['POST','GET'])
def selfWriteQuery():
   data=[]
   conn = sqlite3.connect(dbname)
   table = request.form.get('selectedTable')
   query = request.form.get('sqliteQuery')
   #f-stringillä voidaan käyttää useampaakin muuttujaa.
   cursor = conn.execute(f"{query} {table}")

   for row in cursor:
      print(row)
      data.append(row)
  
   return render_template("sqlite.html",data=data)

@sqliteScripts.route("/databaseBackup", methods=['POST','GET'])
def backUpDB():
   dbname=request.form.get("sqliteBase")
   conn = sqlite3.connect(dbname)
   with io.open('backupdatabase_dump.sql', 'w') as p:  
          
    # iterdump() function 
    for line in conn.iterdump():
         p.write('%s\n' % line) 
   conn.close()
   return render_template("sqlite.html")

#vastaan otetaan parametrina html:stä saatu id ja sen perusteella poistetaan
@sqliteScripts.route("/deleteSqlite/<id>",methods=['POST','GET'])
def deleteSqliteRecord(id):
      databaseName=request.form.get('dbname')
      databaseTable=request.form.get('sqlSelection')
      idField=request.form.get('idfield')
      #poistetaan id:stä ylim. merkit ja muunnetaan se numeroksi.
      strid=str(id)
      if "," in strid:
         rep=strid.replace(",","").replace(" ","")
         idToInt = int(rep)
         print(idToInt)
      else:
         idToInt = int(id)
         print(idToInt)
      conn=sqlite3.connect(databaseName)
      #sql lause, jossa poistetaan valitusta taulusta id-numeron perusteella
      #idfield on sarake, jossa id-numerot ovat
      cursor=conn.execute(f"DELETE FROM {databaseTable} WHERE {idField}={idToInt}")
      conn.commit()
      conn.close()
      #cursor = conn.execute(f"DELETE FROM {databaseTable}" "WHERE ")
      return render_template("sqlite.html")

#amount on parametri jonka arvo annetaan sqlite.html:ssä. amount sisältää input kenttien lukumäärän
@sqliteScripts.route("/createSqliteRecord/<amount>",methods=['POST','GET'])
def createSqliteRec(amount):
   amounInt=int(amount)
   i=-1
   while i<amounInt:
      j=request.form.get(str(i))
      print(j)
      i=i+1
      
      

     
   print(i)
   return render_template("sqlite.html")
   


   
    
    

    
    