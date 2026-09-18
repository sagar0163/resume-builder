<template>
  <div>
    <header class="bg-surface border-b border-white/10 p-4">
      <div class="max-w-6xl mx-auto flex justify-between items-center">
        <h1 class="text-xl font-bold">Resume Builder</h1>
        <button @click="store.createResume('Untitled')" class="bg-primary px-4 py-2 rounded-xl">+ New Resume</button>
      </div>
    </header>

    <main class="max-w-6xl mx-auto p-4">
      <ResumeList v-if="!store.selectedResume" />

      <div v-else class="grid grid-cols-2 gap-6">
        <ResumeForm />
        <ResumePreview />
      </div>

      <button v-if="store.selectedResume" @click="store.clearSelected()" class="mt-4 bg-surface px-4 py-2 rounded-xl">← Back to List</button>
    </main>
  </div>
</template>

<script setup>
import { useResumeStore } from '../stores/resume'
import ResumeList from '../components/ResumeList.vue'
import ResumeForm from '../components/ResumeForm.vue'
import ResumePreview from '../components/ResumePreview.vue'

const store = useResumeStore()
</script>
