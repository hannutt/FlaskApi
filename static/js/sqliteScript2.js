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

function getInputValue() {
    var input=document.getElementById("srcFolder").value
    if (input!=='')
    {
        document.getElementById("searchFolderBtn").hidden=false
    }
    console.log(input)
    document.getElementById("searchFolderBtn").textContent="Search from "+input
}

function showSearchOptions() {
    var cb=document.getElementById("searchFolderCB")
    if (cb.checked==true)
    {
        var btn=document.getElementById("searchFolderBtn")
        document.getElementById("srcFolder").hidden=false
        document.getElementById("srcFolder").placeholder="ENTER PATH"
        document.getElementById("searchFolderBtn").hidden=false
        
    }
    else {
        document.getElementById("srcFolder").hidden=true
        document.getElementById("searhcFolderBtn").hidden=true

    }
}

