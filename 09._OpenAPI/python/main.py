from fastapi import FastAPI

app = FastAPI()

from routers.spacecraft_router import router as spacecraft_router
app.include_router(spacecraft_router)