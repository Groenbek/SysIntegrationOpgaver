const date = new Date();
console.log(date);

console.log(Date)

console.log(date.getTime())


/* Specific region obviously*/
console.log(new Intl.DateTimeFormat('en-US').format(date))
console.log(new Intl.DateTimeFormat('da-DK').format(date))