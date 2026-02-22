from flask import Blueprint, jsonify

templates_bp = Blueprint('templates', __name__)

TEMPLATES = [
    {
        'id': 'modern',
        'name': 'Modern',
        'description': 'Clean and minimal design with a professional look',
        'thumbnail': 'modern.png'
    },
    {
        'id': 'classic',
        'name': 'Classic',
        'description': 'Traditional resume layout, perfect for corporate jobs',
        'thumbnail': 'classic.png'
    },
    {
        'id': 'creative',
        'name': 'Creative',
        'description': 'Colorful and unique design to stand out',
        'thumbnail': 'creative.png'
    }
]


@templates_bp.route('/templates', methods=['GET'])
def get_templates():
    """Get all available templates"""
    return jsonify(TEMPLATES)


@templates_bp.route('/templates/<template_id>', methods=['GET'])
def get_template(template_id):
    """Get a specific template"""
    template = next((t for t in TEMPLATES if t['id'] == template_id), None)
    if template is None:
        return jsonify({'error': 'Template not found'}), 404
    return jsonify(template)
