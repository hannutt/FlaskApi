var ReloadPage=false
function runSqlite() {
    var cb = document.getElementById("sqlite")
    if (cb.checked==true)
    {  
        document.getElementById("choice").hidden=false
        /*
        document.getElementById("sqliteStart").hidden=false
        document.getElementById("sqliteStart2").hidden=false*/
    }
    else {
        document.getElementById("choice").hidden=true
        document.getElementById("sqliteTable").hidden=true
        /*
        document.getElementById("sqliteStart").hidden=true
        document.getElementById("sqliteStart2").hidden=true*/

    }
}

function selectionSqlite(dbtable) {
    var selectedTable= dbtable.options[dbtable.selectedIndex].text
    rep=selectedTable.replace("(","").replace(")","").replace(",","").replace("'","").replace("'","")
    document.getElementById("selectedTable").value=rep
    document.getElementById("selectedTable2").value=rep
    document.getElementById("selfWriteBtn").hidden=false
    document.getElementById("selfWriteBtn").textContent="Access "+rep
    //document.getElementById("dataBname").value=sessionStorage.getItem("dbname")
  
  
    
}

function showQueryBox() {
    var cb = document.getElementById("queryCB")
    if (cb.checked==true)
    {
        
        document.getElementById("sqliteQuery").hidden=false
        document.getElementById("showTableBtn").hidden=true
        document.getElementById("runsqlitequery").hidden=false

    }
    else {
        document.getElementById("sqliteQuery").hidden=true
        document.getElementById("showTableBtn").hidden=false
        document.getElementById("runsqlitequery").hidden=true
    }
   
}
//funktio näyttää create table ja backup database checkboksit, jos ehto täyttyy.
function backUp(inputVal) {
   
    if (inputVal!=null)
    {
        document.getElementById("backup").hidden=false
        document.getElementById("backupLbl").hidden=false
        document.getElementById("createTableCB").hidden=false
        document.getElementById("createTableLbl").hidden=false
        
    }
}
function clearBackup(val) {
    if (val=='')
    {
        document.getElementById("backup").hidden=true
        document.getElementById("backupLbl").hidden=true
        document.getElementById("createTableCB").hidden=true
        document.getElementById("createTableLbl").hidden=true
    }
}

function startBackup() {
    var cb = document.getElementById("backup").checked
    if (cb===true)
    {  //simuloitu klikkaus buttonille
        document.getElementById("backupBtn").click()

    }
    
}
//funktio hakee amountin arvon, joka kertoo montako inputtia tarvitaan
//inputit luodaan for silmukassa createElementin avulla ja sijoitetaan
//createNew diviin appendChild metodin avulla
function createSqlFields() {
    //haetaan kaikki elementin sisältämä teksti
    var columnNames=document.getElementsByClassName("columnNames")
    //talletetaan se toiseen muuttujaan, että voidaan käyttää split metodia
    var cols = columnNames[0].innerHTML
    var colsRep = cols.replace("[","").replace("]","")
    //splitnames on taulukko ja muuttujan teksti katkaistaan aina pilkun kohdalta, jolloin
    //jokainen sana saadaan omaksi alkiokseen listaan
    var splitNames = colsRep.split(",")
    
    var amount = document.getElementById("colAmount").innerHTML
    console.log(amount)
    var amountInt = parseInt(amount)
    var cb= document.getElementById("createRecord")
    if (cb.checked===true)
    {
        document.getElementById("columnNames").hidden=false
        //vähennetään luotavista input-kentistä yksi, eli id kenttä.
        
       
        for (var i=0;i<amountInt;i++)
        {
           var input= document.createElement("INPUT")
           document.getElementById("createNew").appendChild(input)
           input.id=i
           input.name=i
           //placeholderin arvoksi tulee sarakkeiden nimet
           input.placeholder=splitNames[i]
        }
        var createBtn = document.createElement("button")
        createBtn.textContent="Create record"
        createBtn.setAttribute("class","runBtn")
        document.getElementById("createNew").appendChild(createBtn)
    }
    else {
        document.getElementById("createNew").innerHTML=""
        document.getElementById("columnNames").hidden=true
    }
    

}

function createSqlEditFields() {
    var amount = document.getElementById("colAmount").innerHTML
    console.log(amount)
    var amountInt = parseInt(amount)
    console.log(amountInt)
    var cb= document.getElementById("editSqlRecord")
    var editBtn=document.createElement("button")
    editBtn.textContent="Edit record"
    editBtn.setAttribute("class","runBtn")
    if (cb.checked===true)
    {   
        for (var i=0;i<amountInt;i++)
        {
           var input= document.createElement("INPUT")
           document.getElementById("editSqlite").appendChild(input)
           input.id=i
           input.name=i
          
        }
        
        
       
        document.getElementById("editSqlite").appendChild(editBtn)
    }
    else {
        document.getElementById("editSqlite").innerHTML=""     
    }
}
function createSqliteTable() {
    var cb= document.getElementById("createTableCB")
    
    if (cb.checked==true)
    {
        
        var t = document.createElement("input")
        var b = document.createElement("button")
        b.textContent="Create table"
        t.name="createArea"
        t.placeholder="TABLE NAME"
        document.getElementById("texta").appendChild(t)
        document.getElementById("texta").appendChild(b)
    }
    else{
        document.getElementById("texta").innerHTML=''
    }
}
function tableColumnsDiv() {
    var cb=document.getElementById("tableColumnsCB").checked
    if (cb===true)
    {
        document.getElementById("tableColumnsDiv").hidden=false
    }
    else{
        document.getElementById("tableColumnsDiv").hidden=true

    }
}
var inputsClicks=0
//funktion suoritus lisää aina yhden html-inputin / klikkaus
function createInputsSqlite() {

    inputsClicks=inputsClicks+1
    var input =document.createElement("INPUT")
    input.id=inputsClicks
    document.getElementById("tableColumnsDiv").appendChild(input)
    document.getElementById("columns").value=inputsClicks


}

