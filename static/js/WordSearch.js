var words=[]
//tekstin haku html-sivulta
  function search(text,bgcol) {
    words.push(text)
    console.log(words)
    document.getElementById("words").innerHTML='previous searches: '+words

    if (window.find && window.getSelection) {


      document.designMode = "on";
      //getselection on käyttäjän valitsema tekstialue / tai tekstin sijainti

      var sel = window.getSelection();
      sel.collapse(document.body, 0);
      while (window.find(text)) {
            document.execCommand("HiliteColor", false, bgcol);
            sel.collapseToEnd();
    }
    
  }
  document.designMode = "off";
}




function wordStatistic() {
    return words.reduce(function (a, b) {
        var shortest= a.length < b.length ? a : b;
        var longest=a.length > b.length ? a : b;
        document.getElementById("longest").innerHTML='Longest word: ' +longest + " length: "+longest.length
        document.getElementById("shortest").innerHTML='Shortest word: '+shortest + " length: "+shortest.length
    });
}

