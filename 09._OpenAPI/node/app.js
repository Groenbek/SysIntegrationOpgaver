import express from "express"

const app = express()

app.use(express.json());

import swaggerUi from "swagger-ui-express"
import swaggerJSDoc from "swagger-jsdoc";


import usersRouter from "./routers/usersRouter.js"
app.use(usersRouter)

const swaggerDefinition = {
    openapi: "3.0.0",
    info: {
        title: "OpenAPI Example API",
        version: "1.0.0",
        description: "A simple Express Users API",
}
};



const options = {
    swaggerDefinition,
    apis: ["./routers/*.js"],
}

app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerJSDoc(options)))



app.listen(8080, () => console.log("Server is running on port 8080"))