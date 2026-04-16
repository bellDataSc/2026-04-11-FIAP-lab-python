"""build_static.py

Generates a static index.html for GitHub Pages deployment by rendering
the Jinja2 home template with a default GameSession.

Must be run from the repository root directory.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure the repo root is on sys.path so that `app` is importable
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from jinja2 import Environment, FileSystemLoader  # noqa: E402

from app.models import GameState  # noqa: E402
from app.game_service import GameSession  # noqa: E402

REPO_NAME = "2026-04-11-FIAP-lab-python"
TEMPLATES_DIR = REPO_ROOT / "app" / "templates"
OUTPUT_FILE = REPO_ROOT / "_site" / "index.html"


def url_for(name: str, path: str = "") -> str:
    """Replicate FastAPI url_for for static assets on GitHub Pages."""
    if name == "static":
        return f"/{REPO_NAME}/app/static/{path}"
    return path


def main() -> None:
    print(f"Templates dir : {TEMPLATES_DIR}")
    print(f"Output file   : {OUTPUT_FILE}")

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=True,
    )

    session = GameSession()
    template = env.get_template("home.html")
    html = template.render(
        session=session,
        GameState=GameState,
        url_for=url_for,
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html, encoding="utf-8")

    print(f"Written {len(html):,} characters to {OUTPUT_FILE}")
    print("--- First 10 lines ---")
    for line in html.splitlines()[:10]:
        print(line)


if __name__ == "__main__":
    main()
