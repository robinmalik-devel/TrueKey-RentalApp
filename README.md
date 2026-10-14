# TrueKey

An AI-powered rental app where every flat is filmed live in the app, every owner and tenant passes KYC, and an AI plus a human verifier check each listing before it goes live.

**Core promise:** live-captured listings, verified owners and tenants, explicit tenant-preference tags (couples, bachelors, pets, safety), and a digital move-in with a signed, photo-backed condition report.

## Stack

- **Backend:** Django 5.2 + Django REST Framework, JWT auth (SimpleJWT), OpenAPI via drf-spectacular
- **Data:** PostgreSQL with pgvector
- **Workers:** Celery + Redis (queues for media processing, AI checks and notifications)
- **AI:** Claude for listing verification and natural-language search
- **Ops:** Docker Compose, Gunicorn/Uvicorn, Sentry

## Repo layout

```
backend/
  requirements/
    base.txt   # runtime dependencies
    dev.txt    # test and lint tools (pytest, ruff, pre-commit)
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements/dev.txt
```

## Status

Phase 1 (week 1, day 1): project scaffolding in progress.
