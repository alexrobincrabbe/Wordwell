const rankings = document.getElementsByClassName("ranking")
let rank = 0;
for (let ranking of rankings){
    rank=rank+1;
    ranking.innerHTML=rank
}