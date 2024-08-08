const postDeleteModal = new bootstrap.Modal(document.getElementById("post-delete-modal"));
const postDeleteButton = document.getElementById("post-btn-delete");
const postDeleteConfirm = document.getElementById("post-delete-confirm");
const replyDeleteModal = new bootstrap.Modal(document.getElementById("reply-delete-modal"));
const relpyEditButtons = document.getElementsByClassName("reply-btns-edit");
const replyDeleteButtons = document.getElementsByClassName("reply-btn-delete");
const replyDeleteConfirm = document.getElementById("reply-delete-confirm");


postDeleteButton.addEventListener("click", (e) => {
    let slug=e.target.getAttribute("slug");
    postDeleteConfirm.href = `delete_post/${slug}`
    postDeleteModal.show();
    console.log("clicked")
})

for (let button of relpyEditButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply-id");
      commentForm.setAttribute("action", `edit_reply/${replyId}`);
    });
  }

for (let button of replyDeleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment-id");
      deleteConfirm.href = `/board/delete_comment/${commentId}`;
      deleteModal.show();
    });
  }