// 1 READ CSV FILE
const fs = require("fs");

fs.readFile("me.csv", "utf8", (err, data) => {
  if (err) throw err;

  const lines = data.split("\n");
  const header = lines[0].split(",");
  const values = lines[1].split(",");

  const result1 = {};
  header.forEach((item, index) => {
    result1[item] = values[index];
  });
  console.log("Reading CSV file...\n" + result1);
});

// 2 READ JSON FILE
fs.readFile("me.json", "utf8", (err, data) => {
  if (err) throw err;

  const result2 = JSON.parse(data);

  console.log("Reading JSON file...\n" + result2);
});

// 3 READ TXT FILE
fs.readFile("me.txt", "utf8", (err, data) => {
  if (err) throw err;

  const lines = data.split("\n");
  const result3 = {};

  for (const line of lines) {
    const [key, value] = line.split(": ");
    result3[key] = value;
  }

  console.log("Reading TXT file...\n" + result3);
});

// 4 READ XML FILE
const xml2js = require("xml2js");

fs.readFile("me.xml", "utf8", (err, data) => {
  if (err) throw err;

  xml2js.parseString(data, (err, result4) => {
    if (err) throw err;

    console.log("Reading XML file...\n" + result4);
  });
});

// 5 READ YAML FILE
const yaml = require("js-yaml");

fs.readFile("me.yaml", "utf8", (err, data) => {
  if (err) throw err;

  try {
    const doc = yaml.load(data);
    console.log(doc);
  } catch (e) {
    console.error(e);
  }
});
