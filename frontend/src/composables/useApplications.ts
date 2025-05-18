import { ref, computed, onMounted } from 'vue';
import type { Application, GroupedApplications, ApplicationStatus } from '../types/application';

export function useApplications() {
  const applications = ref<Application[]>([]);
  const loading = ref(true);
  const error = ref<string | null>(null);

  const groupedApplications = computed<GroupedApplications>(() => {
    const result: GroupedApplications = {
      Wishlist: [],
      Applied: [],
      Interview: [],
      Offer: [],
      Rejected: [],
    };

    applications.value.forEach(app => {
      result[app.status].push(app);
    });

    return result;
  });

  const fetchApplications = async () => {
    loading.value = true;
    error.value = null;

    try {
      const response = await fetch('http://localhost:5000/api/applications');
      
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      
      const data = await response.json();
      applications.value = data;
    } catch (err) {
      console.error('Failed to fetch applications:', err);
      error.value = err instanceof Error ? err.message : 'An unknown error occurred';
      
      // Fallback mock data for development if the API is not available
      if (import.meta.env.DEV) {
        applications.value = generateMockData();
      }
    } finally {
      loading.value = false;
    }
  };

  onMounted(() => {
    fetchApplications();
  });

  return {
    applications,
    groupedApplications,
    loading,
    error,
    refresh: fetchApplications
  };
}

// Generate mock data for development when API is unavailable
function generateMockData(): Application[] {
  const statuses: ApplicationStatus[] = ['Wishlist', 'Applied', 'Interview', 'Offer', 'Rejected'];
  const companies = ['Apple', 'Google', 'Microsoft', 'Amazon', 'Netflix', 'Meta', 'Spotify', 'Twitter', 'Airbnb', 'Uber'];
  const jobTitles = [
    'Frontend Developer', 
    'Backend Engineer', 
    'Full Stack Developer', 
    'UI/UX Designer', 
    'Product Manager', 
    'DevOps Engineer',
    'Data Scientist',
    'Mobile Developer',
    'Software Engineer',
    'QA Engineer'
  ];

  return Array.from({ length: 20 }, (_, i) => ({
    id: i + 1,
    jobTitle: jobTitles[Math.floor(Math.random() * jobTitles.length)],
    company: companies[Math.floor(Math.random() * companies.length)],
    status: statuses[Math.floor(Math.random() * statuses.length)],
    date: new Date(Date.now() - Math.floor(Math.random() * 30) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
  }));
}