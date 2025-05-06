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

    var totalrecords = document.getElementById("totalsql").innerText
    var recordsInt = Number(totalrecords)
    var table = document.getElementById("dbTable")
    var marks = [")", "(", ","]
    var originalText = table.innerText
    var prettytext = originalText
    for (var i = 0; i < recordsInt; i++) {

        //tämän avulla teksti voidaan palauttaa alkuperäiseen muotoon
        table.setAttribute('data-orig', originalText);
        for (j = 0; j < marks.length; j++) {

            prettytext = prettytext.replace(marks[j], "")
        }

        document.getElementById("dbTable").innerText = prettytext
    }
}




//tarkistetaan h2 elementin sisältämä teksti ja sen perusteella näytetään oikeat labelit ja cb:t
function checkDbType() {
    var dbtype = document.getElementById("dbHeader").innerText
    console.log(dbtype)
    if (dbtype.includes("SQL")) {
        document.getElementById("tableCBLbltxt").hidden = true
        document.getElementById("prettytxtCB").hidden = true

    }
    else if (dbtype.includes("MongoDB")) {
        document.getElementById("tableCBLbltxt2").hidden = true
        document.getElementById("prettytxtCBSql").hidden = true

    }
}
//funktio lisää sulkumerkit aina, jos tekstistä löydetään = merkki
function blockspg() {
    var txt = document.getElementById("writePostgre").value
    if (txt.includes("=")) {
        var txtBlock = txt + "('')"
        document.getElementById("writePostgre").value = txtBlock

    }
}