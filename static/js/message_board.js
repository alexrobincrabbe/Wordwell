const postDeleteModal = new bootstrap.Modal(document.getElementById("post-delete-modal"));
const postDeleteButton = document.getElementById("post-btn-delete");
const postDeleteConfirm = document.getElementById("post-delete-confirm");

postDeleteButton.addEventListener("click", (e) => {
    let slug=e.target.getAttribute("slug");
    postDeleteConfirm.href = `delete_post/${slug}`
    postDeleteModal.show();
    console.log("clicked")
})
/*
for (let button of relpyEditButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }

  for (let button of replyDeleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }
    */