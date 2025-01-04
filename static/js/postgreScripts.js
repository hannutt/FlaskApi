function goPostgrePage() {
    var cb = document.getElementById("postgreCB").checked
    if (cb) {
        document.getElementById("gobtn").click()

    }
}

function getPostgreDB(database) {
    var sel = document.getElementById("postgre").value = database.options[database.selectedIndex].text
    var cleartext = sel.replace("(", "").replace(")", "").replace("'", "").replace("'", "").replace(",", "")
    document.getElementById("selectedPostgre").value = cleartext

}
function getPostgeTable(table) {
    var sel = document.getElementById("postgreTables").value = table.options[table.selectedIndex].text
    var cleartext = sel.replace("(", "").replace(")", "").replace("'", "").replace("'", "").replace(",", "")
    document.getElementById("postgreTable").value = cleartext
    


}
function writePostgre() {
    var cb = document.getElementById("postgreQueryCB").checked
    if (cb) {
        document.getElementById("writePostgre").hidden = false
    }
    else {
        document.getElementById("writePostgre").hidden = true
    }
}

function removeExtraMarks() {

    var originalText = document.getElementById("dbSize").innerText
    //käydään for-silmukalla läpi originaltext muuttuja ja marks lista
    //silmukka poistaa listalla olevat merkit lopputuloksesta
    var marks = ["(", ")", ",","'","'"]
    for (var i = 0; i < marks.length; i++) {
        originalText= originalText.replace(marks[i], "")
    }
    document.getElementById("dbSize").innerText = ""
    document.getElementById("dbSize").innerText = originalText
}

function removeMarksMySql() {
    var loopLast=document.getElementById("loopLast").innerText
    var looplastInt=parseInt(loopLast)
    var cleardata=""
    for (var i=1;i<=looplastInt;i++)
    {
        //silmukassa haetaan jokainen data+numero idllä nimetty td elementti eli elementit
        //käydään yksitellen läpi ja niistä poistetaan ylim merkit
        var data =document.getElementById("data"+i).innerText
        //elementistä poistetaan replacen avulla ylim. merkit
        cleardata=data.replace("(","").replace(")","").replace("'","").replace("'","")
        //suodatettu teksti lisätään data+numero td elementteihin
        document.getElementById("data"+i).innerText=cleardata   
    } 
}

//tarkistetaan h2 elementin sisältämä teksti ja sen perusteella näytetään oikeat labelit ja cb:t
function checkDbType() {
    var dbtype = document.getElementById("dbHeader").innerText
    console.log(dbtype)
    if (dbtype.includes("SQL")) {
        document.getElementById("tableCBLbltxt").hidden=true
        document.getElementById("prettytxtCB").hidden=true

    }
    else if (dbtype.includes("MongoDB")){
        document.getElementById("tableCBLbltxt2").hidden=true
        document.getElementById("prettytxtCBSql").hidden=true

    }
}
   //funktio lisää sulkumerkit aina, jos tekstistä löydetään = merkki
   function blockspg() {
    var txt = document.getElementById("writePostgre").value
    if (txt.includes("=")) {
      var txtBlock=txt+"()"
      document.getElementById("writePostgre").value=txtBlock

    }
  }