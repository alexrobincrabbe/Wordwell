const match = document.getElementById("match");
const guess = document.getElementById("guess");
const wordList = document.getElementById("word-list")
let word = "";
let matched = false;

// Load the dictionary then start the game
getDictionary().then(dictionary => {
  guess.innerHTML = "dictionary loaded"
  runGame(dictionary)
})


// Main game function
function runGame(dictionary) {
  if (dictionary) {
    let word = "";
    word = guessWord(word, dictionary);
    // Sample code to display a match
    for (let [key, value] of Object.entries(dictionary)) {
      if (word === key.toUpperCase()) {
        match.innerHTML += `${key}: ${value}<br>`;
      }
    }
  }
}


/**
 * Loads a json dictionary of words as a javascript object
 * The Json file is saved on the server(file path is specified in the dictionary view)
 * @returns (object) dictionary of words
 */
async function getDictionary() {
  guess.innerHTML = "loading dictionary..."
  const dictionaryUrl = "dictionary"

  try {
    const response = await fetch(dictionaryUrl);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    dictionary = await response.json();
    return dictionary;
  } catch (error) {
    console.error("Failed to load dictionary:", error.message);
  }
}

function guessWord(word, dictionary) {
  document.addEventListener('keydown', event => {
    if (event.key == "Backspace" && word.length > 0) {
      word = word.substring(0, word.length - 1)
    }
    if (event.keyCode >= 65 && event.keyCode <= 90) {
      if (word.length < 17) word += event.key.toUpperCase()
    }
    guess.innerHTML = word
    matched = false;
    if (dictionary) {
      // Sample code to display a match
      for (let [key, value] of Object.entries(dictionary)) {
        if (word === key.toUpperCase()) {
          match.innerHTML = `${key}: ${value}<br>`;
          matched = true;
        }
      }
      if (matched == false) {
        match.innerHTML = "";
      }
    }
    if (event.key == "Enter"){
      checkWord(word, matched);
    }
  })
}

function checkWord(word){
  if (matched){
    wordList.innerHTML += `${word} <br>`;
    guess.innerHTML="";
  }else{
    match.innerHTML="invalid word";
  }
  
}