<script setup lang="ts">
import { SignedIn, SignedOut, SignInButton, SignUpButton, useAuth } from '@clerk/vue'
import { useRouter } from 'vue-router'
import { watch } from 'vue'

const router = useRouter()
const { isSignedIn } = useAuth()

// Redirection automatique si déjà connecté
watch(isSignedIn, (signedIn) => {
  if (signedIn) {
    router.push('/dashboard')
  }
}, { immediate: true })

function goToDashboard() {
  router.push('/dashboard')
}
</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50">
    <h1 class="text-4xl font-bold mb-6">Bienvenue sur JobTracker</h1>
    <p class="mb-8 text-lg">Gérez vos candidatures facilement.</p>
    
    <SignedOut>
      <div class="flex gap-4">
        <SignInButton afterSignInUrl="/dashboard" class="btn btn-primary" />
        <SignUpButton afterSignUpUrl="/dashboard" class="btn btn-secondary" />
      </div>
    </SignedOut>
    
    <SignedIn>
      <button @click="goToDashboard" class="btn btn-primary">Aller au Dashboard</button>
    </SignedIn>
  </div>
</template>
