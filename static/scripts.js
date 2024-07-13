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
        document.getElementById("statsBtn").textContent='Database Statistics'

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
//valikosta valitun tekstin näyttö selectionfordb tagissa
function getSelectedDataBase(select) {
  document.getElementById("nameOfDb").value=select.options[select.selectedIndex].text
}

function getCollectionName(col) {
  document.getElementById("atlasCollection").value=col.options[col.selectedIndex].text
}
//table elementin taustavärin vaihto
function changeBGcolor(sel) {
    var col =  sel.options[sel.selectedIndex].value
    console.log(col)
    document.getElementById("dbTable").style.backgroundColor=col
}
//table elementin fontin koon vaihto
function changeFont(sel) {
    var size = sel.options[sel.selectedIndex].value
    document.getElementById("dbTable").style.fontSize=size
}


//funktiolla poistetaan/näytetään checkboksin statesta(checked) riippuen table elementtied tietokannan datan
//ympärillä    

function removeTable() {
    var tableCB=document.getElementById("tableCB")
    if (tableCB.checked==true)
    {
      
      document.getElementById('dbTable').border=0
      document.getElementById("tableCBLbl").innerText='Show table borders'

    }
    if (tableCB.checked==false)
    {
      document.getElementById('dbTable').border=1
      document.getElementById("tableCBLbl").innerText='Remove table borders'
    }
    

  }

  function prettyText() {
    var table=document.getElementById("dbTable")
    var originalText = table.innerHTML
   
    var txtCB = document.getElementById("prettytxtCB")
    

    var total=document.getElementById("total").innerHTML
    var records = Number(total)
    console.log(typeof(records))
    console.log('pretty text')
    //for-silmukan avulla käydään koko taulukon tekstisisältö läpi ja poistetaan määritellyt merkit
    //replace metodilla. records on näytettävien dokumenttien määrä ja se saadaan alunperin pyMongo count
    //metodilla, joka suoritetaan python funktiossa ja lähetetään html-sivulle ja otetaan käyttöön
    //javascriptissä total ja records muuttujissa.
    if (txtCB.checked==true)
    {
      for (var i=0;i<records;i++)
        {
          //tämän avulla teksti voidaan palauttaa alkuperäiseen muotoon
          table.setAttribute('data-orig', originalText);
          var prettytxt=document.getElementById("dbTable").innerHTML.replace('{','',).replace("}","").replace('ObjectId',"").replace("(","").replace(")","")
          document.getElementById("dbTable").innerHTML=prettytxt
          
    
        }
    }
    if (txtCB.checked==false)
    {
        var table = document.getElementById("dbTable")
        //palauteteaan alkuperäinen teksti
        var originalText=table.getAttribute('data-orig');
        table.innerHTML=originalText

      }
      

    }
 


  