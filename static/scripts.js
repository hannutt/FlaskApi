var clicks=0
function stats()
{
    clicks=clicks+1
    if (clicks % 1 == 0)
    {
        document.getElementById("stats").hidden=false
        document.getElementById("chart").hidden=false
        document.getElementById("statsBtn").textContent='Hide'
    }
    if (clicks % 2 ==0)
    {
        document.getElementById("stats").hidden=true
        document.getElementById("chart").hidden=true
        document.getElementById("statsBtn").textContent='Stats'

    }
}
function selected() {
    var sel = document.getElementById('dbs').value

  
    document.getElementById("selectedDB").value = sel
    console.log(sel)
    localStorage.setItem("db",sel)
    document.getElementById("selection").innerHTML = "Your selected: " + sel
    //button elementti pitää olla valmiina, muuten jquery hide ei toimi eli
    //tässä muutetaan buttoni näkyväksi
    document.getElementById("hideBtn").hidden = false
    
   

}
//näytetään valitun select-elementin teksti
function getSelectedText(sel) {
    document.getElementById("DBname").value=sel.options[sel.selectedIndex].text
    
}

function changeBGcolor(sel) {
    var col =  sel.options[sel.selectedIndex].value
    console.log(col)
    document.getElementById("dbTable").style.backgroundColor=col
}

function changeFont(sel) {
    var size = sel.options[sel.selectedIndex].value
    document.getElementById("dbTable").style.fontSize=size
}