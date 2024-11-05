function runSqlite() {
    var cb = document.getElementById("sqlite")
    if (cb.checked==true)
    {  

        document.getElementById('restrictionLbl').hidden=false
        document.getElementById('restriction').hidden=false
        document.getElementById('sqliteShow').hidden=false
        document.getElementById('dbPath').hidden=false
        document.getElementById('accessBtn').hidden=false

    }
    else {
        document.getElementById('restrictionLbl').hidden=true
        document.getElementById('restriction').hidden=true
        document.getElementById('sqliteShow').hidden=true
        document.getElementById('dbPath').hidden=true
        document.getElementById('accessBtn').hidden=true
        //document.getElementById('sqliteFile').hidden=true

    }
}

function selectionSqlite(dbtable) {
    var selectedTable= dbtable.options[dbtable.selectedIndex].text
    rep=selectedTable.replace("(","").replace(")","").replace(",","").replace("'","").replace("'","")
    console.log(rep)
    document.getElementById("selectedTable").value=rep
    document.getElementById("selectedTable2").value=rep
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

function backUp(inputVal) {
   
    if (inputVal!=null)
    {
        document.getElementById("backup").hidden=false
        document.getElementById("backupLbl").hidden=false
    }
}
function clearBackup(val) {
    if (val=='')
    {
        document.getElementById("backup").hidden=true
        document.getElementById("backupLbl").hidden=true

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
    var amount = document.getElementById("colAmount").innerHTML
    console.log(amount)
    var amountInt = parseInt(amount)
    var cb= document.getElementById("createRecord")
    if (cb.checked===true)
    {
        document.getElementById("columnNames").hidden=false
       
        for (var i=0;i<amountInt;i++)
        {
           var input= document.createElement("INPUT")
           document.getElementById("createNew").appendChild(input)
           input.id=i
           input.name=i
        }
        var createBtn = document.createElement("button")
        createBtn.textContent="Create record"
        document.getElementById("createNew").appendChild(createBtn)
    }
    else {
        document.getElementById("createNew").innerHTML=""
    }
    

}
