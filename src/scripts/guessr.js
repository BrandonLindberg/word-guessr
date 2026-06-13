document.getElementById('guess-button').addEventListener('click', buttonQuery);

let attemptCounter = 0;

async function buttonQuery() {
    const input = document.getElementById('guess-input');
    let guess = input.value.trim();
    input.value = '';
    
    if (!guess) return;

    attemptCounter++;
    const counter = document.getElementById('attempts-text');
    counter.innerHTML = `Attempts: ${attemptCounter}`;

    const response = await fetch(`/crunch?word=${encodeURIComponent(guess)}`);

    const data = await response.json();
    queryResult(data.score, guess);

    // console.log(data);
};

function queryResult(result, guess) {
    const resultText = document.getElementById('result-num');
    const resultNum = result;

    if (resultNum <= 0.2){
        resultText.innerHTML = 'Freezing';
    }

    else if (resultNum <= 0.4){
        resultText.innerHTML = 'Cold';
    }

    else if (resultNum <= 0.6){
        resultText.innerHTML = 'Lukewarm';
    }

    else if (resultNum <= 0.8){
        resultText.innerHTML = 'Hot';
    }
    else if (resultNum < 0.99){
        resultText.innerHTML = 'Burning Up';
    }
    else {
        resultText.innerHTML = `Correct! Word was: ${guess}`;
    }
}