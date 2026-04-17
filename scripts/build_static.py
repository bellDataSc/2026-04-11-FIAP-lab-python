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

HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0a0e27">
    <meta name="description" content="Soc Ops - Social Bingo Game. FIAP AI Specialization lab project.">
    <title>Soc Ops - Social Bingo</title>
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #0a0e27;
            color: #e2e8f0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem 1rem;
        }
        .container {
            max-width: 680px;
            width: 100%;
            text-align: center;
        }
        .badge {
            display: inline-block;
            background: rgba(99,102,241,0.15);
            color: #a5b4fc;
            border: 1px solid rgba(99,102,241,0.3);
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 0.35rem 1rem;
            margin-bottom: 1.5rem;
        }
        h1 {
            font-size: clamp(2.5rem, 8vw, 4rem);
            font-weight: 900;
            letter-spacing: -0.02em;
            line-height: 1.1;
            color: #f8fafc;
            margin-bottom: 0.5rem;
        }
        .tagline {
            font-size: 1rem;
            color: #94a3b8;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 2rem;
        }
        .cta-group {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 3rem;
        }
        .btn-primary {
            display: inline-block;
            background: #6366f1;
            color: #fff;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 0.75rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            transition: background 0.2s;
        }
        .btn-primary:hover { background: #4f46e5; }
        .btn-secondary {
            display: inline-block;
            background: transparent;
            color: #a5b4fc;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 0.75rem 2rem;
            border-radius: 8px;
            border: 1px solid rgba(99,102,241,0.4);
            text-decoration: none;
            transition: border-color 0.2s, color 0.2s;
        }
        .btn-secondary:hover { border-color: #6366f1; color: #e0e7ff; }
        .hint {
            font-size: 0.8rem;
            color: #64748b;
            margin-bottom: 3rem;
        }
        .hint code {
            background: rgba(255,255,255,0.06);
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
            font-family: 'Fira Code', 'Courier New', monospace;
        }
        .divider {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.07);
            margin-bottom: 2.5rem;
        }
        .how-to-play h2 {
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #475569;
            margin-bottom: 1.5rem;
        }
        .rules {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 3rem;
        }
        .rule-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 1.25rem 1rem;
            flex: 1;
            min-width: 140px;
            max-width: 180px;
        }
        .rule-number {
            font-size: 1.5rem;
            font-weight: 900;
            color: #6366f1;
            margin-bottom: 0.5rem;
        }
        .rule-text {
            font-weight: 700;
            font-size: 0.9rem;
            color: #f1f5f9;
            margin-bottom: 0.25rem;
        }
        .rule-desc {
            font-size: 0.78rem;
            color: #64748b;
        }
        .stack {
            display: flex;
            gap: 0.75rem;
            justify-content: center;
            flex-wrap: wrap;
        }
        .stack-tag {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 6px;
            padding: 0.4rem 0.9rem;
            font-size: 0.78rem;
            color: #94a3b8;
        }
        .stack-tag span {
            color: #c7d2fe;
            font-weight: 700;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="badge">FIAP AI Specialization Lab</div>
    <h1>SOC OPS</h1>
    <p class="tagline">Social Bingo</p>
    <div class="cta-group">
        <a href="https://github.com/bellDataSc/2026-04-11-FIAP-lab-python" class="btn-primary" target="_blank" rel="noopener">View on GitHub</a>
        <a href="https://github.com/bellDataSc/2026-04-11-FIAP-lab-python#readme" class="btn-secondary" target="_blank" rel="noopener">Documentation</a>
    </div>
    <p class="hint">Run locally with <code>uv run soc-ops</code></p>
    <hr class="divider">
    <div class="how-to-play">
        <h2>How to play</h2>
        <div class="rules">
            <div class="rule-card">
                <div class="rule-number">1</div>
                <p class="rule-text">Find People</p>
                <p class="rule-desc">Search the room for people who match each square</p>
            </div>
            <div class="rule-card">
                <div class="rule-number">2</div>
                <p class="rule-text">Tap Squares</p>
                <p class="rule-desc">Mark a square when you find a match</p>
            </div>
            <div class="rule-card">
                <div class="rule-number">3</div>
                <p class="rule-text">Get 5 in a Row</p>
                <p class="rule-desc">Complete a horizontal, vertical, or diagonal line to win</p>
            </div>
        </div>
    </div>
    <div class="stack">
        <div class="stack-tag"><span>FastAPI</span> Backend</div>
        <div class="stack-tag"><span>HTMX</span> Frontend</div>
        <div class="stack-tag"><span>Jinja2</span> Templates</div>
        <div class="stack-tag"><span>Python</span> 3.13</div>
    </div>
</div>
</body>
</html>
"""


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(HTML, encoding="utf-8")
    print(f"Written {len(HTML):,} characters to {OUTPUT_FILE}")
    print("--- First 5 lines ---")
    for line in HTML.splitlines()[:5]:
        print(line)


if __name__ == "__main__":
    main()
