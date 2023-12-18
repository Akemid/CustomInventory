<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  idModalToReturn: {
    type: String,
  },
  id:{
    type: String,
    required: true
  }
})
defineEmits([
  'close',
])
</script>

<template>
    <div class="modal">
      <div class="modal-dialog modal-dialog-scrollable  modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5">
              {{ title }}
            </h1>
            <button type="button" class="btn-close" 
            @click="$emit('close')"
            ></button>
          </div>
          <div class="modal-body">
            <slot name="body">

            </slot>
          </div>
          <slot name="footer">
          </slot>
          
        </div>
      </div>
    </div>
</template>
<style>
.modal{
  position: fixed;
  display: flex;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  transition: opacity 0.3s ease;
}
.modal-dialog{
  margin: auto;
  transition: all 0.3s ease;
}
.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>