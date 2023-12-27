<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/shared/NavBar.vue';
</script>

<template>
  <NavBar />    
  <RouterView />
</template>
<style>
#app{  
  padding: 0px;
}
</style>
