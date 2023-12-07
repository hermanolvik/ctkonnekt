document.addEventListener('DOMContentLoaded', function() {

    // 'Like' button functionality
    var likeButtons = document.querySelectorAll('.like-btn');
    if (likeButtons) {
        likeButtons.forEach(function (btn) {
            btn.addEventListener('click', function (e) {
                e.stopPropagation();  // Prevent the event from bubbling up

                var postId = btn.parentElement.parentElement.getAttribute('data-post-id');
                var isActive = btn.classList.contains('active');

                // Toggle the active class
                btn.classList.toggle('active', !isActive);

                // Send the like/unlike request to the server
                fetch('/like_post/' + postId, {
                    method: 'POST',
                    // Add any necessary headers, CSRF tokens, etc.
                })
                    .then(response => response.json())
                    .then(data => {
                        btn.parentElement.querySelector('.like-count').innerHTML = data.likes_count;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            });
        });
    }

});