
<script setup lang="ts">
import ModalGeneral from '../shared/ModalGeneral.vue';
defineProps(
    {
        show: {
            type: Boolean,
            required: true
        }
    },

)

defineEmits([
  'close',])

</script>

<template>
   <Transition name="modal">
      <ModalGeneral 
      v-if="show"
      id="addCategory" title="Agregar Categoria"
      @close="$emit('close')"
      >
      <template #body>
         <div class="mb-3">
            <label class="form-label">Nombre</label>
            <input type="text" class="form-control" placeholder="Categoria 1">
        </div>
      </template>
      <template #footer>
         <div class="modal-footer">
             <button type="button" class="btn btn-secondary" @click="$emit('close')">Cerrar</button>
             <button type="button" class="btn btn-primary">
                 Agregar
             </button>
         </div>
     </template>
         
      </ModalGeneral>
   </Transition>
</template>