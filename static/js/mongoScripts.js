function createNewCollection() {
    var cb=document.getElementById("newCollection")
    if (cb.checked==true) {
        document.getElementById("collectionName").hidden=false
        document.getElementById("createBtn").hidden=false
        var mongodb = document.getElementById("selecDB").value
        document.getElementById("mongoDBname").value=mongodb
    }
    else {
        document.getElementById("collectionName").hidden=true
        document.getElementById("createBtn").hidden=true
        document.getElementById("mongoDBname").value=""
        
    }

}

function deleteCollection() {
    var cb=document.getElementById("dropCol")
    if (cb.checked==true) {
        document.getElementById("colToDelete").hidden=false
        document.getElementById("colDeleteBtn").hidden=false
        var mongodb = document.getElementById("selecDB").value
        document.getElementById("DB").value=mongodb

    }
    else {
        document.getElementById("colToDelete").value=""
        document.getElementById("colToDelete").hidden=true
        document.getElementById("colDeleteBtn").hidden=true

    }
}