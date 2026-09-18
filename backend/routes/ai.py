from flask import Blueprint, request, jsonify, current_app
from services.ai_service import AIResumeService
from extensions import limiter

ai_bp = Blueprint('ai', __name__)


def get_ai_service():
    """Get or create AIResumeService instance in application context."""
    if 'ai_service' not in current_app.extensions:
        # Initialize once per application context
        current_app.extensions['ai_service'] = AIResumeService()
    return current_app.extensions['ai_service']


@ai_bp.route('/ai/parse', methods=['POST'])
@limiter.limit("5 per minute")
def parse_resume():
    """Parse raw text into resume data"""
    try:
        data = request.json
        raw_text = data.get('text', '')
        
        if not raw_text:
            return jsonify({'error': 'No text provided'}), 400
        
        ai_service = get_ai_service()
        result = ai_service.parse_resume_text(raw_text)
        
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'AI parsing failed: {str(e)}'}), 500


@ai_bp.route('/ai/score', methods=['POST'])
@limiter.limit("5 per minute")
def score_resume():
    """Score resume for ATS optimization"""
    try:
        resume_data = request.json
        
        if not resume_data:
            return jsonify({'error': 'No resume data provided'}), 400
        
        ai_service = get_ai_service()
        result = ai_service.score_resume(resume_data)
        
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'AI scoring failed: {str(e)}'}), 500


@ai_bp.route('/ai/rephrase', methods=['POST'])
@limiter.limit("5 per minute")
def rephrase_experience():
    """Rephrase experience bullet points"""
    try:
        data = request.json
        description = data.get('description', '')
        
        if not description:
            return jsonify({'error': 'No description provided'}), 400
        
        ai_service = get_ai_service()
        result = ai_service.rephrase_experience(description)
        
        return jsonify({'rephrased': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'AI rephrasing failed: {str(e)}'}), 500


@ai_bp.route('/ai/cover-letter', methods=['POST'])
@limiter.limit("5 per minute")
def generate_cover_letter():
    """Generate matching cover letter"""
    try:
        data = request.json
        resume_data = data.get('resume_data', {})
        job_description = data.get('job_description', '')
        
        if not job_description:
            return jsonify({'error': 'No job description provided'}), 400
        
        ai_service = get_ai_service()
        result = ai_service.generate_cover_letter(resume_data, job_description)
        
        return jsonify({'cover_letter': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'AI cover letter generation failed: {str(e)}'}), 500
