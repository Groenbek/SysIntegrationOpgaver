/* console.log("Hello from Node.js"); */
import express from "express";
const app = express();
const PORT = 8080;
app.listen(PORT, () => console.log("Server started on port ", PORT));

app.get("/date", (req, res) => {
  res.send(new Date());
})

app.get("/datefromfastapi", async (req, res) => {
    const response = await fetch("http://127.0.0.1:8000/date")
    const date = await response.json()
    res.send(date)
})

app.get("/test", async (req, res) => {
    res.send("Hello from Node.js")
})

