<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import type { ApplicationStatus } from '../types/application';

const router = useRouter();

const formData = ref({
  jobTitle: '',
  company: '',
  status: 'Wishlist' as ApplicationStatus,
  jobBoard: '',
  location: '',
  notes: ''
});

const loading = ref(false);
const error = ref<string | null>(null);

const statuses: ApplicationStatus[] = ['Wishlist', 'Applied', 'Interview', 'Offer', 'Rejected'];

async function handleSubmit() {
  loading.value = true;
  error.value = null;

  try {
    const response = await fetch('http://localhost:5000/api/applications', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData.value),
    });

    if (!response.ok) throw new Error('Failed to create application');
    
    router.push('/');
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to create application';
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div class="max-w-2xl mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold text-gray-900 mb-8">Add New Job Application</h1>

    <form @submit.prevent="handleSubmit" class="bg-white shadow rounded-lg p-6">
      <div class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-700">Job Title</label>
          <input
            v-model="formData.jobTitle"
            type="text"
            required
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Company</label>
          <input
            v-model="formData.company"
            type="text"
            required
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Status</label>
          <select
            v-model="formData.status"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500"
          >
            <option v-for="status in statuses" :key="status" :value="status">
              {{ status }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Job Board</label>
          <input
            v-model="formData.jobBoard"
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Location</label>
          <input
            v-model="formData.location"
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Notes</label>
          <textarea
            v-model="formData.notes"
            rows="4"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500"
          ></textarea>
        </div>

        <div v-if="error" class="bg-red-50 text-red-700 p-4 rounded-lg">
          {{ error }}
        </div>

        <div class="flex justify-end">
          <button
            type="submit"
            :disabled="loading"
            class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
          >
            {{ loading ? 'Creating...' : 'Create Application' }}
          </button>
        </div>
      </div>
    </form>
  </div>
</template>