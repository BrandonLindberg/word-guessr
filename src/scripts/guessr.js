document.getElementById('guess-button').addEventListener('click', buttonQuery);
document.getElementById('guess-input')

async function buttonQuery() {
    const input = document.getElementById('guess-input')
    let guess = input.value.trim();
    
    if (!guess) return;

    const response = await fetch(`/crunch?word=${encodeURIComponent(guess)}`);

    input.value = '';

    const data = await response.json();
    console.log(data);
};