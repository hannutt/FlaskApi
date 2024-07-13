//elementit luodaan tässä mutta niitä käytetään
//vasta createatlas funktiossa. näin piilotus/näyttö saadaan toimiaan klikkauksella oikein.
//var uriInput=document.createElement("INPUT")
//var pswInput=document.createElement("INPUT")
var nameOfDb=document.createElement("INPUT")
nameOfDb.id="nameOfDb"
nameOfDb.setAttribute('name','nameOfDb')
var DBname=document.createElement("INPUT")
//var collectionName=document.createElement("INPUT")
var conn = document.createElement("BUTTON")
linebreak = document.createElement("br");
var selected = document.createElement("p")
selected.setAttribute('id','selectionForDB')
conn.textContent='Select'
//uriInput.placeholder="Atlas URI"
//pswInput.placeholder="Password"
//userInput.placeholder="Username"
DBname.placeholder='Database name'
//collectionName.placeholder='Collection name'
uriInput.name='uri'

DBname.name='dbname'
//collectionName.name='collection'
function createAtlas() {
  var atlasCB=document.getElementById("atlas")
  if (atlasCB.checked==true)
  {
    var atlas = document.getElementById("atlasDB")
    
   
    document.getElementById("atlasForm").appendChild(nameOfDb)
    document.getElementById("atlasForm").appendChild(conn)
    //document.getElementById("atlasForm").appendChild(pswInput)
   // pswInput.setAttribute('name','psw')
    //userInput.setAttribute('name','user')
    DBname.setAttribute('name','dbname')
    //collectionName.setAttribute('name','colname')
    //document.getElementById("atlasForm").appendChild(userInput)
    
    document.getElementById("atlasForm").appendChild(linebreak)

    atlas.hidden=false
    document.getElementById("atlasForm").appendChild(atlas)
    //document.getElementById("atlasForm").appendChild(DBname)
    //document.getElementById("atlasForm").appendChild(collectionName)
    document.getElementById("atlasForm").appendChild(conn)
    document.getElementById("atlasForm").appendChild(selected)
    document.getElementById("atlasForm").hidden=false
    
  }
  else if(atlasCB.checked==false){
    document.getElementById("atlasForm").hidden=true
  }
}



function createEdit() {

    var fieldsTotal = document.getElementById("keystotal").innerHTML
    var fieldsTotalInt = Number(fieldsTotal)
    console.log(typeof fieldsTotalInt)
    var cb = document.getElementById("edit")
    var addCB = document.getElementById("add")
    
    var editBtn = document.createElement("BUTTON")
    editBtn.id = "editBtn"
    editBtn.textContent = "Edit"
    //jos checkbox on klikattu, luodaan edit painike, muussa tapauksessa tuhotaan painike
    if (cb.checked == true) {
      //document.body.appendChild(editBtn)
      
      //silmukan avulla luodaan yhtä monta input-kenttää kuin mitä kenttiä on kokoelmassakin
      for (var i = 0; i < fieldsTotalInt; i++) {
        var inpField = document.createElement("INPUT");
        //annetaan id silmukkamuuttujan kautta eli id:t ovat 0,1,2,3 jne
        inpField.id = i
        inpField.name= i
        inpField.setAttribute("type", "text");
        //document.body.appendChild(inpField);
        document.getElementById("editing").appendChild(editBtn)
        document.getElementById("editing").appendChild(inpField)

        //tietokannan kenttien nimet on lähetetty python listana html-sivulle, josta ne on puolestaan
        //talletettu javascript listaan. i-silmukkamuuttujan avulla saadaan asetettuja oikea placeholder
        //oikeaan input-kenttään
        document.getElementById(i).value = valuesList[i]
      }

    }
    else if(addCB.checked==true)
    {
      var addBtn = document.createElement("BUTTON")
      addBtn.id = "Add"
      editBtn.textContent = "Add"
      fieldTotal=document.createElement("INPUT")
      fieldTotal.id="fieldtotal"
      fieldTotal.name="fieldtotal"
      
      //silmukan avulla luodaan yhtä monta input-kenttää kuin mitä kenttiä on kokoelmassakin
      for (var i = 1; i < fieldsTotalInt; i++) {
        var inpField = document.createElement("INPUT");
        var fieldValues = document.createElement("INPUT");

        //annetaan id silmukkamuuttujan kautta eli id:t ovat 0,1,2,3 jne
        inpField.id = i
        inpField.name= i
        fieldValues.name="field"+i
        fieldValues.id="field"+i
        fieldValues.hidden=true
        fieldValues.setAttribute("type","text")
        inpField.setAttribute("type", "text");
       
        
        //luodut syötentät ja painkkeet sijoitetaan addNew diviin
        document.getElementById("addNew").appendChild(inpField)
        document.getElementById("addNew").appendChild(editBtn)
        document.getElementById("addNew").appendChild(fieldValues)
        document.getElementById("addNew").appendChild(atlas)
        //tietokannan kenttien nimet on lähetetty python listana html-sivulle, josta ne on puolestaan
        //talletettu javascript listaan. i-silmukkamuuttujan avulla saadaan asetettuja oikea placeholder
        //oikeaan input-kenttään
        document.getElementById(i).placeholder = valuesList[i]
        document.getElementById("field"+i).value=valuesList[i]
        
        document.getElementById("addNew").appendChild(fieldTotal)
        document.getElementById("fieldtotal").value=fieldsTotalInt

      }
      
      
    }
    else {
      document.getElementById("editBtn").remove()
      //input-kenttien tuhoamisessa käytetään myös silmukkaa ja fieldstotal muuttujaa
      for (var i = 0; i < fieldsTotalInt; i++) {
        document.getElementById(i).remove()

      }
    }

  }