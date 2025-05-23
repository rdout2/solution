<script setup lang="ts">
import { SignedIn, SignedOut, SignInButton } from '@clerk/vue'
import { useRouter } from 'vue-router'
const router = useRouter()
function goToDashboard() {
  router.push('/dashboard')
}
</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50">
    <h1 class="text-4xl font-bold mb-6">Bienvenue sur JobTracker</h1>
    <p class="mb-8 text-lg">Gérez vos candidatures facilement.</p>
    <SignedOut>
      <SignInButton afterSignInUrl="/dashboard" />
    </SignedOut>
    <SignedIn>
      <button @click="goToDashboard" class="btn btn-primary">Aller au Dashboard</button>
    </SignedIn>
  </div>
</template>
