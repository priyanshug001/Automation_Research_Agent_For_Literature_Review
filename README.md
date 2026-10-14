# AI Research Agent for Automated Literature Reviews

A research assistant that discovers scholarly works from real academic APIs, stores project/paper records, supports human screening, generates evidence-aware reviews with an optional LLM, and exports reports.

## Current implementation scope
- Flask REST API with SQLite by default and PostgreSQL-compatible SQLAlchemy configuration.
- Real Crossref and OpenAlex search adapters; arXiv adapter is optional and uses its public Atom API.
- Project CRUD, paper discovery, DOI/title deduplication, inclusion decisions, paper analysis, review generation, citation audit, DOCX/PDF export, and health checks.
- React + Vite research workspace with project creation, search, screening, review generation, and export actions.
- Tests for normalization, deduplication, and health endpoints.
- LLM calls are optional and configured on the backend only. Without an LLM key, the app reports that generation is unavailable; it does not fabricate an AI-generated review.

## Requirements
Python 3.11+ recommended; Node.js 20+ recommended. A real Crossref/OpenAlex search can work without an LLM key. Respect provider rate limits and terms.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
python -m backend.run
```
Backend: http://localhost:5000. In another terminal:
```bash
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:5173.

Set `OPENAI_API_KEY` and optionally `LLM_MODEL` in `backend/.env` to enable LLM synthesis. Never put secrets in frontend environment variables. Set `DATABASE_URL` for PostgreSQL. The local version does not implement user authentication; do not expose it publicly or use it for multi-user private data until authentication/authorization is added.

## Tests
```bash
pytest backend/tests
```
```bash
cd frontend && npm test
```

## API (v1)
- `GET /api/v1/health`
- `GET /api/v1/projects`, `POST /api/v1/projects`
- `GET /api/v1/projects/<id>`, `PATCH /api/v1/projects/<id>`, `DELETE /api/v1/projects/<id>`
- `POST /api/v1/projects/<id>/search`
- `GET /api/v1/projects/<id>/papers`
- `PATCH /api/v1/projects/<id>/papers/<paper_id>/decision`
- `POST /api/v1/projects/<id>/review/generate`
- `POST /api/v1/projects/<id>/audit`
- `POST /api/v1/projects/<id>/export?format=docx|pdf`

Responses use JSON and return useful HTTP status codes. Search provider failures are recorded in the response; results from successful sources are retained.

## Architecture and limitations
See [docs/architecture.md](docs/architecture.md) and [docs/deployment.md](docs/deployment.md). This is a functional starter implementation, not yet a fully hardened production multi-user system. It does not claim exhaustive literature coverage, global novelty verification, full LangGraph checkpoints, a persistent task broker, or complete APA/IEEE/MLA/Chicago style fidelity. LLM-generated claims are constrained to discovered records/abstracts, but human verification remains necessary.
