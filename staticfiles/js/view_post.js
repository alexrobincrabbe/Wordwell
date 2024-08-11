const postDeleteModal = new bootstrap.Modal(document.getElementById("post-delete-modal"));
const replyDeleteModal = new bootstrap.Modal(document.getElementById("reply-delete-modal"));

const postDeleteButton = document.getElementById("post-btn-delete");
const postDeleteConfirm = document.getElementById("post-delete-confirm");
const replyDeleteButtons = document.getElementsByClassName("reply-btn-delete");
const replyDeleteConfirm = document.getElementById("reply-delete-confirm");
console.log(replyDeleteButtons)

postDeleteButton.addEventListener("click", (e) => {
    let slug=e.target.getAttribute("slug");
    postDeleteConfirm.href = `delete_post/${slug}`
    postDeleteModal.show();
})

for (let button of replyDeleteButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply-id");
      let slug = e.target.getAttribute("slug")
      replyDeleteConfirm.href = `/board/delete_reply/${slug}/${replyId}`;
      replyDeleteModal.show();
    });
  }