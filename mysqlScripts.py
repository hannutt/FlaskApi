from flask import Blueprint, render_template, request
import mysql.connector

mysqlScripts = Blueprint('mysqlScripts',__name__,static_folder='static',template_folder='templates')

tablesShown=False
@mysqlScripts.route("/mysql",methods=['POST','GET'])
def readSelectedSql():
       tables=[]
       
       global dbname
       dbname=request.form.get('selectedSQL')
      
       mydb = mysql.connector.connect(
       
        host="localhost",
        user="root",
        password="Root512!",
        database=dbname
)
       
       
       cursor = mydb.cursor()
       cursor.execute("SHOW TABLES")
       #tämä sql lause hakee valitun tietokannan koon
       sizequery="SELECT table_schema '%(dbname)s', SUM(data_length + index_length) / 1024 FROM information_schema.TABLES GROUP BY table_schema LIMIT 1"
       #myresult = cursor.fetchall()
     
       for x in cursor:
            #x:n tietotyyppi on tuple, joten join metodin avulla muutetaan se merkkijonoksi
            #että voidaan käyttää replace metodia poistamaan ylim. merkit.
            result = "".join(x)
            finalres=result.replace("(","").replace(")","")
            tables.append(finalres)
       cursor.execute(sizequery)
       for dbsize in cursor:
            print(dbsize[1])
       lng=len(tables)

      
       return render_template("mysql.html",tables=tables,dbname=dbname,lng=lng,dbsize=dbsize[1])

@mysqlScripts.route("/runScript",methods=['POST','GET'])
def runSQLScript():
     sqldata=[]
     script = request.form.get('querytext')
     print(script)
     print("db "+dbname)
     mydb = mysql.connector.connect(
       
        host="localhost",
        user="root",
        password="Root512!",
        database=dbname
)
     cursor=mydb.cursor()
     cursor.execute(script)
     for x in cursor:
          print(x)
          sqldata.append(x)
     

     return render_template("mysql.html",sqldata=sqldata,script=script)

@mysqlScripts.route("/mysqlTable/<dbname>",methods=['POST','GET'])
def readTableData(dbname):
      tablesShown=True
      data=[]
      ids=[]
      sqltable=request.form.get("selectedTable")
      #dbName=request.form.get("dbname")
      mydb = mysql.connector.connect(
       
        host="localhost",
        user="root",
        password="Root512!",
        database=dbname
)
    

      cursor = mydb.cursor()
      cursor.execute("SELECT * FROM "+sqltable)
      #sql taulujen sarakkeiden nimet
      numfields = len(cursor.description)
      fieldnames = [i[0] for i in cursor.description]
      #listan muunto merkkijonoksi, että voidaan näyttää kaikki samalla rivillä html:n puolella.
      finalHeaders = " ".join(fieldnames)
      myresult = cursor.fetchall()

      for x in myresult:
        print(x)
        data.append(x)
      

      return render_template("mysql.html",data=data,finalHeaders=finalHeaders,numfields=numfields,fieldnames=fieldnames,tablesShown=tablesShown)