const express = require('express');
const app = express();

app.use(express.static('src'));

app.get('/crunch', async (req, res) => {
    const response = await fetch('http://10.34.144.180:8000/crunch?word1=ocean&word2=water');

    const data = await response.json();
    res.json(data);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});