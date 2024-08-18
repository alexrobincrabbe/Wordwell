/* Script to fix the currently field in the profile update form */
/* jshint esversion: 11 */

const currentlyLink = document.querySelectorAll(".text-break>a")[0];
const currentlyField = document.querySelectorAll(".text-break")[0];
const profilePicture = document.getElementsByClassName('account-img')[0];
const alt = profilePicture.alt;

/* show the text 'Image' as a link to the image if the user has uploaded one.
otherwise show text none with no linke */
if (alt != "placeholder profile picture") {
    currentlyLink.innerHTML = "Image";
    currentlyLink.style.color = "blue";
    currentlyLink.style.textDecoration = "underline";
} else {
    currentlyField.innerHTML = "None";
}