<script setup lang="ts">
import { computed } from 'vue';
import type { Application, ApplicationStatus } from '../../types/application';
import ApplicationCard from './ApplicationCard.vue';

const props = defineProps<{
  title: ApplicationStatus;
  applications: Application[];
}>();

const columnColor = computed(() => {
  const colors = {
    'Wishlist': 'bg-wishlist text-white',
    'Applied': 'bg-applied text-white',
    'Interview': 'bg-interview text-white',
    'Offer': 'bg-offer text-white',
    'Rejected': 'bg-rejected text-white'
  };
  return colors[props.title] || 'bg-gray-200 text-gray-800';
});

const columnBgColor = computed(() => {
  const colors = {
    'Wishlist': 'bg-wishlist-light/30',
    'Applied': 'bg-applied-light/30',
    'Interview': 'bg-interview-light/30',
    'Offer': 'bg-offer-light/30',
    'Rejected': 'bg-rejected-light/30'
  };
  return colors[props.title] || 'bg-gray-50';
});
</script>

<template>
  <div class="kanban-column flex flex-col h-full min-w-[280px] max-w-[320px]">
    <div class="column-header p-3 rounded-t-lg" :class="columnColor">
      <div class="flex justify-between items-center">
        <h2 class="font-medium">{{ title }}</h2>
        <span class="bg-white bg-opacity-30 text-white px-2 py-0.5 rounded-full text-xs">
          {{ applications.length }}
        </span>
      </div>
    </div>
    
    <div class="column-body flex-1 p-3 overflow-y-auto" :class="columnBgColor">
      <div v-if="applications.length === 0" class="flex flex-col items-center justify-center h-32 text-gray-400">
        <p class="text-sm">No applications</p>
      </div>
      
      <ApplicationCard 
        v-for="application in applications" 
        :key="application.id" 
        :application="application"
      />
    </div>
    
    <div class="column-footer p-2 bg-white border-t border-gray-100">
      <button class="w-full py-2 px-3 flex items-center justify-center rounded-md bg-gray-50 hover:bg-gray-100 transition-colors duration-200 text-gray-600">
        <span class="mr-1 text-lg font-medium leading-none">+</span>
        <span class="text-sm">Add application</span>
      </button>
    </div>
  </div>
</template>