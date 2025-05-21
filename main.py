from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import newspaper
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class URLRequest(BaseModel):
    url: str

@app.get("/")
async def main():
    return FileResponse("./static/summarizer.html")

@app.post("/resumir")
async def resumir(request: URLRequest):
    article = newspaper.Article(request.url)
    article.download()
    article.parse()
    text = article.text

    if not text:
        return {"resumen": "No se pudo extraer el contenido de la página."}

    resumen = summarizer(text[:1024], max_length=500, min_lenght=100, do_sample=False)
    return {"resumen": resumen[0]['summary_text']}
