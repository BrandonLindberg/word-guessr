const express = require('express');
const app = express();

app.use(express.static('src'));

app.get('/crunch', async (req, res) => {
    const word = req.query.word;
    
    const response = await fetch(`http://10.34.144.180:8000/crunch?word=${encodeURIComponent(word)}`);
    const data = await response.json();
    res.json(data);
});


app.listen(3344, () => {
    console.log('Server is running on port 3344');
});