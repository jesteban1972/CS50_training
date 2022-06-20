window.onpopstate = function(event) {
    console.log(event.state.section);
    showSection(event.state.section);
}

function showSection(section) { // Shows given section

    // Find section text from server
    fetch(`/singlepage/sections/${section}`)
        .then(response => response.text())
        .then(text => {
            console.log(text);
            document.querySelector('#content').innerHTML = text;
        });
}

window.onscroll = () => { // Event listener for scrolling

    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) { // Check if we're at the bottom

        document.querySelector('body').style.background = 'rgb(2, 0, 36)';
        document.querySelector('body').style.backgroundImage = 'linear-gradient(135deg, rgba(2, 0,36, 1) 0%, rgba(9, 9, 121, 1) 64%, rgba(0, 212, 255, 1) 100%)';
        document.querySelector('body').style.backgroundAttachment = 'fixed';
    } else {

        document.querySelector('body').style.background = 'rgb(2, 0, 36)';
        document.querySelector('body').style.backgroundImage = 'linear-gradient(135deg, rgba(0, 212, 255, 1) 100%, rgba(9, 9, 121, 1) 64%, rgba(2, 0,36, 1) 0%)';
        document.querySelector('body').style.backgroundAttachment = 'fixed';
    }
};

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const section = this.dataset.section;

            // Add the current state to the history
            history.pushState({section: section}, "", `section${section}`);
            showSection(section);
        };
    });
});