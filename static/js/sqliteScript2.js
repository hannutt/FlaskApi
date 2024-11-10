function createNewColumn() {
    var cb=document.getElementById("createColumn").checked 
    if (cb==true)
    {
        document.getElementById("columnCreate").hidden=false
    }
    else{
        document.getElementById("columnCreate").hidden=true

    }

}