function createEdit() {

    var fieldsTotal = document.getElementById("keystotal").innerHTML
    var fieldsTotalInt = Number(fieldsTotal)
    console.log(typeof fieldsTotalInt)
    var cb = document.getElementById("edit")
    var addCB = document.getElementById("add")
    
    var editBtn = document.createElement("BUTTON")
    editBtn.id = "editBtn"
    editBtn.textContent = "Edit"
    //jos checkbox on klikattu, luodaan edit painike, muussa tapauksessa tuhotaan painike
    if (cb.checked == true) {
      //document.body.appendChild(editBtn)
      
      //silmukan avulla luodaan yhtä monta input-kenttää kuin mitä kenttiä on kokoelmassakin
      for (var i = 0; i < fieldsTotalInt; i++) {
        var inpField = document.createElement("INPUT");
        //annetaan id silmukkamuuttujan kautta eli id:t ovat 0,1,2,3 jne
        inpField.id = i
        inpField.name= i
        inpField.setAttribute("type", "text");
        //document.body.appendChild(inpField);
        document.getElementById("editing").appendChild(editBtn)
        document.getElementById("editing").appendChild(inpField)

        //tietokannan kenttien nimet on lähetetty python listana html-sivulle, josta ne on puolestaan
        //talletettu javascript listaan. i-silmukkamuuttujan avulla saadaan asetettuja oikea placeholder
        //oikeaan input-kenttään
        document.getElementById(i).value = valuesList[i]
      }

    }
    else if(addCB.checked==true)
    {
      var addBtn = document.createElement("BUTTON")
      addBtn.id = "Add"
      editBtn.textContent = "Add"
      fieldTotal=document.createElement("INPUT")
      fieldTotal.id="fieldtotal"
      fieldTotal.name="fieldtotal"
      //silmukan avulla luodaan yhtä monta input-kenttää kuin mitä kenttiä on kokoelmassakin
      for (var i = 1; i < fieldsTotalInt; i++) {
        var inpField = document.createElement("INPUT");
        var fieldValues = document.createElement("INPUT");

        //annetaan id silmukkamuuttujan kautta eli id:t ovat 0,1,2,3 jne
        inpField.id = i
        inpField.name= i
        fieldValues.name="field"+i
        fieldValues.id="field"+i
        fieldValues.hidden=true
        fieldValues.setAttribute("type","text")
        inpField.setAttribute("type", "text");
        
        //luodut syötentät ja painkkeet sijoitetaan addNew diviin
        document.getElementById("addNew").appendChild(inpField)
        document.getElementById("addNew").appendChild(editBtn)
        document.getElementById("addNew").appendChild(fieldValues)
        //tietokannan kenttien nimet on lähetetty python listana html-sivulle, josta ne on puolestaan
        //talletettu javascript listaan. i-silmukkamuuttujan avulla saadaan asetettuja oikea placeholder
        //oikeaan input-kenttään
        document.getElementById(i).placeholder = valuesList[i]
        document.getElementById("field"+i).value=valuesList[i]
        
        document.getElementById("addNew").appendChild(fieldTotal)
        document.getElementById("fieldtotal").value=fieldsTotalInt

      }
      
      
    }
    else {
      document.getElementById("editBtn").remove()
      //input-kenttien tuhoamisessa käytetään myös silmukkaa ja fieldstotal muuttujaa
      for (var i = 0; i < fieldsTotalInt; i++) {
        document.getElementById(i).remove()

      }
    }

  }