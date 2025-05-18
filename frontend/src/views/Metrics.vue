<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import type { Application } from '../types/application';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const applications = ref<Application[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

const chartData = computed(() => {
  const statusCounts = {
    Wishlist: 0,
    Applied: 0,
    Interview: 0,
    Offer: 0,
    Rejected: 0
  };

  applications.value.forEach(app => {
    statusCounts[app.status]++;
  });

  return {
    labels: Object.keys(statusCounts),
    datasets: [{
      label: 'Applications by Status',
      data: Object.values(statusCounts),
      backgroundColor: [
        '#F59E0B',  // Wishlist
        '#3B82F6',  // Applied
        '#10B981',  // Interview
        '#6366F1',  // Offer
        '#EF4444'   // Rejected
      ]
    }]
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    }
  }
};

const metrics = computed(() => ({
  total: applications.value.length,
  interviews: applications.value.filter(app => app.status === 'Interview').length,
  offers: applications.value.filter(app => app.status === 'Offer').length
}));

const recentApplications = computed(() => {
  return [...applications.value]
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
    .slice(0, 5);
});

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:5000/api/applications');
    if (!response.ok) throw new Error('Failed to fetch applications');
    applications.value = await response.json();
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load metrics';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="max-w-6xl mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold text-gray-900 mb-8">Application Metrics</h1>

    <div v-if="loading" class="animate-pulse space-y-8">
      <div class="h-64 bg-gray-200 rounded"></div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div v-for="i in 3" :key="i" class="h-24 bg-gray-200 rounded"></div>
      </div>
    </div>

    <div v-else-if="error" class="bg-red-50 text-red-700 p-4 rounded-lg">
      {{ error }}
    </div>

    <div v-else class="space-y-8">
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-lg font-medium text-gray-900">Total Applications</h3>
          <p class="mt-2 text-3xl font-bold text-primary-600">{{ metrics.total }}</p>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-lg font-medium text-gray-900">Active Interviews</h3>
          <p class="mt-2 text-3xl font-bold text-interview">{{ metrics.interviews }}</p>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-lg font-medium text-gray-900">Offers Received</h3>
          <p class="mt-2 text-3xl font-bold text-offer">{{ metrics.offers }}</p>
        </div>
      </div>

      <!-- Chart -->
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-lg font-medium text-gray-900 mb-4">Applications by Status</h2>
        <div class="h-64">
          <Bar :data="chartData" :options="chartOptions" />
        </div>
      </div>

      <!-- Recent Applications Table -->
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-lg font-medium text-gray-900 mb-4">Recent Applications</h2>
        <div class="overflow-x-auto">
          <table class="min-w-full">
            <thead>
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Job Title</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Company</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="app in recentApplications" :key="app.id">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ app.jobTitle }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ app.company }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ app.date }}</td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="px-2 py-1 text-xs font-medium rounded-full"
                    :class="{
                      'bg-wishlist-light text-wishlist-dark': app.status === 'Wishlist',
                      'bg-applied-light text-applied-dark': app.status === 'Applied',
                      'bg-interview-light text-interview-dark': app.status === 'Interview',
                      'bg-offer-light text-offer-dark': app.status === 'Offer',
                      'bg-rejected-light text-rejected-dark': app.status === 'Rejected',
                    }">
                    {{ app.status }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>