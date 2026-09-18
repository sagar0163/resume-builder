<template>
  <div class="space-y-4">
    <!-- Personal Info -->
    <div class="bg-surface rounded-xl p-4">
      <h3 class="font-bold mb-4">Personal Information</h3>
      <div class="grid grid-cols-2 gap-3">
        <input v-model="form.full_name" placeholder="Full Name" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
        <input v-model="form.email" placeholder="Email" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
        <input v-model="form.phone" placeholder="Phone" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
        <input v-model="form.address" placeholder="Address" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
        <input v-model="form.linkedin" placeholder="LinkedIn" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
        <input v-model="form.github" placeholder="GitHub" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
      </div>
      <textarea v-model="form.summary" placeholder="Professional Summary" class="w-full mt-3 bg-dark border border-white/10 rounded-lg px-3 py-2" rows="3"></textarea>
      <button @click="store.savePersonalInfo" class="mt-3 bg-primary px-4 py-2 rounded-lg">Save</button>
    </div>

    <!-- Experience -->
    <div class="bg-surface rounded-xl p-4">
      <h3 class="font-bold mb-4">Experience</h3>
      <div v-for="(exp, i) in form.experiences" :key="i" class="mb-4 p-3 bg-dark rounded-lg">
        <input v-model="exp.position" placeholder="Position" class="w-full mb-2 bg-surface border border-white/10 rounded px-3 py-2">
        <input v-model="exp.company" placeholder="Company" class="w-full mb-2 bg-surface border border-white/10 rounded px-3 py-2">
        <div class="grid grid-cols-2 gap-2 mb-2">
          <input v-model="exp.start_date" placeholder="Start Date" class="bg-surface border border-white/10 rounded px-3 py-2">
          <input v-model="exp.end_date" placeholder="End Date" class="bg-surface border border-white/10 rounded px-3 py-2">
        </div>
        <textarea v-model="exp.description" placeholder="Description" class="w-full bg-surface border border-white/10 rounded px-3 py-2" rows="2"></textarea>
        <button @click="store.removeExperience(i)" class="mt-2 text-red-400 text-sm">Remove</button>
      </div>
      <button @click="store.addExperience" class="text-primary">+ Add Experience</button>
    </div>

    <!-- Skills -->
    <div class="bg-surface rounded-xl p-4">
      <h3 class="font-bold mb-4">Skills</h3>
      <div class="flex flex-wrap gap-2 mb-3">
        <span v-for="(skill, i) in form.skills" :key="i" class="bg-primary/20 text-primary px-3 py-1 rounded-full flex items-center gap-2">
          {{ skill.name }}
          <button @click="store.removeSkill(i)" class="text-primary hover:text-white">×</button>
        </span>
      </div>
      <div class="flex gap-2">
        <input v-model="newSkill" @keyup.enter="addSkill" placeholder="Add skill" class="flex-1 bg-dark border border-white/10 rounded-lg px-3 py-2">
        <select v-model="skillProficiency" class="bg-dark border border-white/10 rounded-lg px-3 py-2">
          <option value="beginner">Beginner</option>
          <option value="intermediate">Intermediate</option>
          <option value="advanced">Advanced</option>
          <option value="expert">Expert</option>
        </select>
        <button @click="addSkill" class="bg-primary px-4 py-2 rounded-lg">Add</button>
      </div>
    </div>

    <!-- Education -->
    <div class="bg-surface rounded-xl p-4">
      <h3 class="font-bold mb-4">Education</h3>
      <div v-for="(edu, i) in form.education" :key="i" class="mb-4 p-3 bg-dark rounded-lg">
        <input v-model="edu.institution" placeholder="Institution" class="w-full mb-2 bg-surface border border-white/10 rounded px-3 py-2">
        <input v-model="edu.degree" placeholder="Degree" class="w-full mb-2 bg-surface border border-white/10 rounded px-3 py-2">
        <button @click="store.removeEducation(i)" class="mt-2 text-red-400 text-sm">Remove</button>
      </div>
      <button @click="store.addEducation" class="text-primary">+ Add Education</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useResumeStore } from '../stores/resume'

const store = useResumeStore()
const form = computed(() => store.form)

const newSkill = ref('')
const skillProficiency = ref('intermediate')

const addSkill = async () => {
  if (!newSkill.value) return
  await store.addSkill({ name: newSkill.value, proficiency: skillProficiency.value })
  newSkill.value = ''
}
</script>
