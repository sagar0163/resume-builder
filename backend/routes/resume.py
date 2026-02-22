from flask import Blueprint, request, jsonify
from app import db
from models import Resume, PersonalInfo, Experience, Education, Skill, Certification, Language, Project

resume_bp = Blueprint('resume', __name__)


@resume_bp.route('/resumes', methods=['GET'])
def get_resumes():
    """Get all resumes"""
    resumes = Resume.query.order_by(Resume.updated_at.desc()).all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'template': r.template,
        'created_at': r.created_at.isoformat(),
        'updated_at': r.updated_at.isoformat()
    } for r in resumes])


@resume_bp.route('/resumes', methods=['POST'])
def create_resume():
    """Create a new resume"""
    data = request.json
    resume = Resume(name=data.get('name', 'Untitled Resume'))
    db.session.add(resume)
    db.session.commit()
    
    # Create empty personal info
    personal_info = PersonalInfo(resume_id=resume.id)
    db.session.add(personal_info)
    db.session.commit()
    
    return jsonify({
        'id': resume.id,
        'name': resume.name,
        'template': resume.template
    }), 201


@resume_bp.route('/resumes/<int:resume_id>', methods=['GET'])
def get_resume(resume_id):
    """Get a single resume with all details"""
    resume = Resume.query.get_or_404(resume_id)
    
    return jsonify({
        'id': resume.id,
        'name': resume.name,
        'template': resume.template,
        'created_at': resume.created_at.isoformat(),
        'updated_at': resume.updated_at.isoformat(),
        'personal_info': {
            'id': resume.personal_info.id if resume.personal_info else None,
            'full_name': resume.personal_info.full_name or '',
            'email': resume.personal_info.email or '',
            'phone': resume.personal_info.phone or '',
            'address': resume.personal_info.address or '',
            'linkedin': resume.personal_info.linkedin or '',
            'github': resume.personal_info.github or '',
            'website': resume.personal_info.website or '',
            'summary': resume.personal_info.summary or ''
        } if resume.personal_info else None,
        'experiences': [{
            'id': e.id,
            'company': e.company,
            'position': e.position,
            'start_date': e.start_date,
            'end_date': e.end_date,
            'current': e.current,
            'description': e.description
        } for e in resume.experiences],
        'education': [{
            'id': e.id,
            'institution': e.institution,
            'degree': e.degree,
            'field_of_study': e.field_of_study,
            'start_date': e.start_date,
            'end_date': e.end_date,
            'gpa': e.gpa
        } for e in resume.education],
        'skills': [{
            'id': s.id,
            'name': s.name,
            'proficiency': s.proficiency
        } for s in resume.skills],
        'certifications': [{
            'id': c.id,
            'name': c.name,
            'issuer': c.issuer,
            'date': c.date
        } for c in resume.certifications],
        'languages': [{
            'id': l.id,
            'name': l.name,
            'proficiency': l.proficiency
        } for l in resume.languages],
        'projects': [{
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'technologies': p.technologies,
            'link': p.link
        } for p in resume.projects]
    })


@resume_bp.route('/resumes/<int:resume_id>', methods=['PUT'])
def update_resume(resume_id):
    """Update a resume"""
    resume = Resume.query.get_or_404(resume_id)
    data = request.json
    
    if 'name' in data:
        resume.name = data['name']
    if 'template' in data:
        resume.template = data['template']
    
    db.session.commit()
    return jsonify({'message': 'Resume updated'})


@resume_bp.route('/resumes/<int:resume_id>', methods=['DELETE'])
def delete_resume(resume_id):
    """Delete a resume"""
    resume = Resume.query.get_or_404(resume_id)
    db.session.delete(resume)
    db.session.commit()
    return jsonify({'message': 'Resume deleted'})


# Personal Info
@resume_bp.route('/resumes/<int:resume_id>/personal-info', methods=['PUT'])
def update_personal_info(resume_id):
    """Update personal information"""
    resume = Resume.query.get_or_404(resume_id)
    data = request.json
    
    if resume.personal_info:
        for key, value in data.items():
            setattr(resume.personal_info, key, value)
    else:
        personal_info = PersonalInfo(resume_id=resume_id, **data)
        db.session.add(personal_info)
    
    db.session.commit()
    return jsonify({'message': 'Personal info updated'})


