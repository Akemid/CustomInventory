<script setup lang="ts">
import { type Ref,ref, onMounted } from 'vue'
import { supabase } from '../supabaseClient'

interface Country {
  id: number;
  name: string;
}

const countries:Ref<Country[]> = ref([])

async function getCountries() {
  const { data, error} = await supabase.from('countries').select()
  if (error) {
    console.error('Error fetching countries:', error)
    return
  }
  countries.value = data || []
}
onMounted(() => {  
getCountries()
})
</script>

<template>
  <ul>
    <li v-for="country in countries" :key="country.id">{{ country.name }}</li>
  </ul>
</template>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
