
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
        document.getElementById("findFiles").hidden = false
        document.getElementById("jsontable").hidden = false



    }
    if (cbShow.checked == false) {
        document.getElementById("findFiles").hidden = true
        document.getElementById("jsontable").hidden = true
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
        document.getElementById("datafield").hidden = true
        document.getElementById("data").hidden = true
        document.getElementById("txtmultiple").hidden=false
        document.getElementById("saveMultiple").hidden=false
        document.getElementById("saveSingle").hidden=true
    }
    if (cb.checked==false) {
        document.getElementById("datafield").hidden = false
        document.getElementById("data").hidden = false
        document.getElementById("txtmultiple").hidden=true
        document.getElementById("saveMultiple").hidden=true
        document.getElementById("saveSingle").hidden=false

    }

}
