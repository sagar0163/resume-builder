<template>
  <div class="bg-white text-black rounded-xl p-8 min-h-[800px]">
    <div class="text-center border-b pb-4 mb-4">
      <h2 class="text-2xl font-bold">{{ form.full_name || 'Your Name' }}</h2>
      <p class="text-gray-600">{{ form.email }} | {{ form.phone }}</p>
      <p class="text-gray-600">{{ form.address }}</p>
    </div>
    <div v-if="form.summary" class="mb-4">
      <h3 class="font-bold border-b mb-2">Summary</h3>
      <p class="text-sm">{{ form.summary }}</p>
    </div>
    <div v-if="form.experiences.length" class="mb-4">
      <h3 class="font-bold border-b mb-2">Experience</h3>
      <div v-for="(exp, i) in form.experiences" :key="i" class="mb-2">
        <div class="font-semibold">{{ exp.position }} at {{ exp.company }}</div>
        <div class="text-sm text-gray-600">{{ exp.start_date }} - {{ exp.end_date }}</div>
        <p class="text-sm">{{ exp.description }}</p>
      </div>
    </div>
    <div v-if="form.skills.length" class="mb-4">
      <h3 class="font-bold border-b mb-2">Skills</h3>
      <p>{{ form.skills.map(s => s.name).join(', ') }}</p>
    </div>
    <div v-if="form.education.length">
      <h3 class="font-bold border-b mb-2">Education</h3>
      <div v-for="(edu, i) in form.education" :key="i" class="mb-2">
        <div class="font-semibold">{{ edu.degree }}</div>
        <div class="text-sm text-gray-600">{{ edu.institution }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useResumeStore } from '../stores/resume'

const store = useResumeStore()
const form = computed(() => store.form)
</script>
