"""
main.py — FastAPI app that serves the static presentation UI (index.html).
All assets (index.html, template.html, etc.) are embedded at build time via
the Modal image, so the single-page app is available at the root path.
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="AI Adoption Workshop — Presentation Hub")

# Base directory where all files were copied into the image
BASE_DIR = "/app" if os.path.exists("/app") else os.path.dirname(os.path.abspath(__file__))


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main presentation UI."""
    index_path = os.path.join(BASE_DIR, "index.html")
    return FileResponse(index_path, media_type="text/html")


@app.get("/template.html", response_class=HTMLResponse)
async def template():
    """Serve the template HTML if needed."""
    template_path = os.path.join(BASE_DIR, "template.html")
    return FileResponse(template_path, media_type="text/html")


@app.get("/health")
async def health():
    """Health-check endpoint."""
    return {"status": "ok"}
