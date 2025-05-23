import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import KanbanBoard from '../components/kanban/KanbanBoard.vue'
import Profile from '../views/Profile.vue'
import AddJob from '../views/AddJob.vue'
import JobDetails from '../views/JobDetails.vue'
import Metrics from '../views/Metrics.vue'

const routes = [
  { path: '/', name: 'landing', component: LandingPage },
  { path: '/dashboard', name: 'dashboard', component: KanbanBoard, meta: { requiresAuth: true } },
  { path: '/profile', name: 'profile', component: Profile, meta: { requiresAuth: true } },
  { path: '/add-job', name: 'add-job', component: AddJob, meta: { requiresAuth: true } },
  { path: '/job/:id', name: 'job-details', component: JobDetails, props: true, meta: { requiresAuth: true } },
  { path: '/metrics', name: 'metrics', component: Metrics, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

import { useAuth } from '@clerk/vue'
router.beforeEach((to, _from, next) => {
  const { isSignedIn } = useAuth()
  if (to.meta.requiresAuth && !isSignedIn.value) {
    next('/')
  } else {
    next()
  }
})

export default router

