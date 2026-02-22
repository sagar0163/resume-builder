"""
AI Service for Resume Builder
Magic Importer and Resume Scorer using Gemini API
"""
import os
import json
from typing import Dict, Any

try:
    import google.generativeai as genai
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "google-generativeai"], check=True)
    import google.generativeai as genai


class AIResumeService:
    """AI-powered resume enhancement features"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set")
        
        genai.configure(api_key=self.api_key)
        self.model = "gemini-1.5-flash"
    
    def parse_resume_text(self, raw_text: str) -> Dict[str, Any]:
        """Parse raw text into resume data"""
        
        prompt = f"""Parse this resume/cv text and extract the following information. 
Return ONLY valid JSON (no markdown, no explanation):

JSON Schema:
{{
    "personal_info": {{
        "full_name": "string or null",
        "email": "string or null", 
        "phone": "string or null",
        "linkedin": "string or null",
        "github": "string or null"
    }},
    "summary": "string or null",
    "experience": [
        {{
            "company": "string",
            "position": "string", 
            "start_date": "string or null",
            "end_date": "string or null",
            "description": "string"
        }}
    ],
    "education": [
        {{
            "institution": "string",
            "degree": "string",
            "field_of_study": "string or null"
        }}
    ],
    "skills": ["skill1", "skill2"]
}}

Text to parse:
{raw_text}

Return ONLY the JSON object:"""
        
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        
        # Clean response and parse JSON
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        
        return json.loads(text.strip())
    
    def score_resume(self, resume_data: Dict[str, Any]) -> Dict[str, Any]:
        """Score resume for ATS optimization"""
        
        prompt = f"""Analyze this resume and provide an ATS score (0-100) with feedback.
Return ONLY valid JSON:

JSON Schema:
{{
    "score": 0-100,
    "strengths": ["strength1", "strength2"],
    "weaknesses": ["weakness1", "weakness2"],
    "suggestions": ["suggestion1", "suggestion2"],
    "keywords_found": ["keyword1"],
    "keywords_missing": ["keyword2"]
}}

Resume Data:
{json.dumps(resume_data, indent=2)}

Return ONLY the JSON object:"""
        
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        
        # Parse JSON response
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        
        return json.loads(text.strip())
    
    def rephrase_experience(self, description: str) -> str:
        """Rephrase weak bullet points into impact statements"""
        
        prompt = f"""Rephrase this resume bullet point to be more impactful and quantifiable.
Use action verbs and add metrics where possible.

Original: {description}

Rephrased (1-2 sentences max):"""
        
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        
        return response.text.strip()
    
    def generate_cover_letter(self, resume_data: Dict[str, Any], job_description: str) -> str:
        """Generate matching cover letter"""
        
        prompt = f"""Generate a professional cover letter based on this resume and job description.

Resume:
{json.dumps(resume_data, indent=2)}

Job Description:
{job_description}

Write a personalized cover letter that highlights relevant experience and skills.
Keep it to 3-4 paragraphs. Professional tone."""
        
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        
        return response.text.strip()


if __name__ == "__main__":
    # Test the service
    print("Testing AI Resume Service...")
    # Will work once GEMINI_API_KEY is set
