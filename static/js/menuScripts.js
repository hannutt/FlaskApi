function mongoquery() {
    if (document.getElementById("mongoQuery").checked == true) {
      document.getElementById("mongodata").hidden = false
      document.getElementById("runMongo").hidden = false
      document.getElementById("dbTable").hidden = true
  
    } else {
      document.getElementById("mongodata").hidden = true
      document.getElementById("runMongo").hidden = true
      document.getElementById("dbTable").hidden = false
  
    }
  
  
  }
  var opened = 0
  function MenuOpened() {
    opened += 1
  
    if (opened % 1 === 0) {
      document.getElementById("colorCode").hidden = false
  
    }
    if (opened % 2 === 0) {
      document.getElementById("colorCode").hidden = true
  
    }
  }
  var fontMenu=0
  function fontMenuOpened() {
    fontMenu+=1
    if (fontMenu % 1 === 0) {
      document.getElementById("fontFam").hidden = false
  
    }
    if (fontMenu % 2 === 0) {
      document.getElementById("fontFam").hidden = true
  
    }
  
  }
  function showDelete() {
    if (document.getElementById("deleteCB").checked==true)
  {
    document.getElementById("objIdtext").hidden=false
    document.getElementById("objId").hidden=false
    document.getElementById("deleteButton").hidden=false
  
  }
  else{
    document.getElementById("objIdtext").hidden=true
    document.getElementById("objId").hidden=true
    document.getElementById("deleteButton").hidden=true
  
  
  }
  
  
  }
  
  
  
  
  