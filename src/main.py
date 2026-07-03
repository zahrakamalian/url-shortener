from fastapi import FastAPI
from src.api.v1.redirect import router as redirect_router
from src.api.v1.url import router as url_router

app = FastAPI(
    title="URL Shortener"
)

app.include_router(redirect_router, tags=["redirect"])
app.include_router(url_router, prefix="/urls", tags=["URL & Log"])


@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"
