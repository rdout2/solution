<script setup lang="ts">
import { useRouter } from 'vue-router';
import type { Application } from '../../types/application';

const router = useRouter();
const props = defineProps<{
  application: Application;
}>();

const viewDetails = () => {
  router.push(`/job/${props.application.id}`);
};
</script>

<template>
  <div class="application-card bg-white rounded-lg p-4 mb-3 shadow-card 
              hover:shadow-card-hover transition-all duration-200 
              cursor-pointer border-l-4"
       :class="{
         'border-wishlist': application.status === 'Wishlist',
         'border-applied': application.status === 'Applied',
         'border-interview': application.status === 'Interview',
         'border-offer': application.status === 'Offer',
         'border-rejected': application.status === 'Rejected',
       }"
       @click="viewDetails">
    <div class="flex items-start justify-between">
      <div>
        <h3 class="font-medium text-gray-900 text-base mb-1">{{ application.jobTitle }}</h3>
        <p class="text-gray-500 text-sm">{{ application.company }}</p>
      </div>
      <span class="text-xs text-gray-400">{{ application.date }}</span>
    </div>
    
    <div class="mt-3 flex justify-between items-center">
      <span class="px-2 py-1 rounded-full text-xs font-medium"
            :class="{
              'bg-wishlist-light text-wishlist-dark': application.status === 'Wishlist',
              'bg-applied-light text-applied-dark': application.status === 'Applied',
              'bg-interview-light text-interview-dark': application.status === 'Interview',
              'bg-offer-light text-offer-dark': application.status === 'Offer',
              'bg-rejected-light text-rejected-dark': application.status === 'Rejected',
            }">
        {{ application.status }}
      </span>
    </div>
  </div>
</template>