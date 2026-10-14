# Deployment

Use Python 3.11+ and Node.js 20+. Configure secrets in the host's secret manager; never commit `.env`. Set `DATABASE_URL` to a managed PostgreSQL connection string for persistent production storage. Run the backend using `gunicorn --chdir backend 'run:app'` (verify the working directory/module path for your deployment platform). Build the frontend with `cd frontend && npm ci && npm run build`.

For local use, SQLite is created automatically. This initial implementation does not include a persistent queue, authentication, or persistent object storage. Consequently, treat it as a local/single-user development app until those controls are added. Academic APIs may rate-limit requests; provider failures are returned per source, and successful-source results remain usable.
