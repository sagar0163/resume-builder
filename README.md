# Resume Builder

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/python-3.11+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/vue-3-green.svg" alt="Vue">
</p>

Create professional resumes with multiple templates. Export to PDF.

## Features

- Create multiple resumes
- Personal information management
- Work experience entries
- Education history
- Skills with proficiency levels
- Live preview
- Multiple templates

## Quick Start

### Backend

```bash
cd backend
pip install -r requirements.txt
python server.py
```

Server runs on http://localhost:5000

### Frontend

Open `frontend/index.html` in your browser, or serve it:

```bash
cd frontend
npx serve .
```

## Tech Stack

- **Backend**: Python Flask + SQLAlchemy
- **Database**: SQLite
- **Frontend**: Vue.js 3 + TailwindCSS

## API Endpoints

- `GET /api/resumes` - List resumes
- `POST /api/resumes` - Create resume
- `GET /api/resumes/{id}` - Get resume
- `PUT /api/resumes/{id}` - Update resume
- `DELETE /api/resumes/{id}` - Delete resume
- `GET /api/templates` - List templates

## License

MIT
