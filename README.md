# Soc Ops — Social Bingo

This repository is part of an ongoing specialization curriculum at FIAP, focused on Artificial Intelligence and advanced software engineering.

The project serves as the starting point for a practical learning track on AI agent development using GitHub Copilot, VS Code, and Python. The lab was originally designed by the GitHub Copilot Dev Days team and is being extended here as a personal study artifact.

## About the Project

Soc Ops is a Social Bingo web application built for in-person networking events. Players find colleagues who match the questions on their bingo card and aim to complete five in a row.

The application is built with FastAPI, Jinja2 templates, and HTMX for dynamic interactions, running on Python 3.13.

## Learning Objectives

This project is used to develop and document the following skills:

- Applied use of GitHub Copilot in agent mode for software development
- Context engineering and prompt design for AI-assisted coding
- Design-first frontend development with HTMX
- Multi-agent orchestration patterns in Python
- CI/CD pipeline configuration with GitHub Actions

## Lab Guide

| Part | Title |
|------|-------|
| [00](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview and Checklist |
| [01](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup and Context Engineering |
| [02](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend |
| [03](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master |
| [04](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development |

Lab guides are also available in the [`workshop/`](workshop/) directory for offline reference.

## Project Structure

```
.
├── app/                    # FastAPI application
│   ├── main.py             # Application entry point and route definitions
│   ├── models.py           # Data models and game state
│   ├── game_service.py     # Session and game logic orchestration
│   ├── game_logic.py       # Core game rules
│   ├── data.py             # Questions dataset
│   ├── static/             # CSS, JS, and static assets
│   └── templates/          # Jinja2 HTML templates
├── tests/                  # Test suite (pytest)
├── .github/
│   ├── workflows/
│   │   ├── ci.yml          # Continuous integration: lint and test
│   │   └── deploy.yml      # GitHub Pages deployment
│   ├── agents/             # Copilot agent definitions
│   ├── instructions/       # Copilot custom instructions
│   └── prompts/            # Reusable prompt files
├── workshop/               # Offline lab guide
├── pyproject.toml          # Project metadata and dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Running Locally

```bash
# Install dependencies
uv sync

# Start the development server
uv run soc-ops
```

The application will be available at `http://localhost:8000`.

### Running Tests

```bash
uv run pytest
```

### Linting

```bash
uv run ruff check .
```

## Deployment

The application deploys a static preview to GitHub Pages on every push to `main`.

**Required setup (one-time):** GitHub Pages must be enabled in the repository settings under Settings > Pages > Source, selecting "GitHub Actions" as the build and deployment source. Without this configuration, the deployment workflow will fail with `HttpError: Not Found`.

## References

- [GitHub Copilot Agent Mode — GitHub Blog](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/)
- [VS Code Copilot Agent Lab — Quick Reference](https://copilot-dev-days.github.io/agent-lab-python/step.html?step=guide)
- [Original Lab Repository — copilot-dev-days/agent-lab-python](https://github.com/copilot-dev-days/agent-lab-python)

## License

MIT
