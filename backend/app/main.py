import uuid
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app import database
from app.config import BASE_URL, CORS_ORIGINS
from app.schemas import LinkInfo, ShortenRequest, ShortenResponse

app = FastAPI(title="Acortador de enlaces")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/shorten", response_model=ShortenResponse)
def shorten(data: ShortenRequest):
    short_code = str(uuid.uuid4())  
    original_url = str(data.original_url)

    database.save_link({
        "short_code": short_code,
        "original_url": original_url,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    return ShortenResponse(
        short_code=short_code,
        original_url=original_url,
        short_url=f"{BASE_URL}/{short_code}",
    )


@app.get("/urls/{short_code}", response_model=LinkInfo)
def link_info(short_code: str):
    item = database.get_link(short_code)
    if item is None:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    return item


@app.get("/{short_code}")
def redirect(short_code: str):
    item = database.get_link(short_code)
    if item is None:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")

    return RedirectResponse(url=item["original_url"], status_code=307)
