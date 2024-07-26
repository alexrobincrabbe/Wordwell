const match = document.getElementById("match");
const guess = document.getElementById("guess");
let word = "";
//const dictionary=$.getJSON('dictionary');
// let dictionary_global
// const dictionary= getDictionary()
// console.log(dictionary)
// console.log(dictionary_global)
/*
let word = "cat";
for (let [key, value] of Object.values(dictionary)){
    console.log(key)
    if (key==word){
        match.innerHTML=`${key}:${value}`
    }
}
*/


// async function getDictionary() {
//     const dictionaryUrl = "dictionary";
//     try {
//       const response = await fetch(dictionaryUrl);
//       if (!response.ok) {
//         throw new Error(`Response status: ${response.status}`);
//       }
//       dictionary_global = await response.json();
//       console.log(dictionary_global)
//       return(dictionary_global)
//     } catch (error) {
//       console.error(error.message);
//     }
//   }

async function getDictionary() {
  const dictionaryUrl = "dictionary"
  try {
    const response = await fetch(dictionaryUrl);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    dictionary_global = await response.json();
    return dictionary_global;
  } catch (error) {
    console.error("Failed to load dictionary:", error.message);
  }
}

/*
document.addEventListener('keydown', event => {
  if (event.key == "Backspace" && word.length > 0){
    word = word.substring(0, word.length -1)
  }
  if (event.keyCode >= 65 && event.keyCode <= 90) {
    if (word.length < 17) word += event.key.toUpperCase()
    }
  guess.innerHTML = word
  getDictionary().then(dictionary => {
    if (dictionary) {
      // Sample code to display a match
      for (let [key, value] of Object.entries(dictionary)) {
        if (word===key.toUpperCase()) {
          match.innerHTML += `${key}: ${value}<br>`;
        }
      }
    }
  });
})
*/
getDictionary().then(dictionary => {
  runGame(dictionary)
})

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
let matched = false
function guessWord(word, dictionary) {
  document.addEventListener('keydown', event => {
    if (event.key == "Backspace" && word.length > 0) {
      word = word.substring(0, word.length - 1)
    }
    if (event.keyCode >= 65 && event.keyCode <= 90) {
      if (word.length < 17) word += event.key.toUpperCase()
    }
    guess.innerHTML = word
    matched =false;
    if (dictionary) {
      // Sample code to display a match
      for (let [key, value] of Object.entries(dictionary)) {
        if (word === key.toUpperCase()) {
          match.innerHTML = `${key}: ${value}<br>`;
          matched = true;
        }
      }
      if (matched == false){
        match.innerHTML="";
      }
    }
  })
}