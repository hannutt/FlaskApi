
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

function cancelCrud() {
    document.getElementById("selectedfile").value = ""
    document.getElementById("selectedfile").hidden=true
    document.getElementById("saveNshow").hidden = true
    document.getElementById("cancel").hidden = true
}

