<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white border-b border-gray-200 shadow-sm py-4">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center">
          <h1 class="text-xl font-bold text-primary-600">JobTracker</h1>
          <nav class="flex gap-4">
            <router-link 
              to="/" 
              class="text-gray-600 hover:text-primary-600 transition-colors"
              active-class="text-primary-600 font-medium"
            >
              Applications
            </router-link>
            <router-link 
              to="/metrics" 
              class="text-gray-600 hover:text-primary-600 transition-colors"
              active-class="text-primary-600 font-medium"
            >
              Metrics
            </router-link>
            <router-link 
              to="/add-job" 
              class="text-gray-600 hover:text-primary-600 transition-colors"
              active-class="text-primary-600 font-medium"
            >
              Add Job
            </router-link>
            <router-link 
              to="/profile" 
              class="text-gray-600 hover:text-primary-600 transition-colors"
              active-class="text-primary-600 font-medium"
            >
              Profile
            </router-link>
          </nav>
        </div>
      </div>
    </header>

    <main class="container mx-auto">
      <router-view></router-view>
    </main>
  </div>
</template>