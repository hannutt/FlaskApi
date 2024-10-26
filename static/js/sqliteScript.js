function runSqlite() {
    var cb = document.getElementById("sqlite")
    if (cb.checked==true)
    {
        document.getElementById('restriction').hidden=false
        document.getElementById('sqliteShow').hidden=false

    }
    else {
        document.getElementById('restriction').hidden=true
        document.getElementById('sqliteShow').hidden=true

    }
}