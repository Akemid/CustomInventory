<script setup lang="ts">
import { ref } from 'vue';
import FloatButton from '../components/shared/FloatButton.vue';
// import AddProductModal from '@/components/products/AddProductModal.vue';
// import AddCategoryModal from '@/components/category/AddCategoryModal.vue';
import ListProduct from '@/components/products/ListProduct.vue';

const showAddProductModal = ref(false)
const showAddCategoryModal = ref(false)


function showModal(){
    showAddProductModal.value = true;
}

</script>
<template>
    <ListProduct/>
   <!--  <Teleport to="body">
        <AddProductModal 
        :show="showAddProductModal" 
        @close="showAddProductModal = false"
        @add-category="showAddCategoryModal = true"
        />
    </Teleport>
    <Teleport to="body">
        <AddCategoryModal 
        :show="showAddCategoryModal" 
        @close="showAddCategoryModal = false"/>
    </Teleport> -->
    <FloatButton @add-product="showModal" />
</template>