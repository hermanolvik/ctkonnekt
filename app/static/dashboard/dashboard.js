document.addEventListener('DOMContentLoaded', function() {


    // Make posts clickable and link to view_post
    var posts = document.querySelectorAll('.post');
    posts.forEach(function(post) {
        post.addEventListener('click', function() {
            var postId = post.getAttribute('data-post-id');
            window.location.href = '/post/' + postId;
        });
    });


    // 'Like' button functionality
    var likeButtons = document.querySelectorAll('.like-btn');
    likeButtons.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
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
                    if (!isActive) {
                        btn.parentElement.querySelector('.like-count').innerHTML++;
                    } else {
                        btn.parentElement.querySelector('.like-count').innerHTML--;
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });


});