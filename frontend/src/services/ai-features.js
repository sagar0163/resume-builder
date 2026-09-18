// AI Features JavaScript Module
// Add to frontend/index.html for Magic Import and Resume Scoring

const aiFeatures = {
    API_URL: 'http://localhost:5000/api',
    
    // Parse raw text into resume data
    async parseResume(text) {
        try {
            const res = await fetch(`${this.API_URL}/ai/parse`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            if (!res.ok) throw new Error('Parse failed');
            return await res.json();
        } catch (e) {
            console.error('Parse error:', e);
            throw e;
        }
    },
    
    // Score resume for ATS
    async scoreResume(resumeData) {
        try {
            const res = await fetch(`${this.API_URL}/ai/score`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(resumeData)
            });
            if (!res.ok) throw new Error('Score failed');
            return await res.json();
        } catch (e) {
            console.error('Score error:', e);
            throw e;
        }
    },
    
    // Rephrase experience
    async rephrase(text) {
        try {
            const res = await fetch(`${this.API_URL}/ai/rephrase`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ description: text })
            });
            if (!res.ok) throw new Error('Rephrase failed');
            const data = await res.json();
            return data.rephrased;
        } catch (e) {
            console.error('Rephrase error:', e);
            throw e;
        }
    },
    
    // Generate cover letter
    async generateCoverLetter(resumeData, jobDescription) {
        try {
            const res = await fetch(`${this.API_URL}/ai/cover-letter`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ resume_data: resumeData, job_description: jobDescription })
            });
            if (!res.ok) throw new Error('Cover letter failed');
            const data = await res.json();
            return data.cover_letter;
        } catch (e) {
            console.error('Cover letter error:', e);
            throw e;
        }
    }
};

// Export for use
window.aiFeatures = aiFeatures;
