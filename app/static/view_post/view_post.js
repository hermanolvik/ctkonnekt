document.addEventListener('DOMContentLoaded', function() {

    // Comments deletion script
    let deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            let commentDiv = button.closest('.comment');
            let commentId = commentDiv.getAttribute('data-comment-id');

            fetch('/delete_comment/' + commentId, {
                method: 'DELETE',
                // Add headers, CSRF tokens, etc.
            })
                .then(response => {
                    if (response.ok) {
                        commentDiv.remove(); // Remove the comment div from the DOM
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });


    // Comments editing functionality
    let editButtons = document.querySelectorAll('.edit-btn');
    let saveEditButtons = document.querySelectorAll('.save-edit-btn');
    let cancelEditButtons = document.querySelectorAll('.cancel-edit-btn');

    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            let commentDiv = button.closest('.comment');
            let displayContent = commentDiv.querySelector('.comment-content');
            let editContent = commentDiv.querySelector('.edit-comment-content');
            displayContent.style.display = 'none';
            editContent.style.display = 'block';
            button.style.display = 'none'; // hide edit button
            commentDiv.querySelector('.save-edit-btn').style.display = 'block';
            commentDiv.querySelector('.cancel-edit-btn').style.display = 'block';
        });
    });

    saveEditButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            let commentDiv = button.closest('.comment');
            let commentId = commentDiv.getAttribute('data-comment-id');
            let newContent = commentDiv.querySelector('.edit-comment-content').value;

            fetch('/edit_comment/' + commentId, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // Include CSRF token and other necessary headers
                },
                body: JSON.stringify({ content: newContent })
            })
                .then(response => response.json())
                .then(data => {
                    commentDiv.querySelector('.comment-content').textContent = newContent;
                    // Reset view
                    commentDiv.querySelector('.comment-content').style.display = 'block';
                    commentDiv.querySelector('.edit-comment-content').style.display = 'none';
                    commentDiv.querySelector('.edit-btn').style.display = 'block';
                    button.style.display = 'none'; // hide save button
                    commentDiv.querySelector('.cancel-edit-btn').style.display = 'none';
                })
                .catch(error => console.error('Error:', error));
        });
    });


    // Cancel comment editing script
    cancelEditButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            let commentDiv = button.closest('.comment');
            commentDiv.querySelector('.comment-content').style.display = 'block';
            commentDiv.querySelector('.edit-comment-content').style.display = 'none';
            commentDiv.querySelector('.edit-btn').style.display = 'block';
            commentDiv.querySelector('.save-edit-btn').style.display = 'none';
            button.style.display = 'none'; // hide cancel button
        });
    });


    // Script for editing the post
    let editPostButton = document.querySelector('.edit-post-btn');
    editPostButton.addEventListener('click', function() {
        let postDiv = editPostButton.closest('.post-view');
        let postId = postDiv.getAttribute('data-post-id');
        let postTitle = postDiv.querySelector('h3').textContent;
        let postContent = postDiv.querySelector('p').textContent;

        // Populate the edit modal fields
        document.getElementById('editPostId').value = postId;
        document.getElementById('editPostTitle').value = postTitle;
        document.getElementById('editPostContent').textContent = postContent;

        // Show the edit modal
        let editModal = new bootstrap.Modal(document.getElementById('editPostModal'));
        editModal.show();
    });


    // Post deletion script
    let deletePostBtn = document.querySelector('.delete-post-btn');
    deletePostBtn.addEventListener('click', function() {
        let postDiv = editPostButton.closest('.post-view');
        let postId = postDiv.getAttribute('data-post-id');

        fetch('/delete_post/' + postId, {
            method: 'DELETE',
            // Add headers, CSRF tokens, etc?
        })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/dashboard'
                }
            })
            .catch(error => console.error('Error:', error));
    });

});