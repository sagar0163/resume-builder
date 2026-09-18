# Issue #2: Implement Rate Limiting on AI Endpoints

- [x] Add `Flask-Limiter` to `requirements.txt`.
- [x] Initialize `Flask-Limiter` in `backend/app.py` or a new `extensions.py` file.
- [x] Apply rate limiting to `backend/routes/ai.py` (5 requests per minute per IP).
- [ ] Update `API.md` to document the new AI endpoints and their rate limits.
- [ ] Create tests to verify rate limiting on `/api/ai/parse`, `/api/ai/score`, `/api/ai/rephrase`, `/api/ai/cover-letter` (optional, since test suite is not explicitly requested, but good to check if they exist or just rely on manual tests via curl or a quick test script).
- [ ] Verify everything works.
