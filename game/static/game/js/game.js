const match = document.getElementById("match");
const guess = document.getElementById("guess");
const wordList = document.getElementById("word-list")
const timer = document.getElementById("timer")
const startButton = document.getElementById("start-button")
let runTimer

// Load the dictionary then ready startGame
getDictionary().then(dictionary => {
  guess.innerHTML = "dictionary loaded"
  startGame(dictionary)
})


// Start game function
function startGame(dictionary) {
  if (dictionary) {
    startButton.onclick = function () {
      runGame(dictionary)
    }
  }
}

// run game function
function runGame(dictionary) {
  startButton.innerText = "save score"
  startButton.onclick = function () {
    saveScore(score)
  }
  let word = "";
  let matched = false;
  let score = 0;
  let time = 60;
  let wordArray = [];
  // start the game timer
  clearInterval(runTimer);
  runTimer = setInterval(() => time = countDown(time), 1000);
  // update/guess the word
  [word, score, matched, wordArray] = guessWord(word, score, matched, dictionary, wordArray);
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

function countDown(time) {
  if (time > 0) {
    time -= 1
    timer.innerHTML = `${time}`
    return (time)
  }
}

function guessWord(word, score, matched, dictionary, wordArray) {
  document.addEventListener('keydown', event => {
    switch (true) {
      // delete a letter
      case (event.key == "Backspace" && word.length > 0):
        word = word.substring(0, word.length - 1);
        matched = checkDictionary(word, dictionary)
        break;
        // add a letter
      case (event.keyCode >= 65 && event.keyCode <= 90):
        if (word.length < 17) {
          word += event.key.toUpperCase()
        }
        matched = checkDictionary(word, dictionary)
        break;
        // guess a word
      case (event.key == "Enter"):
        [word, score, matched, wordArray] = checkWord(word, score, matched, wordArray);
        console.log(wordArray)
    }
    guess.innerHTML = word
    return [word, score, matched, wordArray]
  })
}

function checkDictionary(word, dictionary) {
  let match_found = false
  if (dictionary) {
    for (let [key, value] of Object.entries(dictionary)) {
      if (word === key.toUpperCase()) {
        match.innerHTML = `${key}: ${value}<br>`;
        match_found = true;
      }
    }
  }
  if (match_found) {
    return true
  } else {
    return false
  }
}

function checkWord(word, score, matched, wordArray) {
  if (matched) {
    wordList.innerHTML += `${word} <br>`;
    wordArray.push(word)
    guess.innerHTML = "";
    word = "";
    score += 1;
    matched = false
  } else {
    match.innerHTML = "invalid word";
  }
  return [word, score, matched, wordArray]
}

/**
 * Records the player score on the server
 * @param {*} score The player game score to be sent to the server
 */
async function saveScore(score) {
  const formData = new FormData();
  formData.append("score", score);
  try {
    const response = await fetch("", {
      method: "POST",
      body: formData,
    });
  } catch (e) {
    console.error(e);
  }
}