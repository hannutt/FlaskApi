from flask import Blueprint, render_template, request
import pyodbc,os
from dotenv import load_dotenv
azurePsw=os.getenv('azurePsw')
azureUser=os.getenv('azureUser')
azureSrv=os.getenv('azureSrv')
azureDB=os.getenv("azureDB")
azureScripts = Blueprint('azureScripts',__name__,static_folder='static',template_folder='templates')

@azureScripts.route('/azure',methods=['POST','GET'])
def azureStart():
    data=[]
    connectionString = pyodbc.connect('DRIVER={SQL Server};'
                      f'SERVER={azureSrv};'
                      f'DATABASE={azureDB}; UID={azureUser}; PWD={azurePsw};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = connectionString.cursor()
    query="select * from cars"
    cursor.execute(query)
    records = cursor.fetchall()
    for r in records:
        data.append(r)
    return render_template("azure.html",data=data)
