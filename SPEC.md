# Resume Builder - Technical Specification

## Project Overview
- **Name**: Resume Builder
- **Type**: Full-stack Web Application
- **Core Functionality**: Create professional resumes with multiple templates, export to PDF
- **Target Users**: Job seekers, students, professionals

## Tech Stack
- **Backend**: Python Flask
- **Database**: SQLite (SQLAlchemy)
- **PDF Generation**: WeasyPrint / pdfkit
- **Frontend**: Vue.js 3 + TailwindCSS

## Features

### 1. Resume Management
- Create multiple resumes
- Edit resume details
- Duplicate resumes
- Delete resumes

### 2. Resume Sections
- Personal Information
- Professional Summary
- Work Experience (multiple)
- Education (multiple)
- Skills (with proficiency levels)
- Certifications
- Languages
- Projects
- Awards & Achievements

### 3. Templates
- Modern (clean, minimal)
- Classic (traditional)
- Creative (colorful, unique)

### 4. Export
- PDF export
- JSON export/import

### 5. Preview
- Live preview while editing
- Multiple template previews

## Data Model

### Resume
```python
{
    id: int,
    name: str,
    template: str,
    created_at: datetime,
    updated_at: datetime
}
```

### PersonalInfo
```python
{
    resume_id: int,
    full_name: str,
    email: str,
    phone: str,
    address: str,
    linkedin: str,
    github: str,
    website: str,
    summary: str
}
```

### Experience
```python
{
    resume_id: int,
    company: str,
    position: str,
    start_date: str,
    end_date: str,
    current: bool,
    description: str
}
```

### Education
```python
{
    resume_id: int,
    institution: str,
    degree: str,
    field: str,
    start_date: str,
    end_date: str,
    gpa: str
}
```

### Skill
```python
{
    resume_id: int,
    name: str,
    proficiency: str  # beginner, intermediate, advanced, expert
}
```

## API Endpoints

### Resumes
- GET /api/resumes - List all resumes
- POST /api/resumes - Create resume
- GET /api/resumes/{id} - Get resume
- PUT /api/resumes/{id} - Update resume
- DELETE /api/resumes/{id} - Delete resume

### PDF Export
- GET /api/resumes/{id}/pdf - Export to PDF

### Templates
- GET /api/templates - List templates

## Acceptance Criteria
1. Users can create/edit/delete resumes
2. All resume sections are editable
3. Live preview works
4. PDF export generates valid PDF
5. Multiple templates available
6. Responsive UI works on mobile
