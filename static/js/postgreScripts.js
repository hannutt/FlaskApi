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