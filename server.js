const express = require('express');
const app = express();

app.use(express.static('src'));

app.listen(3344, () => {
    console.log('Server is running on port 3344');
});