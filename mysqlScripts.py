import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request
import mysql.connector
from variables import Variables

mysqlScripts = Blueprint('mysqlScripts',__name__,static_folder='static',template_folder='templates')
sqlDB=False
tablesShown=False

var = Variables()



@mysqlScripts.route("/mysql",methods=['POST','GET'])

def readSelectedSql():
       tables=[]
       sqlDB=True
       
       var.databaseName=request.form.get('selectedSQL')
       var.MySqldbConnector.database=var.databaseName       
       cursor = var.MySqldbConnector.cursor()
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

      
       return render_template("mysql.html",tables=tables,dbname=var.databaseName,lng=lng,dbsize=dbsize[1],sqlDB=sqlDB)

@mysqlScripts.route("/runScript",methods=['POST','GET'])
def runSQLScript():
     tablesShown=True
     sqldata=[]
     script = request.form.get('querytext')

     cursor=var.MySqldbConnector.cursor()
     if script.startswith("update"):
          cursor.execute(script)
          #commit eli toteutetaan muutos
          var.MySqldbConnector.commit()
          #insert eli uuden tietueen lisäys
     elif script.startswith("insert"):
          cursor.execute(script)
          #commit eli toteutetaan muutos
          var.MySqldbConnector.commit()

     else:
          cursor.execute(script)
          for x in cursor:
               sqldata.append(x)
     

     return render_template("mysql.html",sqldata=sqldata,script=script,tablesShown=tablesShown,sqltable=var.sqltable)

@mysqlScripts.route("/mysqlTable/<dbname>",methods=['POST','GET'])
def readTableData(dbname):
      i=0
      tablesShown=True
      data=[]
      ids=[]
      var.sqltable=request.form.get("selectedTable")
      var.MySqldbConnector.database=dbname
      cursor = var.MySqldbConnector.cursor()
      cursor.execute("SELECT * FROM "+var.sqltable)
      #sql taulujen sarakkeiden nimet
      numfields = len(cursor.description)
      fieldnames = [i[0] for i in cursor.description]
      #listan muunto merkkijonoksi, että voidaan näyttää kaikki samalla rivillä html:n puolella.
      finalHeaders = " ".join(fieldnames)
      myresult = cursor.fetchall()

      for x in myresult:
        print(x)
        data.append(x)
        i=i+1
      return render_template("mysql.html",data=data,finalHeaders=finalHeaders,numfields=numfields,fieldnames=fieldnames,tablesShown=tablesShown,i=i,sqltable=var.sqltable)