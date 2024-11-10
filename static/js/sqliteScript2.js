var columns=0
function createNewColumn() {
   
    document.getElementById("columns").innerText=columns
    var cb=document.getElementById("createColumn") 
    if (cb.checked==true)
    {
        document.getElementById("columnCreate").hidden=false
        
    }
    else{
        document.getElementById("columnCreate").hidden=true

    }

}