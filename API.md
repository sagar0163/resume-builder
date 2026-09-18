# Resume Builder API

## Base URL
```
http://localhost:5000/api
```

## Endpoints

### Resumes

#### Get All Resumes
```
GET /resumes
Response: [{ id, name, template, created_at, updated_at }]
```

#### Create Resume
```
POST /resumes
Body: { name: "My Resume" }
Response: { id, name, template }
```

#### Get Resume
```
GET /resumes/:id
Response: { id, name, template, personal_info, experiences, education, skills, ... }
```

#### Update Resume
```
PUT /resumes/:id
Body: { name: "New Name", template: "modern" }
```

#### Delete Resume
```
DELETE /resumes/:id
```

### Personal Info

#### Update Personal Info
```
PUT /resumes/:id/personal-info
Body: { full_name, email, phone, address, linkedin, github, summary }
```

### Experience

#### Add Experience
```
POST /resumes/:id/experiences
Body: { company, position, start_date, end_date, description, current }
```

#### Delete Experience
```
DELETE /resumes/:id/experiences/:exp_id
```

### Skills

#### Add Skill
```
POST /resumes/:id/skills
Body: { name: "Python", proficiency: "expert" }
```

#### Delete Skill
```
DELETE /resumes/:id/skills/:skill_id
```

### Templates

#### Get All Templates
```
GET /templates
Response: [{ id, name, description }]
```

### AI Features (Rate Limited: 5 requests per minute per IP)

#### Parse Resume
```
POST /ai/parse
Body: { "text": "Raw resume text..." }
Response: { "personal_info": {...}, "experiences": [...], ... }
```

#### Score Resume
```
POST /ai/score
Body: { "resume_data": {...} }
Response: { "score": 85, "feedback": [...] }
```

#### Rephrase Experience
```
POST /ai/rephrase
Body: { "description": "Did some things with code..." }
Response: { "rephrased": "Engineered scalable solutions..." }
```

#### Generate Cover Letter
```
POST /ai/cover-letter
Body: { "resume_data": {...}, "job_description": "..." }
Response: { "cover_letter": "Dear Hiring Manager..." }
```
