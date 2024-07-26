const match = document.getElementById("match");

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
    const dictionaryUrl = "../dictionary.json"
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
  
  getDictionary().then(dictionary => {
    console.log(dictionary);
    if (dictionary) {
      // Sample code to display a match
      let word = "cat";
      for (let [key, value] of Object.entries(dictionary)) {
        if (key === word) {
          match.innerHTML = `${key}: ${value}`;
        }
      }
    }
  });