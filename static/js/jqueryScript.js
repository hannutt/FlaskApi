//tämä lause tarvitaan että jquery toimii ulkoisesta js-tiedostosta.
$(document).ready(function () {
    //jquery funktio näyttää jokaisen _id-arvon ja siirtää sen input-kenttään kun sitä klikkaa hiirellä.
    jQuery(".sqlite").click(function () {
        //event.preventDefault();
        var text = jQuery(this).text();
        //katkaistaan merkkijono | merkin kohdalta
        var textSplit = text.split("|")
        //textSplit on taulukko, joten talletetaan muuttujaan taulukon ensimmäinen (0) alkio.
        var splittedText = textSplit[0]
        //trim poistaa välilyönnit
        var noWhiteSpace = splittedText.trim()
        console.log(noWhiteSpace);
        document.getElementById("sqliteFile").value = noWhiteSpace
        document.getElementById("sqliteFile2").value = noWhiteSpace
        document.getElementById("sqliteBase").value = noWhiteSpace
        sessionStorage.setItem('dbfile', noWhiteSpace)
        document.getElementById("sqliteFile").style.background = "yellow"
        document.getElementById("sqliteFile").onchange = backUp(document.getElementById("sqliteFile").value)
        var database = document.getElementById("sqliteFile").value
        document.getElementById("createTableLbl").innerText = "Create empty table to: " + noWhiteSpace
        document.getElementById("tableColumnsCB").hidden = false
        document.getElementById("tableColumns").innerText = "Create Table with columns"
    })


});
$(document).ready(function () {
    jQuery(".sqlite").dblclick(function () {
        var text = jQuery(this).text()
        document.getElementById("dbPath").hidden = false
        document.getElementById("dbPath").value = text
        document.getElementById("accessBtn").hidden = false
    })
})

$(document).ready(function () {
    $("#apiName").animate({
        width: "70%",
        opacity: 0.9,
        marginLeft: "0.6in",
        fontSize: "3em",
        borderWidth: "10px",
    }, 1500);
});
$(document).ready(function () {
    $(function () {
        var paths = document.getElementsByClassName("paths")
        var pathNames = paths[0].innerHTML
        var pathList = pathNames.split(",")
        var newPathList = []
        //käydään pathList listan sisältö läpi
        for (var i = 0; i < pathList.length; i++) {
            var item = pathList[i]
            //jos sisällön merkkijonot sisältävät kaksi \\ merkkiä niin korvataan replacen
            //avulla \\ merkit \ merkiksi ja ' ' merkit tyhjällä ja lisätään se uuteen (newpathlist) listaan.
            if (item.includes("\\\\") && item.includes("'") && item.includes("'")) {
                var itemRep = item.replace("\\\\", "\\").replace("'", "").replace("'", "").replace("[", "").replace("]", "")
                newPathList.push(itemRep)
            }
        }


        $('#dbPath').autocomplete({
            source: newPathList
        })
    })
})