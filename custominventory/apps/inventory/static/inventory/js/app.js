const { createApp, ref } = Vue

createApp(
    {
        setup() {
            const message = ref('Hello vuea!')
            return {
                message
            }
        },
        delimiters : ['${','}']
    }
).mount('#app')