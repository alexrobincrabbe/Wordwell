const match = document.getElementById("match");
const guess = document.getElementById("guess");
const wordList = document.getElementById("word-list")
const timer = document.getElementById("timer")
const startButton = document.getElementById("start-button")
const board = document.getElementById('board')
const letters = document.getElementsByClassName('letter')
const letterValues = document.getElementsByClassName('letterValue')
const reshuffleButton = document.getElementById("reshuffle-button")
const playAgainButton = document.getElementById("play-again-button");
const saveScoreButton = document.getElementById("save-score-button");
const showScore = document.getElementById("score")
let boardLetters = []
let runTimer
// Defines the dice used to generate the letters on the board
let dice = [
  ["R", "I", "F", "O", "B", "X"],
  ["I", "F", "E", "H", "E", "Y"],
  ["D", "E", "N", "O", "W", "S"],
  ["U", "T", "O", "K", "N", "D"],
  ["H", "M", "S", "R", "A", "O"],
  ["L", "U", "P", "E", "T", "S"],
  ["A", "C", "I", "T", "A", "O"],
  ["Y", "L", "G", "K", "U", "E"],
  ["Qu", "B", "M", "J", "O", "A"],
  ["E", "H", "I", "S", "P", "N"],
  ["V", "E", "T", "I", "G", "N"],
  ["B", "A", "L", "I", "Y", "T"],
  ["E", "Z", "A", "V", "N", "D"],
  ["R", "A", "L", "E", "S", "C"],
  ["U", "W", "I", "L", "R", "G"],
  ["P", "A", "C", "E", "M", "D"]
]

// Generate the board tile html elements
for (let i = 0; i < 16; ++i) {
  board.innerHTML += `<div class="letter"><div class="letterValue"></div></div>`
}

// randomly generate board letters
boardLetters = shuffleBoard(dice);

// Load the dictionary then ready startGame
getDictionary().then(dictionary => {
  guess.innerHTML = "dictionary loaded"
  dictionaries = makeDictionaries(dictionary)
  startGame(dictionaries)
})

// Splits the dicionary into 26 dictionaries containing words starting with each letter of the alphabet
function makeDictionaries(dictionary) {
  let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  let dictionaries = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
  for (key in dictionary) {
    let i = 0;
    for (letter of alphabet) {
      if (key[0] == letter) {
        thisDictionary = dictionaries[i]
        thisDictionary[key] = 1
      }
      i += 1
    }
  }
  return dictionaries
}


// Start game function
function startGame(dictionary) {
  if (dictionary) {
    startButton.onclick = function () {
      runGame(dictionary)
    }
    reshuffleButton.onclick = function () {
      boardLetters = shuffleBoard(dice);
    }
    playAgainButton.onclick = function () {
      playAgain()
    }
  }
}

