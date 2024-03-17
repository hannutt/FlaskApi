
from http.client import InvalidURL
from flask import Flask, request, json, Response,jsonify,render_template
from flask_pymongo import PyMongo,MongoClient


app = Flask(__name__)


@app.route("/")


def showIndex():
     dbsList = []
     dbs=MongoClient().list_database_names()
     client = MongoClient('localhost', 27017)
     mydatabase = client.quizDB
     collections = mydatabase.list_collection_names()
     print(collections)
     for i in dbs:
          dbsList.append(i)
    
     return render_template('index.html',dbsList=dbsList)

@app.route('/read-form', methods=['POST']) 
def read_form():
    l=[]
    #client = MongoClient('localhost', 27017)
    selectedDB = request.form.get('selectedDB')
    #DbNameOnly = request.form.get('DBname')
    #mydatabase = client.DbNameOnly
    #collections = mydatabase.list_collection_names()
    #print(collections)
    #collections=mydatabase.list_collection_names()
    #collections = mydatabase.list_collection_names()
    #print(collections)
   
    
    #print(selectedDB)

    app.config['MONGO_URI']=selectedDB
    global mongodb
    mongodb=PyMongo(app).db
    cols=mongodb.list_collection_names()
    # Get the form data as Python ImmutableDict datatype  
    data = request.form
    
    
    return render_template('selectCol.html',cols=cols)


@app.route("/api/all",methods=['GET'])
def read():
    try:

        item=[]
        results = mongodb.results.find({},)
        #keyLen=len(res.keys())
        #print("keylen: ",keyLen)
        for res in results:
         
            first_key = list(res.keys())[0]
            sec_key = list(res.keys())[1]
            third_key= list(res.keys())[2]

            items={

                "id":str(res[first_key]),
                "name":str(res[sec_key]),
                "points":res[third_key],
            }
            item.append(items)
           
        
        return jsonify(item)
    except:InvalidURL
    return "SELECT DATABASE!"
#tässä haetaan nimen perusteella mongokannasta <name> on parametri johon kirjoitetaan haetun käyttäjän nimi, esim.
#http://127.0.0.1:5000/findName/keijo
@app.route("/findName/<name>")
def searchByname(name):
    user = mongodb.results.find_one({"name": name})
    #jos nimi löytyy, items sanakirja-olioon talletetaan user eli löydetyn nimen id,nimi ja pisteet
    if user:
            userinfo={

            "id":str(user['_id']),
            "name":str(user['name']),
            "points":user['points'],
        }
     
    return jsonify({'userinfo':userinfo})

@app.route('/deleteName/<name>')
def delByname(name):
     user = mongodb.results.find_one({"name": name})
     if user:
          mongodb.results.delete_one({"name":name})
          return 'DELETED'
     
    
if __name__ == '__main__':
    app.run(debug=True)






