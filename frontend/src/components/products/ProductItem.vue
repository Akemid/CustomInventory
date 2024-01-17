<script lang="ts" setup>


interface Product {
  id: number;
  name: string;
  short_name: string;
  description: string;
  img_url: string;
}

const props = defineProps<{
  product: Product
}>()

</script>

<template>
    <div class="relative flex  flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-md mb-10">
        <div class="relative mx-4 -mt-6 h-56 overflow-hidden rounded-xl bg-blue-gray-500 bg-clip-border text-white shadow-lg shadow-blue-gray-500/40">
          <img
            :src="props.product.img_url"
            alt="img-blur-shadow"
            layout="fill"
          />
        </div>
        <div class="p-6">
          <h5 class="mb-2 block font-sans text-xl font-semibold leading-snug tracking-normal text-blue-gray-900 antialiased">
            {{props.product.name}}
          </h5>
          <p class="block font-sans text-base font-light leading-relaxed text-inherit antialiased">
            {{props.product.description}}
          </p>
        </div>
        <div class="p-6 pt-0">
          <button
            class="select-none rounded-lg bg-pink-500 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-pink-500/20 transition-all hover:shadow-lg hover:shadow-pink-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
            type="button"
            data-ripple-light="true"
          >
            Read More
          </button>
        </div>
      </div>
      
</template>