var clicks=0

var isSelected = false



function stats()
{
    clicks=clicks+1
    if (clicks % 1 == 0)
    {
      var total=document.getElementById("dbTotal").innerHTML
      //muunnetaan luvuksi
      var intTotal = parseInt(total)
      var dbnames=[]
      var dbsizes=[]
      //2 for silmukkaa, toisella silmukalla käydään läpi arrName = tietokantojen nimet
      //ja toisella arrNums=tietokantojen koot. 
      for (var i=0;i<intTotal;i++)
      {
      arrNames[i]
      dbnames.push(arrNames[i])
      arrNums[i]
      dbsizes.push(arrNums[i])
      
      }
    
     
  
  var barColors = ["red", "green","blue","orange","brown",];
  
  new Chart("myChart", {
    type: "bar",
    data: {
      labels: dbnames,
      datasets: [{
        backgroundColor: barColors,
        data: dbsizes
      }]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "Your databases and their sizes"
      }
    }
  });

        document.getElementById("stats").hidden=false
        document.getElementById("chart").hidden=false
        document.getElementById("statsBtn").textContent='Hide chart'
        //muutetaan buttonin tyyliluokka määrettä
        document.getElementById("statsBtn").setAttribute("class",'statsBtnHide')
        
    }
    if (clicks % 2 ==0)
    {
        document.getElementById("stats").hidden=true
        document.getElementById("chart").hidden=true
        document.getElementById("statsBtn").textContent='Database Statistics'
        document.getElementById("statsBtn").setAttribute("class",'statsBtn')

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

function getMysqlDb(selection) {
  document.getElementById("selectedSQL").value = selection.options[selection.selectedIndex].text
  

}

function getSqlTable(selection)
{
  document.getElementById("selectedTable").value=selection.options[selection.selectedIndex].text
  
}

function getSelectedFieldName(sel) {
  document.getElementById("selFieldName").value=sel.options[sel.selectedIndex].text

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
    
    function GetSelectionFromSelect(sel) {
      
      var path = localStorage.getItem('db')
      //alert(sel.options[sel.selectedIndex].text);
      document.getElementById("path").innerHTML = path + "/" + sel.options[sel.selectedIndex].text
      document.getElementById("colname").value = sel.options[sel.selectedIndex].text
      document.getElementById("DBpath").value = path
      
   
    }

    function cancelEdit() {
      document.getElementById("crudArea").innerHTML=""
      document.getElementById("edit").checked=false
    }
    
    function query() {
      if (document.getElementById("freequery").checked==true)
      {
        document.getElementById("querytext").hidden=false
        document.getElementById("runBtn").hidden=false

      }
      else {
        document.getElementById("querytext").hidden=true
        document.getElementById("runBtn").hidden=true
      }
      
    }


  