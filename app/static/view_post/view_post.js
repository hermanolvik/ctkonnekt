document.addEventListener('DOMContentLoaded', function() {

    // Comment deletion
    var deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var commentDiv = button.closest('.comment');
            var commentId = commentDiv.getAttribute('data-comment-id');

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

    // Comment editing
    var editButtons = document.querySelectorAll('.edit-btn');
    var saveEditButtons = document.querySelectorAll('.save-edit-btn');
    var cancelEditButtons = document.querySelectorAll('.cancel-edit-btn');

    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var commentDiv = button.closest('.comment');
            var displayContent = commentDiv.querySelector('.comment-content');
            var editContent = commentDiv.querySelector('.edit-comment-content');
            displayContent.style.display = 'none';
            editContent.style.display = 'block';
            button.style.display = 'none'; // hide edit button
            commentDiv.querySelector('.save-edit-btn').style.display = 'block';
            commentDiv.querySelector('.cancel-edit-btn').style.display = 'block';
        });
    });

    saveEditButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var commentDiv = button.closest('.comment');
            var commentId = commentDiv.getAttribute('data-comment-id');
            var newContent = commentDiv.querySelector('.edit-comment-content').value;

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

    // Cancel editing
    cancelEditButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var commentDiv = button.closest('.comment');
            commentDiv.querySelector('.comment-content').style.display = 'block';
            commentDiv.querySelector('.edit-comment-content').style.display = 'none';
            commentDiv.querySelector('.edit-btn').style.display = 'block';
            commentDiv.querySelector('.save-edit-btn').style.display = 'none';
            button.style.display = 'none'; // hide cancel button
        });
    });

});