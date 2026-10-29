from pydantic import BaseModel, HttpUrl


class ShortenRequest(BaseModel):
    original_url: HttpUrl  # valida que sea una URL correcta (http/https)


class ShortenResponse(BaseModel):
    short_code: str
    original_url: str
    short_url: str


class LinkInfo(BaseModel):
    short_code: str
    original_url: str
    created_at: str
