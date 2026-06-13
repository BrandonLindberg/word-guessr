document.getElementById('guess-button').addEventListener('click', buttonQuery);
document.getElementById('guess-input')

async function buttonQuery() {
    const input = document.getElementById('guess-input')
    let guess = input.value.trim();
    
    if (!guess) return;

    const response = await fetch(`http://10.34.144.180:8000/crunch?word=${guess}`);

    input.value = '';

    const data = await response.json();
    console.log(data);
};