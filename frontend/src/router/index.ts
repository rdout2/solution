import { createRouter, createWebHistory } from 'vue-router';
import KanbanBoard from '../components/kanban/KanbanBoard.vue';
import Profile from '../views/Profile.vue';
import AddJob from '../views/AddJob.vue';
import JobDetails from '../views/JobDetails.vue';
import Metrics from '../views/Metrics.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: KanbanBoard
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/add-job',
      name: 'add-job',
      component: AddJob
    },
    {
      path: '/job/:id',
      name: 'job-details',
      component: JobDetails,
      props: true
    },
    {
      path: '/metrics',
      name: 'metrics',
      component: Metrics
    }
  ]
});

export default router;