import { defineStore } from 'pinia'
import { ref } from 'vue'

const API = 'http://localhost:5000/api'

export const useResumeStore = defineStore('resume', () => {
  const resumes = ref([])
  const selectedResume = ref(null)
  const form = ref({
    full_name: '',
    email: '',
    phone: '',
    address: '',
    linkedin: '',
    github: '',
    summary: '',
    experiences: [],
    skills: [],
    education: []
  })

  async function loadResumes() {
    const res = await fetch(API + '/resumes')
    resumes.value = await res.json()
  }

  async function createResume(name = 'Untitled') {
    const res = await fetch(API + '/resumes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name })
    })
    const r = await res.json()
    await loadResumes()
    await selectResume(r.id)
  }

  async function selectResume(id) {
    selectedResume.value = id
    const res = await fetch(API + '/resumes/' + id)
    const data = await res.json()
    form.value = {
      full_name: data.personal_info?.full_name || '',
      email: data.personal_info?.email || '',
      phone: data.personal_info?.phone || '',
      address: data.personal_info?.address || '',
      linkedin: data.personal_info?.linkedin || '',
      github: data.personal_info?.github || '',
      summary: data.personal_info?.summary || '',
      experiences: data.experiences || [],
      skills: data.skills || [],
      education: data.education || []
    }
  }

  async function savePersonalInfo() {
    if (!selectedResume.value) return
    await fetch(API + '/resumes/' + selectedResume.value + '/personal-info', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })
    alert('Saved!')
  }

  async function addSkill(skillData) {
    form.value.skills.push(skillData)
    await fetch(API + '/resumes/' + selectedResume.value + '/skills', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(skillData)
    })
  }

  function addExperience() {
    form.value.experiences.push({ company: '', position: '', start_date: '', end_date: '', description: '' })
  }

  function removeExperience(i) {
    form.value.experiences.splice(i, 1)
  }

  function addEducation() {
    form.value.education.push({ institution: '', degree: '', field_of_study: '' })
  }

  function removeEducation(i) {
    form.value.education.splice(i, 1)
  }

  function removeSkill(i) {
    form.value.skills.splice(i, 1)
  }

  function clearSelected() {
    selectedResume.value = null
  }

  return {
    resumes,
    selectedResume,
    form,
    loadResumes,
    createResume,
    selectResume,
    savePersonalInfo,
    addSkill,
    addExperience,
    removeExperience,
    addEducation,
    removeEducation,
    removeSkill,
    clearSelected
  }
})
