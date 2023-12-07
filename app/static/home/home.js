document.addEventListener('DOMContentLoaded', function() {
    let helloAnimation = lottie.loadAnimation({
        container: document.getElementById('lottie-hello-animation'), // the DOM element that will contain the animation
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: '/static/hello_animation.json' // the path to the animation file
    });
});