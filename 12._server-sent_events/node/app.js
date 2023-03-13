import  express from "express"
const app = express()

app.use(express.static("public"))

app.get("/time", (req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    })

    setInterval(() => sendTimeToClient(res), 1000)
});

function sendTimeToClient(res) {
    const time = new Date().toTimeString()
    res.write(`data: ${time}\n\n`)
}


const port = 8080;
app.listen(port, () => { console.log(`Listening on port ${port}`)
}) 