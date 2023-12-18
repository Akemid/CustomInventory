<script setup>
import { ref } from 'vue'

const show = ref(false)
const clickIn = ref(false)
const clickOut = ref(false)

function clickButton() {
    clickOut.value = clickOut.value == true ? clickIn.value : false
    clickIn.value = !clickIn.value
    show.value = !show.value
}

defineEmits(
    ["add-product"]
)



</script>

<template>
    <button 
    class="btn btn-secondary float-button menu-btn" 
    :class="{ rotation: clickIn, rotation_out: clickOut }"
    @click="clickButton">

    <font-awesome-icon icon="fa-solid fa-gear" />
    </button>
        
    <Transition name="float-options">
        <p v-if="show">
            <button type="button"
            class="btn btn-success float-button add-btn"
            @click="$emit('add-product')"
            >
                   <font-awesome-icon icon="fa-solid fa-plus" />
            </button>
            <button type="button"
             class="btn btn-primary float-button find-btn">
            <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
            </button>
        </p>
    </Transition>
    
</template>

<style scoped>
.float-button{        
    position: absolute;     
    z-index: 10;
    width: 3rem;
    height: 3rem;    
    right: 1rem;
}

.menu-btn{   
    bottom: 2.5rem;
}

.add-btn{   
    bottom: 6rem;
}

.find-btn{
    bottom: 9.5rem;
}


/* we will explain what these classes do next! */
.float-options-enter-active,
.float-options-leave-active {
  transition:  opacity 0.5s ease;

  /*transition: bottom 0.5s ease;*/
}

.float-options-enter-from,
.float-options-leave-to {
  opacity: 0;  
}

.float-options-enter-active .find-btn,
.float-options-leave-active .find-btn {
  transition: bottom 0.5s ease;

}

.float-options-enter-from .find-btn,
.float-options-leave-to  .find-btn{
    bottom: 2.5rem;
}

.float-options-enter-active .add-btn,
.float-options-leave-active .add-btn {
  transition: bottom 0.5s ease;

}

.float-options-enter-from .add-btn,
.float-options-leave-to  .add-btn{
    bottom: 2.5rem;
}


.rotation{
    transition:.9s ease-in-out;
    rotate: -180deg;
}

.rotation_out{
    transition:.7s ease-in-out;
    rotate: 180deg;
}


</style>