
function GoTinyDB(cb) {
    if (cb) {
        document.getElementById("tinydbBtn").click()
    }
}

function showCreate(cb) {
    console.log(cb.id)
    if (cb) {
        document.getElementById("createDiv").hidden = false
        document.getElementById("fileName").value = ".json"
    }
    if (cb.checked == false) {
        document.getElementById("createDiv").hidden = true

    }
}

function showFind(cbShow) {


    if (cbShow.checked == true) {
        document.getElementById("findFilesSpan").hidden = false
        



    }
    if (cbShow.checked == false) {
        document.getElementById("findFilesSpan").hidden = true
    
    }

}
function dataAdded() {
    document.getElementById("dataAdded").innerText = "DATA ADDED!"
    setTimeout(function () {
        document.getElementById("dataAdded").innerText = " ";
    }, 5000);
}

function addMultiple(cb) {
    if (cb) {
        document.getElementById("dataFields").hidden=true
        document.getElementById("multipleSpan").hidden=false
        document.getElementById("saveSingle").hidden=true
    }
    if (cb.checked==false) {
        document.getElementById("dataFields").hidden=false
        document.getElementById("multipleSpan").hidden=true
        document.getElementById("saveSingle").hidden=false

    }

}
var idnum=1
function createNewLine() {
    var input = document.createElement("input");
    input.id=idnum
    document.getElementById("newlines").appendChild(input);
    idnum=idnum+1
}
function showDocId(cb) {
    if (cb) {
        document.getElementById("documentId").hidden=false

    }
    if (cb.checked==false)
    {
        document.getElementById("documentId").hidden=true

    }

}