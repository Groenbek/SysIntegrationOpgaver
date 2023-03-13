import { Router } from "express";
const router = Router();

const users= [{
    id: 1,
    name: "John Doe",
}]

/**
* @openapi
* /api/users:
*   get:
*     description: Get all users!
*     responses:
*       200:
*         description: Returns all users.
*/

router.get("/api/users", (req, res) => {
    res.send({data: users})
});

/**
* @openapi
* /api/users:
*   post:
*     description: Create a new users!
*     responses:
*       200:
*         description: Returns the user that was created.
*/

router.post("/api/users", (req, res) => {
    const user = req.body;
    users.push(user);
    res.send({data: user})
});


const spaceships= [{
    id: 1,
    name: "Starship Enterprise",
}]

/**
* @openapi
* /api/spaceships:
*   get:
*     description: Load all your favorite spaceships!
*     responses:
*       200:
*         description: Returns all the spaceships ever launched!
*/

router.get("/api/spaceships", (req, res) => {
    res.send({data: spaceships})
});

export default router;