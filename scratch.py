import re

with open('backend/routes/resume.py', 'r') as f:
    content = f.read()

# Add jwt_required import
content = content.replace(
    "from flask import Blueprint, request, jsonify",
    "from flask import Blueprint, request, jsonify\nfrom flask_jwt_extended import jwt_required, get_jwt_identity"
)

# Add @jwt_required() to all routes
content = re.sub(r'(@resume_bp\.route\([^\)]+\)\n)(def )', r'\1@jwt_required()\n\2', content)

# Modify get_resumes
content = content.replace(
    "resumes = Resume.query.order_by(Resume.updated_at.desc()).all()",
    "resumes = Resume.query.filter_by(user_id=get_jwt_identity()).order_by(Resume.updated_at.desc()).all()"
)

# Modify create_resume
content = content.replace(
    "resume = Resume(name=data.get('name', 'Untitled Resume'))",
    "resume = Resume(name=data.get('name', 'Untitled Resume'), user_id=get_jwt_identity())"
)

# Modify get_resume
content = content.replace(
    "    ).get_or_404(resume_id)",
    "    ).filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()"
)

# Modify update_resume, delete_resume, update_personal_info
content = re.sub(
    r"resume = Resume\.query\.get_or_404\(resume_id\)",
    "resume = Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()",
    content
)

# Modify add_x
for resource in ['Experience', 'Education', 'Skill', 'Certification', 'Language', 'Project']:
    content = re.sub(
        rf"data = request\.json\n    {resource.lower()[:4]} = {resource}\(resume_id=resume_id, \*\*data\)",
        f"Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    {resource.lower()[:4]} = {resource}(resume_id=resume_id, **data)",
        content
    )
    
# Specifically handle add_experience and others using specific variable names
content = content.replace("Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    expe = Experience(resume_id=resume_id, **data)", 
                          "Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    experience = Experience(resume_id=resume_id, **data)")
content = content.replace("Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    educ = Education(resume_id=resume_id, **data)",
                          "Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    education = Education(resume_id=resume_id, **data)")
content = content.replace("Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    skil = Skill(resume_id=resume_id, **data)",
                          "Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    skill = Skill(resume_id=resume_id, **data)")
content = content.replace("Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    cert = Certification(resume_id=resume_id, **data)",
                          "Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    cert = Certification(resume_id=resume_id, **data)")
content = content.replace("Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    lang = Language(resume_id=resume_id, **data)",
                          "Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    lang = Language(resume_id=resume_id, **data)")
content = content.replace("Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    proj = Project(resume_id=resume_id, **data)",
                          "Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    data = request.json\n    project = Project(resume_id=resume_id, **data)")

# Modify update_x, delete_x for sub-resources
# For example: experience = Experience.query.get_or_404(exp_id)
# Should become: 
# Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()
# experience = Experience.query.filter_by(id=exp_id, resume_id=resume_id).first_or_404()
for resource, var_name, id_param in [
    ('Experience', 'experience', 'exp_id'),
    ('Education', 'education', 'edu_id'),
    ('Skill', 'skill', 'skill_id'),
    ('Certification', 'cert', 'cert_id'),
    ('Language', 'lang', 'lang_id'),
    ('Project', 'project', 'proj_id')
]:
    content = re.sub(
        rf"{var_name} = {resource}\.query\.get_or_404\({id_param}\)",
        f"Resume.query.filter_by(id=resume_id, user_id=get_jwt_identity()).first_or_404()\n    {var_name} = {resource}.query.filter_by(id={id_param}, resume_id=resume_id).first_or_404()",
        content
    )


with open('backend/routes/resume.py', 'w') as f:
    f.write(content)
print("Done!")
