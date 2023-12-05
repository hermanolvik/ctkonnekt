document.addEventListener('DOMContentLoaded', function() {

    // Make posts clickable and link to view_post
    var posts = document.querySelectorAll('.post');
    posts.forEach(function(post) {
        post.addEventListener('click', function() {
            var postId = post.getAttribute('data-post-id');
            window.location.href = '/post/' + postId;
        });
    });

});