const {createApp, ref} = Vue

createApp(
    {
    setup(){
        const classAttributep = ref('')
        const classBsToggle = ref('')
        const editMode = ref(false)
        function setClassAttribute(){
            if (editMode.value == true)
            {
                classAttributep.value = '#editProductModal'
            }
            else {
                classAttributep.value = '#addProductModal'
            }
        }
        function addCategoryModal(pEditMode){
            console.log("clickClose:",pEditMode)
            editMode.value = pEditMode
            classBsToggle.value = 'modal'
            setClassAttribute()
        }
        
        return {
            editMode,
            classAttributep,
            addCategoryModal,
            classBsToggle
        }
    },
    delimiters : ['${','}']
    }
).mount('#modals')