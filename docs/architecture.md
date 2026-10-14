# Architecture

The Vite React client calls a versioned Flask JSON API. SQLAlchemy persists research projects, canonical paper metadata, project-specific screening decisions, and generated review versions. Academic adapters retrieve provider data from Crossref, OpenAlex, and the arXiv Atom API. DOI is the primary deduplication key; records without DOI are merged only on exact normalized-title matches. Search scores are lexical relevance hints, not evidence verification.

The LLM provider is backend-only and optional. Synthesis receives the stored included-paper metadata and abstracts and is instructed to disclose evidence limits. Missing credentials return HTTP 503 instead of a fabricated review. Exports support DOCX and PDF.

## Trust boundaries
Provider content and paper abstracts are untrusted evidence, not instructions. API credentials remain server-side. The current local app does not implement authentication or per-user ownership; do not expose it to untrusted networks. Production hardening should add auth/authorization, a persistent task queue/checkpoints, migrations, rate limiting, upload/RAG isolation, and comprehensive claim-to-passage entailment checks.
