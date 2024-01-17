<script lang="ts" setup>
import {type Ref, ref} from 'vue'
import { onMounted } from 'vue';
import { supabase } from '../../supabaseClient'
import ProductItem from './ProductItem.vue'


interface Product {
  id: number;
  name: string;
  short_name: string;
  description: string;
  img_url: string;
}

const products:Ref<Product[]> = ref([])

async function getProducts() {
  const { data, error} = await supabase.from('products').select().order('id', { ascending: true })
  if (error) {
    console.error('Error fetching products:', error) 
    return
  }
  products.value = data || []
  console.log(products.value)
}
onMounted(() => {  
    getProducts()
})

</script>
<template>
    <div class="mt-20 grid lg:grid-cols-4 lg:gap-9">
        <ProductItem v-for="product in products" :key="product.id" :product="product"/>        
    </div>

</template>