# ci-demo

Small Flask app for practicing CI/CD with GitHub Actions.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python -m app.main            # http://localhost:8000/health
```

## Checks (these are the commands your CI must run)

```bash
ruff check .
pytest
```

## Docker

```bash
docker build -t ci-demo .
docker run --rm -p 8000:8000 ci-demo
curl localhost:8000/health
```
