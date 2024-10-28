function runSqlite() {
    var cb = document.getElementById("sqlite")
    if (cb.checked==true)
    {
        document.getElementById('restriction').hidden=false
        document.getElementById('sqliteShow').hidden=false
        document.getElementById('dbPath').hidden=false

    }
    else {
        document.getElementById('restriction').hidden=true
        document.getElementById('sqliteShow').hidden=true
        document.getElementById('dbPath').hidden=true
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

