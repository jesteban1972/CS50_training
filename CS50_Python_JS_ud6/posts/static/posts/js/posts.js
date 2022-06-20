let counter = 1; // Start with first post

const quantity = 20; // Load posts 20 at a time

document.addEventListener('DOMContentLoaded', function() {

    load(); // When DOM loads, render the first 20 posts

    const h1 = document.querySelector('h1'); // Find heading

    h1.style.animationPlayState = 'paused'; // Pause Animation by default

    document.querySelector('button').onclick = () => { // Wait for button to be clicked

        // If animation is currently paused, begin playing it
        if (h1.style.animationPlayState == 'paused') {
            h1.style.animationPlayState = 'running';
        }

        // Otherwise, pause the animation
        else {
            h1.style.animationPlayState = 'paused';
        }
    }
});

window.onscroll = () => { // If scrolled to bottom, load the next 20 posts
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

function load() { // Load next set of posts

    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add posts
    fetch(`/posts/posts?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            data.posts.forEach(add_post);
        })
}

function add_post(contents) { // Add a new post with given contents to DOM

    // Create new post
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `${contents} <button class="hide">Hide</button>`;

    // Add post to DOM
    document.querySelector('#posts').append(post);
}

document.addEventListener('click', event => {
    const element = event.target;

    if (element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () => {
            element.parentElement.remove();
        });
    }
})