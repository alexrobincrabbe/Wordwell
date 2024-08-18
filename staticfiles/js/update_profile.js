/* Script to fix the currently field in the form */
const currently = document.querySelectorAll(".text-break>a");
const currently_field = document.querySelectorAll(".text-break")[0]
const profilePicture = document.getElementsByClassName('account-img')[0]
const alt = profilePicture.alt

/* show the text 'Image' as a link to the image if the user has uploaded one.
otherwise show text none with no linke */
if (alt != "placeholder profile picture") {
    currently[0].innerHTML = "Image"
    currently[0].style.color = "blue";
    currently[0].style.textDecoration = "underline";
} else {
    currently_field.innerHTML = "None"
}