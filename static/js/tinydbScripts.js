
function GoTinyDB(cb) {
    if (cb) {
        document.getElementById("tinydbBtn").click()
    }
}

function showCreate(cb) {
    console.log(cb.id)
    if (cb) {
        document.getElementById("createDiv").hidden=false
        document.getElementById("fileName").value=".json"
    }
    if (cb.checked==false) {
        document.getElementById("createDiv").hidden=true

    }
}
function showFind(cb)
{
    if (cb) {
        document.getElementById("findFiles").hidden=false

    }
    if (cb.checked==false)
    {
        document.getElementById("findFiles").hidden=true
    }

}