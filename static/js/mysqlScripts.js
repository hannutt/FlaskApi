function createMySqlFields(textToArray) {
    var fieldNames = []
    fieldNames.push(document.getElementById('fieldnames').innerHTML)
    var fields = document.getElementById("fields").innerHTML
    var fieldsInt = parseInt(fields)
    var linebreak = document.createElement("br");
    var editBtn=document.createElement("BUTTON")
    editBtn.setAttribute("class","editBtn")
    editBtn.textContent="Edit record"
    var cancelBtn = document.createElement("BUTTON")
    cancelBtn.textContent="Cancel edit"
    cancelBtn.setAttribute("class","cancelBtn")
    //yhdistetään eventlistenerillä klikkaus ja suoritettava funktio
    cancelBtn.addEventListener("click",cancelEdit)
    var cb = document.getElementById("edit")
    if (cb.checked==true)
    {
        //luodaan niin monta syötekenttää, kuin sql taulussa on kenttiä.
        for (var i = 0;i<fieldsInt;i++)
        {
            var inputField=document.createElement("INPUT")
            inputField.id=i
            document.getElementById("crudArea").appendChild(inputField)
            
        }
        document.getElementById("crudArea").appendChild(linebreak)
       
        
       
        
        //lisätään syötekenttien arvoksi tietokannassa olevat arvot
        //eli esim. login taulusta id, username psw ja email. j on kierrosmuuttuja
        //joka alkaa nollasta, samoin kuin luotujen syötekenttien id:t text to arrayssa
        //kenttien nimet listamuodossa
          for (var j=0;j<fieldsInt;j++)
        {
            document.getElementById(j).value=textToArray[j]
          
        }
        document.getElementById("crudArea").appendChild(linebreak)
        document.getElementById("crudArea").appendChild(linebreak)
        document.getElementById("crudArea").appendChild(editBtn)
        
        document.getElementById("crudArea").appendChild(cancelBtn)
        
    }
        
}

function createFieldsToNew() {
    var cbNew = document.getElementById("newrecord")
    var fields = document.getElementById("fields").innerHTML
    var fieldsInt = parseInt(fields)
    var fieldnames=document.getElementById("fieldnames").innerHTML
    var splitNames = fieldnames.split(" ")
    console.log(splitNames)
    if (cbNew.checked==true) {
        //syötekentät
        for (var i = 0;i<fieldsInt;i++)
            {
                var inputField=document.createElement("INPUT")
                inputField.id=i
                document.getElementById("crudArea").appendChild(inputField)
            }
            //placeholderit syötekenttiin
            for (var j=0;j<fieldsInt;j++)
                {
                    document.getElementById(j).placeholder=splitNames[j]
                  
                }

    }
    //jos checboksi ei ole valittu, niin crudarea divin sisältö muutetaan tyhjäksi
    else {
        document.getElementById("crudArea").innerHTML=""
    }       
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