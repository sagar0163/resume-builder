# Plan for Issue 1: Fix N+1 Query Problem in Resume Retrieval

- [x] Inspect `backend/routes/resume.py` and identify the `get_resume` endpoint.
- [x] Update `get_resume` query to use `selectinload` for `personal_info`, `experiences`, `education`, `skills`, `certifications`, `languages`, `projects`.
- [x] Run tests to verify the changes.
- [x] Finalize and clean up plan file.
