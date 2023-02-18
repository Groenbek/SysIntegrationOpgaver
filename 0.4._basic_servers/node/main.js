// To make sure node works, run: npm i
// To run this file: node main.js

const express = require('express');
const app = express();
const fs = require('fs');


const folderPath = './me_files/';

// Route for JSON file
app.get('/mejson', (req, res) => {
    const filePath = folderPath + 'me.json';
    const data = JSON.parse(fs.readFileSync(filePath));
    res.json(data);
  });
  
  // Route for CSV file
  app.get('/mecsv', (req, res) => {
    const filePath = folderPath + 'me.csv';
    const data = fs.readFileSync(filePath, 'utf8');
    res.send(data);
  });
  
  // Route for TXT file
  app.get('/metxt', (req, res) => {
    const filePath = folderPath + 'me.txt';
    const data = fs.readFileSync(filePath, 'utf8');
    res.send(data);
  });
  
  // Route for XML file
  app.get('/mexml', (req, res) => {
    const filePath = folderPath + 'me.xml';
    const data = fs.readFileSync(filePath, 'utf8');
    res.send(data);
  });
  
  // Route for YAML file
  app.get('/meyaml', (req, res) => {
    const filePath = folderPath + 'me.yaml';
    const data = fs.readFileSync(filePath, 'utf8');
    res.send(data);
  });

// TEST WITH DUMMY DATA
/* const data = {
  name: 'Leopold',
  age: 28,
  hobbies: ['Music', 'Programming', 'Singing']

  app.get('/me', (req, res) => {
  res.json(data);
});
}; */



app.listen(3000, () => {
  console.log('Server started on port 3000');
});
