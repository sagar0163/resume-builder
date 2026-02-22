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
