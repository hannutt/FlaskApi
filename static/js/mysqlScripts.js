function createMySqlFields(textToArray) {
    var fieldNames = []
    fieldNames.push(document.getElementById('fieldnames').innerHTML)
    var fields = document.getElementById("fields").innerHTML
    var fieldsInt = parseInt(fields)
    var linebreak = document.createElement("br");
    var editBtn=document.createElement("BUTTON")
    editBtn.textContent="Edit record"
   
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
        
        //lisätään syötekenttien arvoksi tietokannassa olevat arvot
        //eli esim. login taulusta id, username psw ja email. j on kierrosmuuttuja
        //joka alkaa nollasta, samoin kuin luotujen syötekenttien id:t text to arrayssa
        //kenttien nimet listamuodossa
          for (var j=0;j<fieldsInt;j++)
        {
            document.getElementById(j).value=textToArray[j]
          
        }
        document.getElementById("crudArea").appendChild(linebreak)
        document.getElementById("crudArea").appendChild(editBtn)
        
    }
        
}

function createFieldsToNew() {
    var fields = document.getElementById("fields").innerHTML
    var fieldsInt = parseInt(fields)
    var fieldnames=document.getElementById("fieldnames").innerHTML
    var splitNames = fieldnames.split(" ")
    console.log(splitNames)
    for (var i = 0;i<fieldsInt;i++)
        {
            var inputField=document.createElement("INPUT")
            inputField.id=i
            document.getElementById("crudArea").appendChild(inputField)
        }
        for (var j=0;j<fieldsInt;j++)
            {
                document.getElementById(j).placeholder=splitNames[j]
              
            }
        

}