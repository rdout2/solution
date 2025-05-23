<script setup lang="ts">
import { useRouter } from 'vue-router'
import { SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/vue'

const router = useRouter()
function navigateToHome() {
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white border-b border-gray-200 shadow-sm py-4">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center">
          <h1 class="text-xl font-bold text-primary-600 cursor-pointer" @click="navigateToHome">JobTracker</h1>
          
          <SignedIn>
            <nav class="flex gap-4">
              <router-link to="/dashboard" class="text-gray-600 hover:text-primary-600 transition-colors" active-class="text-primary-600 font-medium">
                Applications
              </router-link>
              <router-link to="/metrics" class="text-gray-600 hover:text-primary-600 transition-colors" active-class="text-primary-600 font-medium">
                Metrics
              </router-link>
              <router-link to="/add-job" class="text-gray-600 hover:text-primary-600 transition-colors" active-class="text-primary-600 font-medium">
                Add Job
              </router-link>
              <router-link to="/profile" class="text-gray-600 hover:text-primary-600 transition-colors" active-class="text-primary-600 font-medium">
                Profile
              </router-link>
            </nav>
          </SignedIn>

          <div>
            <SignedOut>
              <SignInButton afterSignInUrl="/dashboard" />
            </SignedOut>
            <SignedIn>
              <UserButton />
            </SignedIn>
          </div>
        </div>
      </div>
    </header>

    <main class="container mx-auto">
      <router-view></router-view>
    </main>
  </div>
</template>
