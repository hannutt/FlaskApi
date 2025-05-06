//elementit luodaan tässä mutta niitä käytetään
//vasta createatlas funktiossa. näin piilotus/näyttö saadaan toimiaan klikkauksella oikein.

var nameOfDb = document.createElement("INPUT")
nameOfDb.id = "nameOfDb"
//lisätään name attribuutti
nameOfDb.setAttribute('name', 'nameOfDb')
var DBname = document.createElement("INPUT")

var select = document.createElement("BUTTON")
var conn = document.createElement("BUTTON")
linebreak = document.createElement("br");
var selected = document.createElement("p")
selected.setAttribute('id', 'selectionForDB')
select.textContent = 'Select'
DBname.placeholder = 'Database name'


var mysqlBtn = document.createElement("BUTTON")
mysqlBtn.id="showsql"
mysqlBtn.textContent = "Show"


DBname.name = 'dbname'
//collectionName.name='collection'
function createAtlas() {
  var atlasCB = document.getElementById("atlas")
  if (atlasCB.checked == true) {
    var atlas = document.getElementById("atlasDB")

    //append childillä lisätään atlas form diviin uusi elementti, eli tässä
    //tapauksessa nameofdb input kenttä
    document.getElementById("atlasForm").appendChild(nameOfDb)
    document.getElementById("atlasForm").appendChild(select)


    DBname.setAttribute('name', 'dbname')

    document.getElementById("atlasForm").appendChild(linebreak)

    atlas.hidden = false
    document.getElementById("atlasForm").appendChild(atlas)

    document.getElementById("atlasForm").appendChild(select)
    //document.getElementById("atlasForm").appendChild(selected)
    document.getElementById("atlasForm").hidden = false

  }
  if (atlasCB.checked == false) {
    document.getElementById("atlasForm").hidden = true
  }
}

function createMysql() {
  var mysqlCB = document.getElementById("mysql")
  if (mysqlCB.checked == true) {
    document.getElementById("mysqlForm").hidden = false
    // document.getElementById("mysqlForm").appendChild(mysqlPath)
    document.getElementById("mysqlForm").appendChild(mysqlBtn)

  }
  if (mysqlCB.checked==false) {
    document.getElementById("mysqlForm").hidden = true
    mysqlBtn.remove()
  }

}





function createEdit() {

  var fieldsTotal = document.getElementById("keystotal").innerHTML
  var fieldsTotalInt = Number(fieldsTotal)
  var cb = document.getElementById("edit")
  //talletetaan kaikki databasefield class tagin sisältämät arvot
  var DBfields = document.getElementsByClassName("databaseFields")
  var DBfieldsList = DBfields[0].innerHTML.split(",")

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
      inpField.name = i

      inpField.setAttribute("type", "text");
      //document.body.appendChild(inpField);
      document.getElementById("editing").appendChild(editBtn)
      document.getElementById("editing").appendChild(inpField)

      //tietokannan kenttien nimet on lähetetty python listana html-sivulle, josta ne on puolestaan
      //talletettu javascript listaan. i-silmukkamuuttujan avulla saadaan asetettuja oikea placeholder
      //oikeaan input-kenttään
      document.getElementById(i).placeholder = DBfieldsList[i]

    }


  } else {
    document.getElementById("editing").innerHTML = ""
  }
}

function createAddFields() {
  var cb = document.getElementById("add").checked
  //kenttien lukumäärä eli montako input kenttää tarvitaan
  var fieldsTotal = document.getElementById("keystotal").innerHTML
  var fieldsTotalInt = Number(fieldsTotal)
  fieldsTotalInt = fieldsTotalInt - 1
  var DBfields = document.getElementsByClassName("databaseFields")
  var DBfieldsList = DBfields[0].innerHTML.split(",")
  if (cb === true) {
    for (var i = 1; i <= fieldsTotalInt; i++) {
      var inpField = document.createElement("INPUT");
      var addBtn = document.createElement("button")
      addBtn.textContent = "Add"
      //annetaan id silmukkamuuttujan kautta eli id:t ovat 0,1,2,3 jne
      inpField.id = i
      inpField.name = i

      inpField.setAttribute("type", "text");
      //document.body.appendChild(inpField);
      //document.getElementById("editing").appendChild(editBtn)
      document.getElementById("addNew").appendChild(inpField)


      //tietokannan kenttien nimet on lähetetty python listana html-sivulle, josta ne on puolestaan
      //talletettu javascript listaan. i-silmukkamuuttujan avulla saadaan asetettuja oikea placeholder
      //oikeaan input-kenttään
      document.getElementById(i).placeholder = DBfieldsList[i]
    }
    document.getElementById("addNew").appendChild(addBtn)

  } else {
    document.getElementById("addNew").innerHTML = ""
  }

}