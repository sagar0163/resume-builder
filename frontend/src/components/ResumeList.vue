<template>
  <div class="grid grid-cols-3 gap-4">
    <div 
      v-for="r in resumes" 
      :key="r.id" 
      @click="selectResume(r.id)" 
      class="bg-surface rounded-xl p-4 cursor-pointer hover:border-primary border border-transparent transition"
    >
      <div class="font-bold">{{ r.name }}</div>
      <div class="text-sm text-gray-400">Template: {{ r.template }}</div>
      <div class="text-xs text-gray-500 mt-2">Updated: {{ formatDate(r.updated_at) }}</div>
    </div>
    <div v-if="resumes.length === 0" class="col-span-3 text-center py-12 text-gray-500">
      No resumes yet. Create one to get started!
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useResumeStore } from '../stores/resume'

const store = useResumeStore()

onMounted(() => {
  store.loadResumes()
})

const resumes = computed(() => store.resumes)

const selectResume = (id) => {
  store.selectResume(id)
}

const formatDate = (d) => new Date(d).toLocaleDateString()
</script>
