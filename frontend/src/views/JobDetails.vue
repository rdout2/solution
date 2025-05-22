<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import type { Application } from '../types/application';

const route = useRoute();
const router = useRouter();

const job = ref<Application | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await fetch(`http://localhost:5000/api/applications/${route.params.id}`);
    if (!response.ok) throw new Error('Failed to fetch job details');
    job.value = await response.json();
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load job details';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <div class="flex items-center mb-8">
      <button
        @click="router.back()"
        class="mr-4 text-gray-600 hover:text-gray-900"
      >
        ← Back
      </button>
      <h1 class="text-2xl font-bold text-gray-900">Job Details</h1>
    </div>

    <div v-if="loading" class="animate-pulse">
      <div class="h-8 bg-gray-200 rounded w-1/2 mb-4"></div>
      <div class="h-6 bg-gray-200 rounded w-1/3 mb-2"></div>
      <div class="h-6 bg-gray-200 rounded w-1/4"></div>
    </div>

    <div v-else-if="error" class="bg-red-50 text-red-700 p-4 rounded-lg">
      {{ error }}
    </div>

    <div v-else-if="job" class="bg-white shadow rounded-lg p-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label class="block text-sm font-medium text-gray-700">Job Title</label>
          <div class="mt-1 text-lg">{{ job.jobTitle }}</div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Company</label>
          <div class="mt-1 text-lg">{{ job.company }}</div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Status</label>
          <div class="mt-1">
            <span 
              class="px-2 py-1 text-sm font-medium rounded-full"
              :class="{
                'bg-wishlist-light text-wishlist-dark': job.status === 'Wishlist',
                'bg-applied-light text-applied-dark': job.status === 'Applied',
                'bg-interview-light text-interview-dark': job.status === 'Interview',
                'bg-offer-light text-offer-dark': job.status === 'Offer',
                'bg-rejected-light text-rejected-dark': job.status === 'Rejected',
              }"
            >
              {{ job.status }}
            </span>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Date Applied</label>
          <div class="mt-1 text-lg">{{ job.date }}</div>
        </div>

        <div class="md:col-span-2">
          <label class="block text-sm font-medium text-gray-700">Notes</label>
          <div class="mt-1 text-lg whitespace-pre-wrap">
            <!-- {{ job.notes || 'No notes available' }} -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>