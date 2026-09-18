# Issue #3: Add Authentication and Fix IDOR Vulnerability

- [x] Add `User` model to `backend/models.py` and associate `Resume` with `User`.
- [x] Add `Flask-JWT-Extended` to `backend/requirements.txt`.
- [ ] Initialize `JWTManager` in `backend/app.py`.
- [ ] Create `auth.py` in `backend/routes` for `/register` and `/login` endpoints.
- [ ] Register `auth` blueprint in `backend/app.py`.
- [ ] Update `backend/routes/resume.py` to use `@jwt_required()` and filter by `current_user` ID.
- [ ] Run backend tests / verify application works.
