// Script to add event listeners to delete buttons to display modal 
/* jshint esversion: 11 */

const postDeleteModal = new bootstrap.Modal(document.getElementById("post-delete-modal"));
const replyDeleteModal = new bootstrap.Modal(document.getElementById("reply-delete-modal"));
const postDeleteButton = document.getElementById("post-btn-delete");
const postDeleteConfirm = document.getElementById("post-delete-confirm");
const replyDeleteButtons = document.getElementsByClassName("reply-btn-delete");
const replyDeleteConfirm = document.getElementById("reply-delete-confirm");

// open model when delete post button is clicked
postDeleteButton.addEventListener("click", (e) => {
    let slug=e.target.getAttribute("slug");
    postDeleteConfirm.href = `delete_post/${slug}`;
    postDeleteModal.show();
});

// copen modal when delete reply buttons are clicked
for (let button of replyDeleteButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply-id");
      let slug = e.target.getAttribute("slug");
      replyDeleteConfirm.href = `/board/delete_reply/${slug}/${replyId}`;
      replyDeleteModal.show();
    });
  }