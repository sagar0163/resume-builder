from app import db
from datetime import datetime

class Resume(db.Model):
    __tablename__ = 'resumes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    template = db.Column(db.String(50), default='modern')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    personal_info = db.relationship('PersonalInfo', backref='resume', uselist=False, cascade='all, delete-orphan')
    experiences = db.relationship('Experience', backref='resume', cascade='all, delete-orphan')
    education = db.relationship('Education', backref='resume', cascade='all, delete-orphan')
    skills = db.relationship('Skill', backref='resume', cascade='all, delete-orphan')
    certifications = db.relationship('Certification', backref='resume', cascade='all, delete-orphan')
    languages = db.relationship('Language', backref='resume', cascade='all, delete-orphan')
    projects = db.relationship('Project', backref='resume', cascade='all, delete-orphan')


class PersonalInfo(db.Model):
    __tablename__ = 'personal_info'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    linkedin = db.Column(db.String(100))
    github = db.Column(db.String(100))
    website = db.Column(db.String(100))
    summary = db.Column(db.Text)


class Experience(db.Model):
    __tablename__ = 'experiences'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    company = db.Column(db.String(100))
    position = db.Column(db.String(100))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    current = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)


class Education(db.Model):
    __tablename__ = 'education'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    institution = db.Column(db.String(100))
    degree = db.Column(db.String(100))
    field_of_study = db.Column(db.String(100))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    gpa = db.Column(db.String(10))


class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    name = db.Column(db.String(50))
    proficiency = db.Column(db.String(20))  # beginner, intermediate, advanced, expert


class Certification(db.Model):
    __tablename__ = 'certifications'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    name = db.Column(db.String(100))
    issuer = db.Column(db.String(100))
    date = db.Column(db.String(20))


class Language(db.Model):
    __tablename__ = 'languages'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    name = db.Column(db.String(50))
    proficiency = db.Column(db.String(50))


class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    technologies = db.Column(db.String(200))
    link = db.Column(db.String(200))
