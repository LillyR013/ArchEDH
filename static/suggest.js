async function cardPhoto(commander) {
    let response = await fetch("/commander/" + commander);
    let data = await response.json();
    if (data.error) {
        alert("Invalid Card");
    }
    else {
        document.getElementById("cardPhoto").src = data.image_uri;
    }
}

async function topCards(commander) {
    let response = await fetch("/top/" + commander);
    let data = await response.json();
    if (data.error) {
    }
    else {
        cards = data["Top Cards"];
        for (var cardNum in cards) {
            var card = cards[cardNum];
            var newParagraph = document.createElement("p");
            newParagraph.textContent = card["name"] + " - " + card["label"];
            document.getElementById("top").appendChild(newParagraph);
        }
    }
}

async function topCreatures(commander) {
    let response = await fetch("/creatures/" + commander);
    let data = await response.json();
    if (data.error) {
    }
    else {
        cards = data["Creatures"];
        for (var cardNum in cards) {
            var card = cards[cardNum];
            var newParagraph = document.createElement("p");
            newParagraph.textContent = card["name"] + " - " + card["label"];
            document.getElementById("creatures").appendChild(newParagraph);
        }
    }
}

function readCSVFile(file) {
    return new Promise((resolve, reject) => {
        var contents = "";
        var reader = new FileReader();
        reader.onload = function (e) {
            resolve(e.target.result);
        }
        reader.onerror = function (e) {
            reject(e);
        }
        reader.readAsText(file);
    });
}

async function search() {
    var commander = document.getElementById("cardName").value;
    collection = [];
    if (document.getElementById("collection").files.length == 1) {
        try {
            csvData = await readCSVFile(document.getElementById("collection").files[0]);
            csvData = csvData.replaceAll("\r\n", "\n");
            csvData = csvData.replaceAll("\"", "");
            csvTester = /^Name\n[\s\S]*$/
            if (csvTester.test(csvData)) {
                collection = csvData.split("\n");
                collection.shift();
            }
        }
        catch (e) {
        }
    }
    console.log(collection);
    cardPhoto(commander)
    topCards(commander)
    topCreatures(commander)
}