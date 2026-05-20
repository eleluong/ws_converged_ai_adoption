"""
modal_server.py — Deploy the AI Adoption Workshop presentation UI to Modal.

Usage:
    modal deploy modal_server.py          # deploy to modal.com
    modal serve modal_server.py           # run locally via Modal tunnel (hot-reload)
"""

from dotenv import load_dotenv
load_dotenv()

import modal
from modal import App, Image, Secret, FilePatternMatcher

# ---------------------------------------------------------------------------
# App definition
# ---------------------------------------------------------------------------
app = App("ai-adoption-workshop-ui")

# ---------------------------------------------------------------------------
# Container image
# - Start from slim Debian + Python 3.12
# - Install Python dependencies from requirements.txt
# - Copy the entire project directory into /app inside the container,
#   excluding heavy/irrelevant directories.
# ---------------------------------------------------------------------------
image = (
    Image.debian_slim(python_version="3.12")
    .pip_install_from_requirements("requirements.txt")
)

image = image.add_local_dir(
    ".",
    "/app",
    copy=True,
    ignore=FilePatternMatcher(
        "**/venv/**",
        "**/.venv/**",
        "**/__pycache__/**",
        "**/.git/**",
        "**/.gemini/**",
        "**/node_modules/**",
    ),
)

# ---------------------------------------------------------------------------
# ASGI endpoint — wraps the FastAPI app defined in main.py
# ---------------------------------------------------------------------------
@app.function(
    image=image,
    timeout=300,
    # Uncomment the line below if you need secrets from a .env file:
    # secrets=[Secret.from_dotenv()],
)
@modal.asgi_app()
def create_app():
    import sys
    sys.path.append("/app")

    from main import app as fastapi_app

    return fastapi_app
