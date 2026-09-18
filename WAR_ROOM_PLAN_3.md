# Issue #3: Add Authentication and Fix IDOR Vulnerability

- [x] Add `User` model to `backend/models.py` and associate `Resume` with `User`.
- [x] Add `Flask-JWT-Extended` to `backend/requirements.txt`.
- [x] Initialize `JWTManager` in `backend/app.py`.
- [x] Create `auth.py` in `backend/routes` for `/register` and `/login` endpoints.
- [x] Register `auth` blueprint in `backend/app.py`.
- [ ] Update `backend/routes/resume.py` to use `@jwt_required()` and filter by `current_user` ID.
- [ ] Run backend tests / verify application works.
