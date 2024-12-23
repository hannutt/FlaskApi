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
        document.getElementById("options").hidden=false
        /*
        document.getElementById("srcRestLbl").hidden=false
        document.getElementById("srcFolder").hidden=false
        document.getElementById("srcFolder").placeholder="ENTER PATH"
        document.getElementById("searchFolderBtn").hidden=false
        document.getElementById("srcRestLbl").hidden=false
        document.getElementById("numberofsearch").hidden=false*/
        
    }
    if (cb.checked==false) {
        document.getElementById("options").hidden=true
        /*
        document.getElementById("srcFolder").hidden=true
        document.getElementById("searchFolderBtn").hidden=true
        document.getElementById("srcRestLbl").hidden=true
        document.getElementById("numberofsearch").hidden=true*/

    }
}
var l =[]
function directoriesToAvoid() {
    
    var dir = document.getElementById("avoidInput").value
    document.getElementById("avoiding").value+=dir+','
    document.getElementById("avoidList").innerText+=dir+","
    l.push(dir)
    document.getElementById("avoidInput").value=''
    console.log(l)

}
function checkFields(numoffiles,dir) {
    if (numoffiles!==null && dir!==null)
    {
        document.getElementById("searchFolderBtn").disabled=false
    }
   

}
function insertTableName() {
    var tablename=document.getElementById("tname").value
    
    document.getElementById("exportBtn").textContent="Export "+tablename+" table to csv"
}

function getSeparatorChar(char) {
    var c = document.getElementById("sep").value = char.options[char.selectedIndex].text
    document.getElementById("sepChar").value=c

}