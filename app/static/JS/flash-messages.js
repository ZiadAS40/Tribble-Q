document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelector('.flash-messages');

    if (flashMessages) {
        setTimeout(function() {
            console.log(flashMessages);
            flashMessages.style.display = 'none';
        }, 5000);
    }
});