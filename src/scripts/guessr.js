document.getElementById('guess-button').addEventListener('click', buttonQuery);

async function buttonQuery() {
    const response = await fetch('/crunch');

    const data = await response.json();
    console.log(data);
};