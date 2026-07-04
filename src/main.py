from fastapi import FastAPI
from src.api.v1.redirect import router as redirect_router
from src.api.v1.url import router as url_router
from src.api.v1.analytics import router as analytics_router

app = FastAPI(
    title="URL Shortener app"
)

app.include_router(url_router, prefix="/urls", tags=["URL shortener & Log"])
app.include_router(redirect_router, tags=["Redirect"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])


@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"