// run game function
function runGame(dictionary) {
  let word = "";
  let matched = false;
  let score = 0;
  let wordArray = [];
  reshuffleButton.style.display = "none";
  startButton.style.display = "none";
  console.log("hello")
  saveScoreButton.addEventListener("click", function () {
    saveScore(wordArray).then(() => {guess.innerHTML="score saved"; saveScoreButton.style.display="none"});
  })

  // update/guess the word
  [word, matched, wordArray] = guessWord(word, matched, dictionary, wordArray);
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

function countDown(time,wordArray) {
  if (time > 0) {
    time -= 1
    timer.innerHTML = `${time}`
    return (time)
  } else {
    playAgainButton.style.display = "inline"
    saveScoreButton.style.display = "inline"
    clearInterval(runTimer)
    let score = 0
    for (word of wordArray) {
      score += word.length - 2
    }
    showScore.innerHTML=score

    
  }
}

function playAgain() {
  location.reload()
}

function guessWord(word, matched, dictionary, wordArray) {
  // start the game timer
  let time = 10;
  clearInterval(runTimer);
  runTimer = setInterval(() => time = countDown(time,wordArray), 1000);
  let boardMatched = false
  let highlight = []
  console.log(time)
  document.addEventListener('keydown', event => {
    if (time > 0) {
      console.log(time)
      switch (true) {
        // delete a letter
        case (event.key == "Backspace" && word.length > 0):
          word = word.substring(0, word.length - 1);
          matched = checkDictionary(word, dictionary)
          clearBoard();
          [boardMatched, highlight] = searchBoard(word);
          highlightLetters(highlight, matched, boardMatched)
          break;
          // add a letter
        case (event.keyCode >= 65 && event.keyCode <= 90):
          if (word.length < 17) {
            word += event.key.toUpperCase()
          }
          matched = checkDictionary(word, dictionary);
          [boardMatched, highlight] = searchBoard(word);
          highlightLetters(highlight, matched, boardMatched)
          break;
          // guess a word
        case (event.key == "Enter"):
          [word, matched, wordArray] = checkWord(word, matched, boardMatched, wordArray);
          clearBoard()
          guess.innerHTML = "";
          word = "";
      }
      guess.innerHTML = word
      return [word, matched, wordArray]
    }
  })
}

function searchBoard(word) {
  let boardMatched = false;
  let highlight = Array(16).fill(false);
  if (word.length > 16) return
  // Mark all characters as not visited
  let visited = Array.from(Array(4), () => new Array(4).fill(0));

  // Initialize current string
  let str = "";

  // Consider every character and look for all words
  // starting with this character
  for (let i = 0; i < 4; i++)
    for (let j = 0; j < 4; j++) {
      searchBoardUtil(boardLetters, visited, i, j, str, word);
    }
  return [boardMatched, highlight]

  function searchBoardUtil(boardLetters, visited, i, j, str, word) {
    // mark current tile as visited
    visited[i][j] = true;
    // add the current tile letter to the search string
    str = str + boardLetters[i][j];
    // highlight word on board
    if (str == word.substring(0, str.length)) {
      highlight[j + (i * 4)] = true
    }
    // check if the word matches a valid string on the board
    if (str == word) {
      boardMatched = true
    }
    // Traverse adjacent cells of boardLetters[i,j]
    // Check if each cell is on the board, has not been visited
    // If the current word string is not on the board, then skip
    for (let row = i - 1; row <= i + 1 && row < 4; row++)
      for (let col = j - 1; col <= j + 1 && col < 4; col++)
        if (row >= 0 && col >= 0 && !visited[row][col] && str == word.substring(0, str.length))
          searchBoardUtil(boardLetters, visited, row, col, str, word);
    // Erase current character from string and mark visited of current tile as false
    str = "" + str[str.length - 1];
    visited[i][j] = false;
  }
}

function highlightLetters(highlight, matched, boardMatched) {
  let colour = "yellow"
  if (matched && boardMatched) {
    colour = "green"
  }
  if (!boardMatched) {
    colour = "red"
  }
  for (i = 0; i < letters.length; i++) {
    if (highlight[i] == 1)
      letters[i].style.backgroundColor = colour;
  }
}

// clears highlighted letters
function clearBoard() {
  for (i = 0; i < letters.length; i++) {
    letters[i].style.backgroundColor = "white";
  }
}

function checkDictionary(word, dictionary) {
  let match_found = false
  if (word.length < 3) {
    return false
  }
  if (dictionary) {
    const alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
      "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    let i = 0;
    for (letter of alphabet) {
      if (word[0] == letter) {
        for (let [key, value] of Object.entries(dictionary[i])) {
          if (word === key.toUpperCase()) {
            match.innerHTML = `${key}: ${value}<br>`;
            match_found = true;
          }
        }
      }
      i += 1
    }
    if (match_found) {
      return true
    } else {
      return false
    }
  }
}


function checkWord(word, matched, boardMatched, wordArray) {
  if (matched && boardMatched) {
    if (!wordArray.includes(word)) {
      let wordScore = word.length - 2
      wordList.innerHTML += `${word} - ${wordScore} points<br>`;
      wordArray.push(word)
      matched = false
    } else {
      match.innerHTML = "already found";
    }

  } else {
    match.innerHTML = "invalid word";
  }
  return [word, matched, wordArray]
}

/**
 * Records the player score on the server
 * @param {*} score The player game score to be sent to the server
 */
async function saveScore(wordArray) {
  let score = 0
  
  for (word of wordArray) {
    score += word.length - 2
  }
  console.log(score)
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

/**
 * Randomly generates the letters on the board
 * @param {*} dice an array of 16 six-sided dice that are rolled and then randomly distributed on the board
 * @returns an 2-D array containing the letters on the board
 */
function shuffleBoard(dice) {
  let shuffledDice = shuffleArray(dice)
  let boardLetters = new Array(4).fill("").map(() => new Array(4).fill(""));
  for (i = 0; i < 4; i++)
    for (j = 0; j < 4; j++) {
      boardLetters[i][j] = shuffledDice[i + j * 4][Math.floor(Math.random() * 6)]
      letterValues[j + i * 4].innerText = boardLetters[i][j]
    }
  return boardLetters
}

// function to shuffle array
function shuffleArray(array) {
  let currentIndex = array.length,
    randomIndex;
  // While there remain elements to shuffle.
  while (currentIndex > 0) {
    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]
    ];
  }
  return array;
}