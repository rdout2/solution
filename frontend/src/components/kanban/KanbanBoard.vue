<script setup lang="ts">
import { useApplications } from '../../composables/useApplications';
import KanbanColumn from './KanbanColumn.vue';
import type { ApplicationStatus } from '../../types/application';

const { groupedApplications, loading, error, refresh } = useApplications();

const columns: ApplicationStatus[] = ['Wishlist', 'Applied', 'Interview', 'Offer', 'Rejected'];
</script>

<template>
  <div class="kanban-board-container px-4 py-6 h-full">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gray-900">Job Applications</h1>
      <button 
        @click="refresh" 
        class="px-4 py-2 bg-primary-500 text-white rounded-md hover:bg-primary-600 transition-colors duration-200"
      >
        Refresh
      </button>
    </div>

    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-pulse flex flex-col items-center">
        <div class="h-12 w-12 mb-2 rounded-full bg-primary-200"></div>
        <div class="h-4 w-24 rounded bg-primary-100"></div>
      </div>
    </div>

    <div v-else-if="error" class="p-4 bg-rejected-light text-rejected-dark rounded-md">
      <p>{{ error }}</p>
      <button 
        @click="refresh" 
        class="mt-2 px-3 py-1 bg-white rounded border border-rejected text-rejected-dark hover:bg-rejected-light"
      >
        Try Again
      </button>
    </div>

    <div v-else class="kanban-board flex gap-4 overflow-x-auto pb-4 h-[calc(100vh-140px)]">
      <KanbanColumn 
        v-for="column in columns" 
        :key="column" 
        :title="column" 
        :applications="groupedApplications[column]"
      />
    </div>
  </div>
</template>

<style scoped>
.kanban-board {
  scrollbar-width: thin;
  scrollbar-color: rgba(156, 163, 175, 0.5) rgba(243, 244, 246, 0.5);
}

.kanban-board::-webkit-scrollbar {
  height: 8px;
}

.kanban-board::-webkit-scrollbar-track {
  background: rgba(243, 244, 246, 0.5);
  border-radius: 4px;
}

.kanban-board::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.5);
  border-radius: 4px;
}

.kanban-board::-webkit-scrollbar-thumb:hover {
  background-color: rgba(156, 163, 175, 0.8);
}

.column-body {
  scrollbar-width: thin;
  scrollbar-color: rgba(156, 163, 175, 0.5) rgba(243, 244, 246, 0.5);
  max-height: calc(100vh - 220px);
}

.column-body::-webkit-scrollbar {
  width: 6px;
}

.column-body::-webkit-scrollbar-track {
  background: rgba(243, 244, 246, 0.5);
}

.column-body::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.5);
  border-radius: 4px;
}

.column-body::-webkit-scrollbar-thumb:hover {
  background-color: rgba(156, 163, 175, 0.8);
}
</style>