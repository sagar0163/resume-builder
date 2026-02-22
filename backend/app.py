from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'resume-builder-secret-2024')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    
    # Register blueprints
    from routes.resume import resume_bp
    from routes.templates import templates_bp
    from routes.ai import ai_bp
    
    app.register_blueprint(resume_bp, url_prefix='/api')
    app.register_blueprint(templates_bp, url_prefix='/api')
    app.register_blueprint(ai_bp, url_prefix='/api')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
