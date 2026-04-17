"""build_static.py

Generates a self-contained static index.html for GitHub Pages deployment.
This page is a landing page for the project - the game itself requires a
running FastAPI server and cannot be deployed as static HTML.

Must be run from the repository root directory.
"""
from __future__ import annotations

from pathlib import Path

REPO_NAME = "2026-04-11-FIAP-lab-python"
REPO_URL = "https://github.com/bellDataSc/2026-04-11-FIAP-lab-python"
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "_site" / "index.html"
STATIC_BASE = f"/{REPO_NAME}/app/static"

HTML = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0a0e27">
    <meta name="description" content="Soc Ops - Social Bingo Game. FIAP AI Specialization lab project.">
    <title>Soc Ops - Social Bingo</title>
    <link rel="stylesheet" href="{STATIC_BASE}/css/app.css">
    <link rel="icon" type="image/png" href="{STATIC_BASE}/favicon.png">
</head>
<body>
<div id="app">
<div id="game-container">
<div class="flex flex-col min-h-full start-container">

  <!-- Hero Section -->
  <section class="hero-section" style="min-height: 40vh; padding: 3rem 1.5rem 1rem;">
    <h1 class="hero-headline">SOC OPS</h1>
    <p class="hero-tagline">SOCIAL BINGO</p>
    <div class="hero-accent"></div>
  </section>

  <!-- Rules Section -->
  <h2 class="how-to-play-heading">How to play</h2>
  <section class="rules-section">
    <div class="rule-card">
      <div class="rule-number">1</div>
      <p class="rule-text">Find People</p>
      <p class="rule-description">Search the room for people who match each square</p>
    </div>
    <div class="rule-card">
      <div class="rule-number">2</div>
      <p class="rule-text">Tap Squares</p>
      <p class="rule-description">Mark a square when you find a match</p>
    </div>
    <div class="rule-card">
      <div class="rule-number">3</div>
      <p class="rule-text">Get 5 in a Row</p>
      <p class="rule-description">Complete a horizontal, vertical, or diagonal line to win</p>
    </div>
  </section>

  <!-- Stats Section -->
  <section class="stats-section">
    <div class="stat-box">
      <span class="stat-number">FastAPI</span>
      <span class="stat-label">Backend</span>
    </div>
    <div class="stat-box">
      <span class="stat-number">HTMX</span>
      <span class="stat-label">Frontend</span>
    </div>
    <div class="stat-box">
      <span class="stat-number">Jinja2</span>
      <span class="stat-label">Templates</span>
    </div>
    <div class="stat-box">
      <span class="stat-number">Python</span>
      <span class="stat-label">3.13</span>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="cta-container">
    <a href="{REPO_URL}" target="_blank" rel="noopener"
       class="dominant-cta"
       style="text-decoration: none; display: inline-block; text-align: center;">
      View on GitHub
    </a>
    <p class="scroll-hint" style="margin-top: 1.5rem;">
      Run locally with &nbsp;<code style="color: var(--color-neon-cyan); font-family: var(--font-mono);">uv run soc-ops</code>
    </p>
  </section>

</div>
</div>
</div>
</body>
</html>
"""


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(HTML, encoding="utf-8")
    print(f"Written {{len(HTML):,}} characters to {{OUTPUT_FILE}}")
    print("--- First 5 lines ---")
    for line in HTML.splitlines()[:5]:
        print(line)


if __name__ == "__main__":
    main()
