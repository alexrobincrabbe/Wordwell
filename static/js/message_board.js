// Styles the message board list alternatingly
/* jshint esversion: 11 */

const rows = document.getElementsByTagName("tr");
let row_no =0;
for (let row of rows){
    row_no+=1;
    if (row_no % 2 ==0){
        row.style.backgroundColor="#1b1835";
    } else{
        row.style.backgroundColor="#352870";
    }
}
