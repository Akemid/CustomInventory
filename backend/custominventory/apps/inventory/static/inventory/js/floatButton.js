const {createApp, ref} = Vue

createApp(
    {
    setup(){
        const show = ref(false)
        const clickIn = ref(false)
        const clickOut = ref(false)
        function clickButton(){
            clickOut.value = true ? clickIn.value : false
            clickIn.value = !clickIn.value            
            show.value = !show.value
        }
        return {
            show,
            clickIn,
            clickOut,
            clickButton
        }
    },
    delimiters : ['${','}']
    }
).mount('#float-button')