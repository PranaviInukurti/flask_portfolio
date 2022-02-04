// ------- nighthawkcsp code -------
const search = document.getElementById('search');
const google = 'https://www.google.com/search?q=';

function submitted(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        const url = google
            + search.value;
        const win = window.open(url, '_blank');
        win.focus();
    }
}
search.addEventListener('keypress', submitted);