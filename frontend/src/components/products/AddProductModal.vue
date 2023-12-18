
<script setup>
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
  'close',
  'add-category',
])


</script>

<template>
    <Transition name="modal">    
        <ModalGeneral 
         v-if="show"
         id="addProduct" title="Agregar productos"
         @close="$emit('close')"
        >
            <template #body>
                <div class="mb-3">
                    <label class="form-label">Nombre</label>
                    <input type="text" class="form-control" placeholder="Colonia abcd">
                </div>
                <div class="mb-3">
                    <label class="form-label">Nombre corto</label>
                    <input type="text" class="form-control" placeholder="abcd">
                </div>
                <div class="mb-3">
                    <label class="form-label">Descripción</label>
                    <input type="text" class="form-control" placeholder="Esta es una colonia para ...">
                </div>
                <div class="mb-3">
                    <label class="form-label">Categoria</label>
                    <div class="input-group mb-3">
                        <select class="form-select" aria-label="Default select example">
                            <option selected>Seleccione categoria</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select>
                        <button type="button"
                            class="btn btn-secondary"
                            @click="$emit('add-category')"
                            >+</button>
                    </div>
                </div>
                <div class="mb-3">
                    <label class="form-label">Marca</label>
                    <div class="input-group mb-3">
                        <select class="form-select" aria-label="Default select example">
                            <option selected>Seleccione marca</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select>
                        <button type="button" class="btn btn-secondary">+</button>
                    </div>
                </div>
                <div class="mb-3">
                    <label class="form-label">Stock inicial</label>
                    <input type="number" min=0 class="form-control" placeholder="0">
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
