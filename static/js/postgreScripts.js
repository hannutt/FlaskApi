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
    var cb=document.getElementById("postgreQueryCB" ).checked
    if (cb) {
        document.getElementById("writePostgre").hidden=false
    }
    else{
        document.getElementById("writePostgre").hidden=true
    }
}