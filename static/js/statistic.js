var arrNums = []
var arrNames = []
var allStats = []
//kokoelmien nimien läpikäynti
function getNameValues() {
    //haetaan tietokantojen kokonaismäärän kertova luku dbTotal tagista
    var total = document.getElementById("dbTotal").innerHTML
    //muunnetaan luvuksi
    var intTotal = parseInt(total)
    console.log(typeof (intTotal))
    var nameValues = document.getElementsByClassName("statsNames")

    for (i = 0; i < intTotal; i++) {
        arrNames.push(nameValues[i].innerHTML)
    }
    console.log(arrNames)

}


var maxVal = 0
var minVal = 0
function getNumValues() {
    var numValues = document.getElementsByClassName("statsNums")
    for (i = 0; i < 7; i++) {
        arrNums.push(parseInt(numValues[i].innerHTML))
        console.log(arrNums)


    }
    minVal = Math.min(...arrNums)
    maxVal = Math.max(...arrNums)
    //suurimman numeron indeksipaikka arrNums listassa. talletetaan se muuttujaan, koska arrNames ja arrNums ovat samankokoisia listoja ja
    // listan järjestys on sama, näin saadaan käyttöön chartJs:ssä suurin kannan koko ja sen nimi
    indexNum = arrNums.indexOf(maxVal)
    indexNumMin = arrNums.indexOf(4)
    console.log(indexNum)
    console.log(maxVal)
    console.log(minVal)
}
function getAllValues() {
    var all = document.getElementsByClassName("allStat")
    for (j = 0; j < 14; j++) {
        allStats.push(all[j].innerHTML)
    }

}
