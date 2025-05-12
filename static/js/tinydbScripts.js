
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

function writingAssistant(ev,cb) {
 

    if (cb.checked==true&&ev.keyCode==32)
    {
    
        var txt=document.getElementById("txtmultiple").value+=":"
        //split ja join poistaa välilyönnit esim product : muuttuu muotoon product:
        var txtNowhiteSpace=txt.split(" ").join("")
        document.getElementById("txtmultiple").value=""
        
        document.getElementById("txtmultiple").value=txtNowhiteSpace
    }

}

