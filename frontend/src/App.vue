<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/shared/NavBar.vue';
</script>

<template>
  <div class="flex flex-col w-screen h-screen">
    <NavBar />    
    <RouterView />
  </div>
</template>
<style>



body{
  background-color: aliceblue;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

}

@media (min-width: 1024px) {
  body{
    display:block;
  }
}

#app{  
  padding: 0px;
  margin: 0;
}
</style>