# Experience
@resume_bp.route('/resumes/<int:resume_id>/experiences', methods=['POST'])
def add_experience(resume_id):
    """Add experience"""
    data = request.json
    experience = Experience(resume_id=resume_id, **data)
    db.session.add(experience)
    db.session.commit()
    return jsonify({'id': experience.id}), 201


@resume_bp.route('/resumes/<int:resume_id>/experiences/<int:exp_id>', methods=['PUT'])
def update_experience(resume_id, exp_id):
    """Update experience"""
    experience = Experience.query.get_or_404(exp_id)
    data = request.json
    for key, value in data.items():
        setattr(experience, key, value)
    db.session.commit()
    return jsonify({'message': 'Experience updated'})


@resume_bp.route('/resumes/<int:resume_id>/experiences/<int:exp_id>', methods=['DELETE'])
def delete_experience(resume_id, exp_id):
    """Delete experience"""
    experience = Experience.query.get_or_404(exp_id)
    db.session.delete(experience)
    db.session.commit()
    return jsonify({'message': 'Experience deleted'})


# Education
@resume_bp.route('/resumes/<int:resume_id>/education', methods=['POST'])
def add_education(resume_id):
    """Add education"""
    data = request.json
    education = Education(resume_id=resume_id, **data)
    db.session.add(education)
    db.session.commit()
    return jsonify({'id': education.id}), 201


@resume_bp.route('/resumes/<int:resume_id>/education/<int:edu_id>', methods=['DELETE'])
def delete_education(resume_id, edu_id):
    """Delete education"""
    education = Education.query.get_or_404(edu_id)
    db.session.delete(education)
    db.session.commit()
    return jsonify({'message': 'Education deleted'})


# Skills
@resume_bp.route('/resumes/<int:resume_id>/skills', methods=['POST'])
def add_skill(resume_id):
    """Add skill"""
    data = request.json
    skill = Skill(resume_id=resume_id, **data)
    db.session.add(skill)
    db.session.commit()
    return jsonify({'id': skill.id}), 201


@resume_bp.route('/resumes/<int:resume_id>/skills/<int:skill_id>', methods=['DELETE'])
def delete_skill(resume_id, skill_id):
    """Delete skill"""
    skill = Skill.query.get_or_404(skill_id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': 'Skill deleted'})


# Certifications
@resume_bp.route('/resumes/<int:resume_id>/certifications', methods=['POST'])
def add_certification(resume_id):
    """Add certification"""
    data = request.json
    cert = Certification(resume_id=resume_id, **data)
    db.session.add(cert)
    db.session.commit()
    return jsonify({'id': cert.id}), 201


@resume_bp.route('/resumes/<int:resume_id>/certifications/<int:cert_id>', methods=['DELETE'])
def delete_certification(resume_id, cert_id):
    """Delete certification"""
    cert = Certification.query.get_or_404(cert_id)
    db.session.delete(cert)
    db.session.commit()
    return jsonify({'message': 'Certification deleted'})


# Languages
@resume_bp.route('/resumes/<int:resume_id>/languages', methods=['POST'])
def add_language(resume_id):
    """Add language"""
    data = request.json
    lang = Language(resume_id=resume_id, **data)
    db.session.add(lang)
    db.session.commit()
    return jsonify({'id': lang.id}), 201


@resume_bp.route('/resumes/<int:resume_id>/languages/<int:lang_id>', methods=['DELETE'])
def delete_language(resume_id, lang_id):
    """Delete language"""
    lang = Language.query.get_or_404(lang_id)
    db.session.delete(lang)
    db.session.commit()
    return jsonify({'message': 'Language deleted'})


# Projects
@resume_bp.route('/resumes/<int:resume_id>/projects', methods=['POST'])
def add_project(resume_id):
    """Add project"""
    data = request.json
    project = Project(resume_id=resume_id, **data)
    db.session.add(project)
    db.session.commit()
    return jsonify({'id': project.id}), 201


@resume_bp.route('/resumes/<int:resume_id>/projects/<int:proj_id>', methods=['DELETE'])
def delete_project(resume_id, proj_id):
    """Delete project"""
    project = Project.query.get_or_404(proj_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted'})
