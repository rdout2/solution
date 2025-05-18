<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface User {
  id: number;
  username: string;
  email: string;
  created_at: string;
}

const user = ref<User | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:5000/api/users/1');
    if (!response.ok) throw new Error('Failed to fetch user data');
    user.value = await response.json();
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load profile';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold text-gray-900 mb-8">Profile</h1>

    <div v-if="loading" class="animate-pulse">
      <div class="h-8 bg-gray-200 rounded w-1/4 mb-4"></div>
      <div class="h-6 bg-gray-200 rounded w-1/3 mb-2"></div>
      <div class="h-6 bg-gray-200 rounded w-1/2"></div>
    </div>

    <div v-else-if="error" class="bg-red-50 text-red-700 p-4 rounded-lg">
      {{ error }}
    </div>

    <div v-else-if="user" class="bg-white shadow rounded-lg p-6">
      <div class="grid grid-cols-1 gap-6">
        <div>
          <label class="block text-sm font-medium text-gray-700">Username</label>
          <div class="mt-1 text-lg">{{ user.username }}</div>
        </div>
        
        <div>
          <label class="block text-sm font-medium text-gray-700">Email</label>
          <div class="mt-1 text-lg">{{ user.email }}</div>
        </div>
        
        <div>
          <label class="block text-sm font-medium text-gray-700">Member Since</label>
          <div class="mt-1 text-lg">
            {{ new Date(user.created_at).toLocaleDateString() }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>