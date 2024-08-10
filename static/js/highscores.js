const rankings = document.getElementsByClassName("ranking")
let rank = 0;
for (let ranking of rankings){
    rank=rank+1;
    switch(true){
        case (rank==1):
            ranking.innerHTML="1st";
            break;
        case (rank==2):
            ranking.innerHTML="2nd";
            break;
        case (rank==3):
            ranking.innerHTML="3rd";
            break;
        default:
            ranking.innerHTML=`${rank}th`;
    }   
}